from prompt_toolkit.styles import Style

INSTANTCMD_STYLE = Style.from_dict({
    # Completion menu
    "completion-menu":                  "bg:#1e1e1e #cccccc",
    "completion-menu.completion":       "bg:#1e1e1e #cccccc",
    "completion-menu.completion.current": "bg:#264f78 #ffffff bold",
    "completion-menu.meta.completion":  "bg:#1e1e1e #888888 italic",
    "completion-menu.meta.completion.current": "bg:#264f78 #bbbbbb italic",
    "scrollbar.background":            "bg:#333333",
    "scrollbar.button":                "bg:#666666",

    # Prompt
    "prompt":                          "#569cd6 bold",
    "prompt.path":                     "#dcdcaa",
    "prompt.arrow":                    "#608b4e bold",

    # Input text
    "":                                "#d4d4d4",

    # Bottom toolbar
    "bottom-toolbar":                  "bg:#007acc #ffffff",
    "bottom-toolbar.text":             "bg:#007acc #ffffff",

    # Search
    "search":                          "#ce9178",
    "search.other":                    "#ce9178",
})

BANNER = r"""
  ___           _              _    ____ __  __ ____
 |_ _|_ __  ___| |_ __ _ _ __ | |_ / ___|  \/  |  _ \
  | || '_ \/ __| __/ _` | '_ \| __| |   | |\/| | | | |
  | || | | \__ \ || (_| | | | | |_| |___| |  | | |_| |
 |___|_| |_|___/\__\__,_|_| |_|\__|\____|_|  |_|____/
"""

WELCOME_MESSAGE = """\033[36m{banner}\033[0m
 \033[33mInstantCMD\033[0m - Command Prompt with live autocomplete
 Type commands and get instant suggestions as you type.

 \033[90m  Arrow Keys  Navigate suggestions       Tab    Complete
   Enter      Run command/selection      Ctrl+C  Cancel
   Ctrl+D     Exit InstantCMD            F1      Toggle help\033[0m
""".format(banner=BANNER)
