# InstantCMD

**Command Prompt with live autocomplete** — like Google Instant meets Windows CMD.

Type and get real-time dropdown suggestions for commands, flags, files, folders, and executables on PATH.

![concept](https://img.shields.io/badge/Windows-CMD-blue?style=flat-square&logo=windows)
![python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square&logo=python)

## What It Does

```
> d
  dir          List directory contents
  date         Display or set the date
  del          Delete one or more files
  diskpart     Disk partition manager
  dism         Deployment Image Servicing and Management
  defrag       Defragment disk drives
  doskey       Edit command line, recall commands, create macros
```

Type `di` and it narrows to:

```
> di
  dir          List directory contents
  diskpart     Disk partition manager
  dism         Deployment Image Servicing and Management
```

After selecting a command, get flag suggestions:

```
> dir /
  /a    Display files with specified attributes
  /b    Bare format (no heading or summary)
  /s    Include subdirectories (recursive)
  /w    Wide list format
  ...
```

## Features

- **Live autocomplete dropdown** as you type — no tab-spam needed
- **150+ built-in CMD commands** with descriptions
- **Flag/switch suggestions** per command (e.g. `dir /s`, `ping -t`)
- **File & folder path completion** with live directory scanning
- **Executable discovery** — finds all `.exe`, `.bat`, `.cmd` on your PATH
- **Command history** with auto-suggest (ghost text from past commands)
- **Syntax highlighting** — commands, flags, pipes, strings, variables get colored
- **Real CMD execution** — commands actually run through `cmd.exe`
- **Persistent history** saved to `~/.instantcmd_history`

## Controls

| Key | Action |
|-----|--------|
| **Arrow Keys** | Navigate through suggestions |
| **Tab** | Accept the selected completion |
| **Enter** | Run the command |
| **Ctrl+C** | Cancel current input |
| **Ctrl+D** | Exit InstantCMD |
| **Ctrl+L** | Clear screen |

## Quick Start

### 1. Setup

```batch
:: Clone or download, then:
cd InstantCMD
setup.bat
```

### 2. Run

```batch
run.bat
```

Or directly:

```batch
python instantcmd.py
```

### Requirements

- **Windows 10/11**
- **Python 3.8+** ([python.org](https://python.org))
- `prompt_toolkit` (auto-installed by setup)

## How It Works

InstantCMD uses `prompt_toolkit` to create a rich terminal UI with:

1. **Multi-source completer** — combines command database, PATH scanning, file globbing, and history
2. **Real-time lexer** — tokenizes input to color commands, flags, pipes, strings, and variables
3. **CMD execution** — pipes commands to `cmd.exe /c` so everything works like real Command Prompt
4. **Internal handling** — `cd`, `set`, `pushd`/`popd`, `cls`, `title` are handled natively to maintain state

## Project Structure

```
InstantCMD/
├── instantcmd.py      # Main shell application & REPL loop
├── commands.py        # Database of 150+ CMD commands with flags & descriptions
├── completer.py       # Multi-source completion engine
├── lexer.py           # Syntax highlighting tokenizer
├── style.py           # Theme, colors, and banner
├── requirements.txt   # Python dependencies
├── setup.bat          # One-click setup script
├── run.bat            # One-click launcher
├── icon.ico           # Application icon
├── docs/              # Landing page (GitHub Pages)
└── .gitignore
```

## Why This Exists

Windows Command Prompt hasn't had real autocomplete for decades. PowerShell has `PSReadLine`, Linux has `zsh-autosuggestions` and `fish` shell. CMD users got nothing.

**InstantCMD** fills that gap — it gives CMD the same "just start typing and see what's available" experience that every modern tool has.

> "It makes CMD autocomplete like a modern search bar"

## License

MIT — do whatever you want with it.
