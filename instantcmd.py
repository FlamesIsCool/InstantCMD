"""InstantCMD - Command Prompt with live autocomplete."""

import os
import sys
import subprocess
import ctypes
import asyncio

from prompt_toolkit import PromptSession


def _enable_ansi_colors():
    """Enable ANSI escape codes on Windows 10+."""
    if sys.platform != "win32":
        return
    try:
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_ulong()
        kernel32.GetConsoleMode(handle, ctypes.byref(mode))
        kernel32.SetConsoleMode(handle, mode.value | 0x0004)
    except Exception:
        pass


_enable_ansi_colors()


def _suppress_asyncio_errors():
    """Suppress asyncio overlapped future errors on Windows."""
    def _silent_exception_handler(loop, context):
        if 'overlapped' in str(context.get('message', '')).lower():
            return
        if 'overlapped' in str(context.get('future', '')).lower():
            return
        # For non-overlapped errors, use default handling
        loop.default_exception_handler(context)

    try:
        loop = asyncio.get_event_loop()
        loop.set_exception_handler(_silent_exception_handler)
    except RuntimeError:
        pass


_suppress_asyncio_errors()


class _AsyncioErrorFilter:
    """Stderr filter for asyncio overlapped future noise."""

    _SUPPRESS = (
        "cancelling an overlapped future",
        "_OverlappedFuture",
        "_cancel_overlapped",
        "The handle is invalid",
    )

    def __init__(self, real_stderr):
        self._real = real_stderr
        self._buffer = ""

    def write(self, text):
        self._buffer += text
        while "\n" in self._buffer:
            line, _, self._buffer = self._buffer.partition("\n")
            if not any(s in line for s in self._SUPPRESS):
                self._real.write(line + "\n")

    def flush(self):
        if self._buffer and not any(s in self._buffer for s in self._SUPPRESS):
            self._real.write(self._buffer)
        self._buffer = ""
        self._real.flush()

    def __getattr__(self, name):
        return getattr(self._real, name)


from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style

from completer import InstantCompleter
from lexer import CMDLexer
from style import INSTANTCMD_STYLE, WELCOME_MESSAGE
from commands import CMD_COMMANDS


def get_prompt_text():
    cwd = os.getcwd()
    return HTML(
        '<prompt>{cwd}</prompt><arrow> > </arrow>'
    ).format(cwd=cwd)


def get_toolbar_text():
    return HTML(
        ' <b>InstantCMD</b> | '
        'Tab: complete | '
        'Arrow Keys: navigate | '
        'Enter: run | '
        'Ctrl+D: exit'
    )


INTERNAL_COMMANDS = {"exit", "quit", "cd", "chdir", "pushd", "popd", "set", "title", "cls", "clear"}


def handle_cd(args):
    if not args:
        print(os.getcwd())
        return

    target = " ".join(args)

    if target.lower().startswith("/d "):
        target = target[3:].strip()

    # Strip surrounding quotes
    if (target.startswith('"') and target.endswith('"')) or \
       (target.startswith("'") and target.endswith("'")):
        target = target[1:-1]

    target = os.path.expandvars(target)

    if target == "-":
        target = os.environ.get("OLDPWD", os.getcwd())

    try:
        old_dir = os.getcwd()
        os.chdir(target)
        os.environ["OLDPWD"] = old_dir
    except FileNotFoundError:
        print(f"The system cannot find the path specified: {target}")
    except PermissionError:
        print(f"Access is denied: {target}")
    except OSError as e:
        print(f"Error: {e}")


def handle_set(args):
    if not args:
        for key, value in sorted(os.environ.items()):
            print(f"{key}={value}")
        return

    expr = " ".join(args)
    if "=" in expr:
        key, _, value = expr.partition("=")
        key = key.strip()
        value = value.strip()
        if not value:
            os.environ.pop(key, None)
        else:
            os.environ[key] = value
    else:
        prefix = expr.upper()
        for key, value in sorted(os.environ.items()):
            if key.upper().startswith(prefix):
                print(f"{key}={value}")


def execute_command(command_text):
    command_text = command_text.strip()
    if not command_text:
        return

    parts = command_text.split()
    cmd = parts[0].lower()
    args = parts[1:]

    if cmd in ("exit", "quit"):
        raise SystemExit(0)

    if cmd in ("cd", "chdir"):
        handle_cd(args)
        return

    if cmd == "pushd":
        if args:
            old_dir = os.getcwd()
            handle_cd(args)
            os.environ.setdefault("DIRSTACK", "")
            stack = os.environ["DIRSTACK"]
            os.environ["DIRSTACK"] = old_dir + (";" + stack if stack else "")
        else:
            print("The syntax of the command is incorrect.")
        return

    if cmd == "popd":
        stack = os.environ.get("DIRSTACK", "")
        if stack:
            dirs = stack.split(";")
            target = dirs[0]
            os.environ["DIRSTACK"] = ";".join(dirs[1:])
            handle_cd([target])
        else:
            print("Unable to pop directory - stack is empty.")
        return

    if cmd == "set":
        handle_set(args)
        return

    if cmd == "title":
        title = " ".join(args) if args else "InstantCMD"
        if sys.platform == "win32":
            ctypes.windll.kernel32.SetConsoleTitleW(title)
        else:
            sys.stdout.write(f"\033]0;{title}\007")
            sys.stdout.flush()
        return

    if cmd in ("cls", "clear"):
        os.system("cls" if sys.platform == "win32" else "clear")
        return

    # Execute external command via cmd.exe
    _real_stderr = sys.stderr
    try:
        sys.stderr = _AsyncioErrorFilter(_real_stderr)
        subprocess.run(
            command_text,
            shell=True,
            cwd=os.getcwd(),
            env=os.environ.copy(),
        )
    except KeyboardInterrupt:
        print("^C")
    except Exception as e:
        print(f"Error executing command: {e}")
    finally:
        sys.stderr = _real_stderr


def setup_keybindings():
    kb = KeyBindings()

    @kb.add("c-l")
    def clear_screen(event):
        event.app.renderer.clear()

    return kb


def main():
    if sys.platform == "win32":
        ctypes.windll.kernel32.SetConsoleTitleW("InstantCMD")

    # Print welcome banner
    print(WELCOME_MESSAGE)

    # History file in user's home directory
    history_path = os.path.join(os.path.expanduser("~"), ".instantcmd_history")

    # Create the prompt session
    session = PromptSession(
        completer=InstantCompleter(),
        complete_while_typing=True,
        lexer=CMDLexer(),
        style=INSTANTCMD_STYLE,
        history=FileHistory(history_path),
        auto_suggest=AutoSuggestFromHistory(),
        bottom_toolbar=get_toolbar_text,
        key_bindings=setup_keybindings(),
        mouse_support=False,
        complete_in_thread=True,
        # Completion settings
        reserve_space_for_menu=8,
    )

    # Main REPL loop
    while True:
        try:
            user_input = session.prompt(get_prompt_text)
            if user_input.strip():
                execute_command(user_input)
        except KeyboardInterrupt:
            # Ctrl+C - cancel current line
            print("^C")
            continue
        except EOFError:
            # Ctrl+D - exit
            print("\nGoodbye!")
            break
        except SystemExit:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
