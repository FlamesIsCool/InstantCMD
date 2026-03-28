import os
import glob
from prompt_toolkit.completion import Completer, Completion
from commands import CMD_COMMANDS


class InstantCompleter(Completer):

    def __init__(self):
        self._path_executables = None

    @property
    def path_executables(self):
        if self._path_executables is None:
            self._path_executables = self._scan_path()
        return self._path_executables

    def _scan_path(self):
        executables = {}
        path_dirs = os.environ.get("PATH", "").split(os.pathsep)
        seen = set()
        exe_extensions = os.environ.get("PATHEXT", ".COM;.EXE;.BAT;.CMD").lower().split(";")

        for directory in path_dirs:
            directory = directory.strip()
            if not directory or not os.path.isdir(directory):
                continue
            try:
                for entry in os.scandir(directory):
                    if entry.is_file():
                        name_lower = entry.name.lower()
                        _, ext = os.path.splitext(name_lower)
                        if ext in exe_extensions:
                            base_name = os.path.splitext(entry.name)[0].lower()
                            if base_name not in seen and base_name not in CMD_COMMANDS:
                                seen.add(base_name)
                                executables[base_name] = f"[PATH] {entry.path}"
            except (PermissionError, OSError):
                continue

        return executables

    def _get_path_completions(self, partial_path):
        if not partial_path:
            partial_path = "."

        # Expand environment variables
        expanded = os.path.expandvars(partial_path)

        # Build glob pattern
        if os.path.isdir(expanded):
            search_pattern = os.path.join(expanded, "*")
        else:
            search_pattern = expanded + "*"

        try:
            matches = glob.glob(search_pattern)
        except (OSError, ValueError):
            return

        for match in matches[:50]:
            display = os.path.basename(match)
            if os.path.isdir(match):
                display += "\\"

                if partial_path == ".":
                text = ".\\" + os.path.basename(match)
                if os.path.isdir(match):
                    text += "\\"
            else:
                text = match
                if os.path.isdir(match):
                    text += "\\"

            meta = "Directory" if os.path.isdir(match) else "File"
            yield Completion(
                text,
                start_position=-len(partial_path),
                display=display,
                display_meta=meta,
            )

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        text_stripped = text.lstrip()

        if not text_stripped:
            for cmd, info in sorted(CMD_COMMANDS.items()):
                yield Completion(
                    cmd,
                    start_position=0,
                    display=cmd,
                    display_meta=info["description"],
                )
            return

        parts = text_stripped.split()
        word_before_cursor = document.get_word_before_cursor(WORD=True)

        if len(parts) <= 1 and not text_stripped.endswith(" "):
            prefix = parts[0].lower() if parts else ""

            for cmd, info in sorted(CMD_COMMANDS.items()):
                if cmd.startswith(prefix):
                    yield Completion(
                        cmd,
                        start_position=-len(prefix),
                        display=cmd,
                        display_meta=info["description"],
                    )

            for exe, desc in sorted(self.path_executables.items()):
                if exe.startswith(prefix):
                    yield Completion(
                        exe,
                        start_position=-len(prefix),
                        display=exe,
                        display_meta="Executable on PATH",
                    )
            return

        cmd = parts[0].lower()
        current_word = word_before_cursor

        if current_word.startswith("/") or current_word.startswith("-"):
            if cmd in CMD_COMMANDS:
                flags = CMD_COMMANDS[cmd].get("flags", {})
                prefix = current_word.lower()
                for flag, desc in sorted(flags.items()):
                    if flag.lower().startswith(prefix):
                        yield Completion(
                            flag,
                            start_position=-len(current_word),
                            display=flag,
                            display_meta=desc,
                        )
            return

        if cmd in CMD_COMMANDS:
            flags = CMD_COMMANDS[cmd].get("flags", {})

            used_flags = {p.lower() for p in parts[1:]}
            for flag, desc in sorted(flags.items()):
                if flag.lower() not in used_flags:
                    yield Completion(
                        flag,
                        start_position=-len(current_word) if current_word else 0,
                        display=flag,
                        display_meta=desc,
                    )

        if current_word:
            yield from self._get_path_completions(current_word)
        else:
            yield from self._get_path_completions(".")
