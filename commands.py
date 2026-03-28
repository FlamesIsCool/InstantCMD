# Built-in CMD commands, flags, and descriptions.
# Format: command_name -> { description, flags: { flag: description } }
CMD_COMMANDS = {
    # --- File & Directory ---
    "dir": {
        "description": "List directory contents",
        "flags": {
            "/a": "Display files with specified attributes",
            "/a:d": "Directories only",
            "/a:h": "Hidden files",
            "/a:s": "System files",
            "/a:r": "Read-only files",
            "/a:-d": "Not directories",
            "/b": "Bare format (no heading or summary)",
            "/c": "Display thousand separator in file sizes",
            "/d": "Wide list sorted by column",
            "/l": "Use lowercase",
            "/n": "Long list format with filenames on the right",
            "/o": "Sort order (N=name, S=size, E=ext, D=date, G=group dirs)",
            "/o:n": "Sort by name",
            "/o:s": "Sort by size",
            "/o:e": "Sort by extension",
            "/o:d": "Sort by date",
            "/p": "Pause after each screen",
            "/q": "Display owner of file",
            "/r": "Display alternate data streams",
            "/s": "Include subdirectories (recursive)",
            "/t": "Time field to display (C=creation, A=access, W=write)",
            "/w": "Wide list format",
            "/x": "Display short names for non-8dot3 filenames",
            "/?": "Display help",
        },
    },
    "cd": {
        "description": "Change directory",
        "flags": {
            "/d": "Change drive and directory",
            "..": "Go up one directory",
            "\\": "Go to root of drive",
            "/?": "Display help",
        },
    },
    "chdir": {
        "description": "Change directory (alias for cd)",
        "flags": {
            "/d": "Change drive and directory",
            "/?": "Display help",
        },
    },
    "md": {
        "description": "Create a directory",
        "flags": {"/?": "Display help"},
    },
    "mkdir": {
        "description": "Create a directory",
        "flags": {"/?": "Display help"},
    },
    "rd": {
        "description": "Remove a directory",
        "flags": {
            "/s": "Remove directory tree (all subdirectories and files)",
            "/q": "Quiet mode, don't ask for confirmation",
            "/?": "Display help",
        },
    },
    "rmdir": {
        "description": "Remove a directory",
        "flags": {
            "/s": "Remove directory tree",
            "/q": "Quiet mode",
            "/?": "Display help",
        },
    },
    "tree": {
        "description": "Display directory structure as a tree",
        "flags": {
            "/f": "Display names of files in each folder",
            "/a": "Use ASCII characters instead of graphic chars",
            "/?": "Display help",
        },
    },

    # --- File Operations ---
    "copy": {
        "description": "Copy files to another location",
        "flags": {
            "/a": "ASCII text file",
            "/b": "Binary file",
            "/d": "Allow destination to be created decrypted",
            "/v": "Verify new files are written correctly",
            "/y": "Suppress confirmation prompt for overwriting",
            "/-y": "Prompt for confirmation before overwriting",
            "/?": "Display help",
        },
    },
    "xcopy": {
        "description": "Copy files and directory trees",
        "flags": {
            "/s": "Copy directories and subdirectories (non-empty)",
            "/e": "Copy directories and subdirectories (including empty)",
            "/h": "Copy hidden and system files",
            "/r": "Overwrite read-only files",
            "/y": "Suppress prompt for overwriting",
            "/i": "Assume destination is directory if copying multiple files",
            "/q": "Quiet mode",
            "/k": "Copy attributes (normally resets read-only)",
            "/d": "Copy files changed on or after a date",
            "/?": "Display help",
        },
    },
    "robocopy": {
        "description": "Robust file copy (advanced)",
        "flags": {
            "/s": "Copy subdirectories (non-empty)",
            "/e": "Copy subdirectories (including empty)",
            "/mir": "Mirror a directory tree",
            "/mov": "Move files (delete from source after copy)",
            "/move": "Move files and dirs (delete from source)",
            "/z": "Copy in restartable mode",
            "/b": "Copy in backup mode",
            "/mt": "Multi-threaded copying (default 8 threads)",
            "/r:n": "Number of retries on failed copies",
            "/w:n": "Wait time between retries",
            "/log:file": "Log output to file",
            "/np": "No progress - don't show % copied",
            "/eta": "Show estimated time of arrival",
            "/xf": "Exclude files matching names/paths/wildcards",
            "/xd": "Exclude directories matching names/paths",
            "/?": "Display help",
        },
    },
    "move": {
        "description": "Move files from one directory to another",
        "flags": {
            "/y": "Suppress confirmation prompt",
            "/-y": "Prompt for confirmation",
            "/?": "Display help",
        },
    },
    "del": {
        "description": "Delete one or more files",
        "flags": {
            "/p": "Prompt before deleting each file",
            "/f": "Force delete read-only files",
            "/s": "Delete from all subdirectories",
            "/q": "Quiet mode",
            "/a": "Select files by attributes",
            "/?": "Display help",
        },
    },
    "erase": {
        "description": "Delete one or more files (alias for del)",
        "flags": {
            "/p": "Prompt before deleting",
            "/f": "Force delete read-only files",
            "/s": "Delete from subdirectories",
            "/q": "Quiet mode",
            "/?": "Display help",
        },
    },
    "ren": {
        "description": "Rename a file or files",
        "flags": {"/?": "Display help"},
    },
    "rename": {
        "description": "Rename a file or files",
        "flags": {"/?": "Display help"},
    },
    "type": {
        "description": "Display the contents of a text file",
        "flags": {"/?": "Display help"},
    },
    "more": {
        "description": "Display output one screen at a time",
        "flags": {
            "/e": "Enable extended features",
            "/c": "Clear screen before displaying page",
            "/p": "Expand form-feed characters",
            "/s": "Squeeze multiple blank lines into one",
            "/t:n": "Expand tabs to n spaces",
            "+n": "Start displaying at line n",
            "/?": "Display help",
        },
    },

    # --- System Info ---
    "systeminfo": {
        "description": "Display detailed system configuration",
        "flags": {
            "/s": "Remote system to connect to",
            "/u": "User context for command",
            "/p": "Password for user context",
            "/fo": "Output format (TABLE, LIST, CSV)",
            "/nh": "No header in output",
            "/?": "Display help",
        },
    },
    "hostname": {
        "description": "Display the computer's hostname",
        "flags": {},
    },
    "ver": {
        "description": "Display Windows version",
        "flags": {},
    },
    "date": {
        "description": "Display or set the date",
        "flags": {
            "/t": "Display date only (no prompt to set)",
            "/?": "Display help",
        },
    },
    "time": {
        "description": "Display or set the system time",
        "flags": {
            "/t": "Display time only (no prompt to set)",
            "/?": "Display help",
        },
    },
    "vol": {
        "description": "Display disk volume label and serial number",
        "flags": {"/?": "Display help"},
    },
    "label": {
        "description": "Create, change, or delete volume label",
        "flags": {"/?": "Display help"},
    },

    # --- Process Management ---
    "tasklist": {
        "description": "Display list of running processes",
        "flags": {
            "/s": "Remote system to connect to",
            "/u": "User context",
            "/p": "Password",
            "/m": "List modules loaded by each task",
            "/svc": "Display services hosted in each process",
            "/v": "Verbose output",
            "/fo": "Output format (TABLE, LIST, CSV)",
            "/nh": "No header in output",
            "/fi": "Filter (e.g. \"STATUS eq RUNNING\")",
            "/?": "Display help",
        },
    },
    "taskkill": {
        "description": "Kill or stop a running process",
        "flags": {
            "/pid": "Process ID to kill",
            "/im": "Image name of process to kill",
            "/f": "Force kill",
            "/t": "Kill process tree",
            "/s": "Remote system",
            "/u": "User context",
            "/p": "Password",
            "/?": "Display help",
        },
    },
    "start": {
        "description": "Start a program or command in a new window",
        "flags": {
            "/min": "Start minimized",
            "/max": "Start maximized",
            "/wait": "Wait for program to finish",
            "/b": "Start without creating new window",
            "/low": "Start with IDLE priority",
            "/normal": "Start with NORMAL priority",
            "/high": "Start with HIGH priority",
            "/realtime": "Start with REALTIME priority",
            "/d": "Specify starting directory",
            "/?": "Display help",
        },
    },

    # --- Networking ---
    "ipconfig": {
        "description": "Display IP configuration",
        "flags": {
            "/all": "Display full configuration",
            "/release": "Release DHCP lease",
            "/renew": "Renew DHCP lease",
            "/flushdns": "Flush DNS resolver cache",
            "/registerdns": "Refresh DHCP and re-register DNS",
            "/displaydns": "Display contents of DNS resolver cache",
            "/?": "Display help",
        },
    },
    "ping": {
        "description": "Send ICMP echo requests to a host",
        "flags": {
            "-t": "Ping continuously until stopped",
            "-a": "Resolve address to hostname",
            "-n": "Number of echo requests to send",
            "-l": "Send buffer size",
            "-f": "Set Don't Fragment flag",
            "-i": "Time to Live",
            "-4": "Force IPv4",
            "-6": "Force IPv6",
            "/?": "Display help",
        },
    },
    "tracert": {
        "description": "Trace route to a remote host",
        "flags": {
            "-d": "Don't resolve addresses to hostnames",
            "-h": "Maximum number of hops",
            "-w": "Timeout in milliseconds for each reply",
            "-4": "Force IPv4",
            "-6": "Force IPv6",
            "/?": "Display help",
        },
    },
    "netstat": {
        "description": "Display network statistics and connections",
        "flags": {
            "-a": "Display all connections and listening ports",
            "-b": "Display executable involved in creating connection",
            "-e": "Display Ethernet statistics",
            "-n": "Display addresses and ports numerically",
            "-o": "Display owning process ID",
            "-p": "Show connections for specified protocol",
            "-r": "Display routing table",
            "-s": "Display per-protocol statistics",
            "/?": "Display help",
        },
    },
    "nslookup": {
        "description": "Query DNS name servers",
        "flags": {"/?": "Display help"},
    },
    "net": {
        "description": "Manage network resources",
        "flags": {
            "use": "Connect/disconnect from shared resource",
            "user": "Manage user accounts",
            "view": "Display shared resources on computer",
            "share": "Manage shared resources",
            "start": "Start a network service",
            "stop": "Stop a network service",
            "session": "Manage server sessions",
            "statistics": "Display network statistics",
            "localgroup": "Manage local groups",
            "accounts": "Update user accounts database",
            "config": "Display configuration info",
            "/?": "Display help",
        },
    },
    "netsh": {
        "description": "Network shell - configure network settings",
        "flags": {
            "wlan": "Wireless LAN commands",
            "interface": "Interface commands",
            "firewall": "Firewall configuration",
            "advfirewall": "Advanced firewall configuration",
            "http": "HTTP configuration",
            "/?": "Display help",
        },
    },
    "arp": {
        "description": "Display and modify ARP cache",
        "flags": {
            "-a": "Display current ARP entries",
            "-g": "Same as -a",
            "-d": "Delete a host entry",
            "-s": "Add a static entry",
            "/?": "Display help",
        },
    },
    "nbtstat": {
        "description": "Display NetBIOS over TCP/IP statistics",
        "flags": {
            "-a": "List remote machine's name table by name",
            "-A": "List remote machine's name table by IP",
            "-c": "List remote name cache",
            "-n": "List local NetBIOS names",
            "-r": "List names resolved by broadcast/WINS",
            "-R": "Purge and reload remote cache",
            "-s": "List sessions table",
            "-S": "List sessions with destination IP",
            "/?": "Display help",
        },
    },
    "route": {
        "description": "Manipulate network routing tables",
        "flags": {
            "print": "Print a route",
            "add": "Add a route",
            "delete": "Delete a route",
            "change": "Modify an existing route",
            "-f": "Clear routing tables",
            "-p": "Make route persistent",
            "/?": "Display help",
        },
    },
    "ftp": {
        "description": "File Transfer Protocol client",
        "flags": {
            "-v": "Suppress remote server responses",
            "-n": "No auto-login",
            "-i": "Turn off interactive prompting",
            "-s:file": "Run FTP commands from file",
            "-a": "Use any local interface for data connection",
            "/?": "Display help",
        },
    },

    # --- Disk Management ---
    "diskpart": {
        "description": "Disk partition manager",
        "flags": {
            "/s": "Run diskpart script file",
            "/?": "Display help",
        },
    },
    "format": {
        "description": "Format a disk",
        "flags": {
            "/fs:ntfs": "Format as NTFS",
            "/fs:fat32": "Format as FAT32",
            "/fs:exfat": "Format as exFAT",
            "/q": "Quick format",
            "/v:label": "Volume label",
            "/x": "Force volume to dismount first",
            "/?": "Display help",
        },
    },
    "chkdsk": {
        "description": "Check disk for errors",
        "flags": {
            "/f": "Fix errors on disk",
            "/r": "Locate bad sectors and recover readable data",
            "/x": "Force volume to dismount first",
            "/v": "Verbose mode",
            "/b": "Re-evaluate bad clusters (NTFS only)",
            "/?": "Display help",
        },
    },
    "defrag": {
        "description": "Defragment disk drives",
        "flags": {
            "/u": "Print progress",
            "/v": "Verbose output",
            "/o": "Perform proper optimization for each media type",
            "/?": "Display help",
        },
    },

    # --- Environment & Variables ---
    "set": {
        "description": "Display, set, or remove environment variables",
        "flags": {
            "/p": "Prompt user for value",
            "/a": "Arithmetic expression",
            "/?": "Display help",
        },
    },
    "setx": {
        "description": "Set environment variables permanently",
        "flags": {
            "/s": "Remote system",
            "/u": "User context",
            "/p": "Password",
            "/m": "Set variable in system-wide environment",
            "/k": "Set variable based on registry key",
            "/?": "Display help",
        },
    },
    "path": {
        "description": "Display or set search path for executables",
        "flags": {"/?": "Display help"},
    },

    # --- Text & Search ---
    "find": {
        "description": "Search for a text string in files",
        "flags": {
            "/v": "Display lines not containing the string",
            "/c": "Display only a count of matching lines",
            "/n": "Display line numbers",
            "/i": "Ignore case",
            "/?": "Display help",
        },
    },
    "findstr": {
        "description": "Search for strings in files using regex",
        "flags": {
            "/b": "Match at beginning of line",
            "/e": "Match at end of line",
            "/l": "Use literal search strings",
            "/r": "Use regular expressions",
            "/s": "Search subdirectories",
            "/i": "Case insensitive",
            "/x": "Print lines that match exactly",
            "/v": "Print lines that don't match",
            "/n": "Print line number before each match",
            "/m": "Print only filename if file contains match",
            "/c": "Print only count of matching lines per file",
            "/?": "Display help",
        },
    },
    "sort": {
        "description": "Sort input",
        "flags": {
            "/r": "Reverse sort order",
            "/+n": "Sort starting at column n",
            "/o": "Output file",
            "/?": "Display help",
        },
    },
    "fc": {
        "description": "Compare two files",
        "flags": {
            "/a": "Display only first and last lines for each difference",
            "/b": "Binary comparison",
            "/c": "Case insensitive",
            "/l": "Compare as ASCII text",
            "/n": "Display line numbers (ASCII comparison)",
            "/w": "Compress white space",
            "/?": "Display help",
        },
    },
    "comp": {
        "description": "Compare two files byte by byte",
        "flags": {
            "/d": "Display differences in decimal",
            "/a": "Display differences as characters",
            "/l": "Display line number of differences",
            "/n": "Compare only first n lines",
            "/c": "Case insensitive",
            "/?": "Display help",
        },
    },

    # --- User & Permissions ---
    "whoami": {
        "description": "Display current user info",
        "flags": {
            "/user": "Display user info",
            "/groups": "Display group membership",
            "/priv": "Display privileges",
            "/all": "Display all info",
            "/fo": "Output format",
            "/?": "Display help",
        },
    },
    "runas": {
        "description": "Run a program as another user",
        "flags": {
            "/user:": "User account to run as",
            "/savecred": "Use previously saved credentials",
            "/noprofile": "Don't load user profile",
            "/env": "Use current environment instead of user's",
            "/?": "Display help",
        },
    },
    "icacls": {
        "description": "Display or modify file/folder permissions (ACLs)",
        "flags": {
            "/grant": "Grant specified user access rights",
            "/deny": "Deny specified user access rights",
            "/remove": "Remove specified user's rights",
            "/reset": "Replace ACLs with inherited ACLs",
            "/t": "Perform on all matching files/dirs in subdirs",
            "/c": "Continue on file errors",
            "/l": "Perform on symbolic link itself",
            "/save": "Store ACLs to file",
            "/restore": "Restore ACLs from file",
            "/?": "Display help",
        },
    },
    "cacls": {
        "description": "Display or modify file ACLs (legacy)",
        "flags": {
            "/t": "Change ACLs in current and subdirectories",
            "/e": "Edit ACL instead of replacing",
            "/c": "Continue on access denied errors",
            "/g": "Grant specified user access rights",
            "/r": "Revoke specified user's access rights",
            "/p": "Replace specified user's access rights",
            "/d": "Deny specified user access",
            "/?": "Display help",
        },
    },
    "takeown": {
        "description": "Take ownership of a file",
        "flags": {
            "/f": "File pattern",
            "/r": "Recurse subdirectories",
            "/d": "Default answer for prompt (Y/N)",
            "/a": "Give ownership to Administrators group",
            "/?": "Display help",
        },
    },

    # --- Registry ---
    "reg": {
        "description": "Manage the Windows registry",
        "flags": {
            "query": "Query registry keys/values",
            "add": "Add registry keys/values",
            "delete": "Delete registry keys/values",
            "copy": "Copy registry keys",
            "save": "Save registry to file",
            "restore": "Restore registry from file",
            "load": "Load registry hive",
            "unload": "Unload registry hive",
            "compare": "Compare registry keys",
            "export": "Export registry to file",
            "import": "Import registry from file",
            "/?": "Display help",
        },
    },
    "regedit": {
        "description": "Open Registry Editor GUI",
        "flags": {},
    },

    # --- System Management ---
    "sfc": {
        "description": "System File Checker",
        "flags": {
            "/scannow": "Scan and repair all system files",
            "/verifyonly": "Scan without repairing",
            "/scanfile": "Scan a specific file",
            "/verifyfile": "Verify a specific file",
            "/offbootdir": "Specify offline boot directory",
            "/offwindir": "Specify offline Windows directory",
            "/?": "Display help",
        },
    },
    "dism": {
        "description": "Deployment Image Servicing and Management",
        "flags": {
            "/online": "Target the running operating system",
            "/image:": "Specify path to offline Windows image",
            "/cleanup-image": "Cleanup or recovery operations",
            "/scanhealth": "Scan image for corruption",
            "/checkhealth": "Check image health",
            "/restorehealth": "Repair image corruption",
            "/get-features": "List available features",
            "/enable-feature": "Enable a Windows feature",
            "/disable-feature": "Disable a Windows feature",
            "/?": "Display help",
        },
    },
    "shutdown": {
        "description": "Shutdown or restart the computer",
        "flags": {
            "/s": "Shutdown",
            "/r": "Restart",
            "/l": "Log off",
            "/h": "Hibernate",
            "/a": "Abort a shutdown",
            "/t": "Set timeout (seconds) before shutdown",
            "/f": "Force running applications to close",
            "/m": "Specify remote computer",
            "/c": "Comment for shutdown reason",
            "/?": "Display help",
        },
    },
    "bcdedit": {
        "description": "Boot Configuration Data editor",
        "flags": {
            "/enum": "List entries in boot configuration",
            "/set": "Set an entry option value",
            "/deletevalue": "Delete an entry option",
            "/create": "Create a new entry",
            "/delete": "Delete an entry",
            "/copy": "Copy an entry",
            "/export": "Export system store to file",
            "/import": "Restore from backup file",
            "/?": "Display help",
        },
    },
    "sc": {
        "description": "Service Control manager",
        "flags": {
            "query": "Query status of a service",
            "queryex": "Query extended info",
            "start": "Start a service",
            "stop": "Stop a service",
            "pause": "Send PAUSE control to a service",
            "continue": "Send CONTINUE control to a service",
            "config": "Modify service configuration",
            "create": "Create a service",
            "delete": "Delete a service",
            "description": "Set service description",
            "/?": "Display help",
        },
    },
    "wmic": {
        "description": "Windows Management Instrumentation CLI",
        "flags": {
            "os": "Operating system info",
            "cpu": "CPU info",
            "memorychip": "Memory info",
            "diskdrive": "Disk drive info",
            "process": "Process management",
            "service": "Service management",
            "startup": "Startup programs",
            "useraccount": "User accounts",
            "bios": "BIOS info",
            "nic": "Network adapter info",
            "/?": "Display help",
        },
    },
    "powercfg": {
        "description": "Configure power settings",
        "flags": {
            "/list": "List all power schemes",
            "/query": "Display contents of power scheme",
            "/change": "Modify a setting in current scheme",
            "/batteryreport": "Generate battery report",
            "/energy": "Analyze energy efficiency",
            "/sleepstudy": "Generate sleep study report",
            "/requests": "Enumerate power requests",
            "/requestsoverride": "Set request override for process",
            "/?": "Display help",
        },
    },

    # --- Scripting & Batch ---
    "echo": {
        "description": "Display a message or toggle echo on/off",
        "flags": {
            "on": "Turn command echoing on",
            "off": "Turn command echoing off",
            ".": "Display a blank line (echo.)",
        },
    },
    "cls": {
        "description": "Clear the screen",
        "flags": {},
    },
    "exit": {
        "description": "Exit the command prompt",
        "flags": {
            "/b": "Exit batch script (not cmd.exe itself)",
            "/?": "Display help",
        },
    },
    "pause": {
        "description": "Pause and wait for a key press",
        "flags": {},
    },
    "rem": {
        "description": "Add a comment/remark in a batch file",
        "flags": {},
    },
    "call": {
        "description": "Call a batch file from another",
        "flags": {"/?": "Display help"},
    },
    "goto": {
        "description": "Jump to a label in a batch file",
        "flags": {},
    },
    "if": {
        "description": "Conditional processing in batch",
        "flags": {
            "exist": "Check if file exists",
            "not": "Negate condition",
            "errorlevel": "Check error level",
            "defined": "Check if variable is defined",
            "/i": "Case insensitive comparison",
            "equ": "Equal",
            "neq": "Not equal",
            "lss": "Less than",
            "leq": "Less or equal",
            "gtr": "Greater than",
            "geq": "Greater or equal",
        },
    },
    "for": {
        "description": "Loop command for batch files",
        "flags": {
            "/d": "Match against directory names",
            "/r": "Walk directory tree rooted at path",
            "/l": "Iterating sequence (start, step, end)",
            "/f": "Parse file content or command output",
            "/?": "Display help",
        },
    },
    "choice": {
        "description": "Prompt user to select from a list of choices",
        "flags": {
            "/c": "List of choices (default YN)",
            "/n": "Hide choice list in prompt",
            "/cs": "Case sensitive choices",
            "/t": "Default choice with timeout",
            "/d": "Default choice after timeout",
            "/m": "Message to display",
            "/?": "Display help",
        },
    },
    "timeout": {
        "description": "Wait a specified number of seconds",
        "flags": {
            "/t": "Seconds to wait (-1 = wait indefinitely)",
            "/nobreak": "Ignore key presses",
            "/?": "Display help",
        },
    },
    "title": {
        "description": "Set the window title for the command prompt",
        "flags": {},
    },
    "color": {
        "description": "Set console text and background colors",
        "flags": {
            "0": "Black",
            "1": "Blue",
            "2": "Green",
            "3": "Aqua",
            "4": "Red",
            "5": "Purple",
            "6": "Yellow",
            "7": "White",
            "8": "Gray",
            "9": "Light Blue",
            "a": "Light Green",
            "b": "Light Aqua",
            "c": "Light Red",
            "d": "Light Purple",
            "e": "Light Yellow",
            "f": "Bright White",
        },
    },
    "prompt": {
        "description": "Change the command prompt display string",
        "flags": {
            "$p": "Current drive and path",
            "$g": "Greater-than sign (>)",
            "$d": "Current date",
            "$t": "Current time",
            "$n": "Current drive",
            "$l": "Less-than sign (<)",
            "$b": "Pipe (|)",
            "$_": "Newline",
            "$$": "Dollar sign",
            "$a": "Ampersand (&)",
            "$q": "Equal sign (=)",
        },
    },

    # --- File Attributes & Links ---
    "attrib": {
        "description": "Display or change file attributes",
        "flags": {
            "+r": "Set read-only",
            "-r": "Clear read-only",
            "+a": "Set archive",
            "-a": "Clear archive",
            "+s": "Set system",
            "-s": "Clear system",
            "+h": "Set hidden",
            "-h": "Clear hidden",
            "/s": "Process files in subdirectories",
            "/d": "Process folders as well",
            "/?": "Display help",
        },
    },
    "mklink": {
        "description": "Create symbolic or hard links",
        "flags": {
            "/d": "Create directory symbolic link",
            "/h": "Create hard link",
            "/j": "Create directory junction",
            "/?": "Display help",
        },
    },

    # --- Archive & Compression ---
    "compact": {
        "description": "Display or change NTFS compression",
        "flags": {
            "/c": "Compress files",
            "/u": "Uncompress files",
            "/s": "Do for specified directory and subdirectories",
            "/a": "Display files with hidden or system attributes",
            "/i": "Continue even after errors",
            "/f": "Force compression",
            "/q": "Report only essential info",
            "/?": "Display help",
        },
    },
    "expand": {
        "description": "Expand compressed files",
        "flags": {
            "/r": "Rename expanded files",
            "/d": "Display list of files in source",
            "/f:": "Specific files to expand",
            "/?": "Display help",
        },
    },
    "tar": {
        "description": "Archive and extract tar files",
        "flags": {
            "-cf": "Create archive",
            "-xf": "Extract archive",
            "-tf": "List archive contents",
            "-czf": "Create gzip compressed archive",
            "-xzf": "Extract gzip compressed archive",
            "-v": "Verbose output",
        },
    },

    # --- Misc Utilities ---
    "clip": {
        "description": "Copy output to Windows clipboard",
        "flags": {"/?": "Display help"},
    },
    "where": {
        "description": "Locate and display files matching a pattern",
        "flags": {
            "/r": "Recursively search from specified directory",
            "/q": "Quiet mode (return exit code only)",
            "/f": "Display filenames in double quotes",
            "/t": "Display file size and date/time",
            "/?": "Display help",
        },
    },
    "assoc": {
        "description": "Display or modify file extension associations",
        "flags": {"/?": "Display help"},
    },
    "ftype": {
        "description": "Display or modify file type open commands",
        "flags": {"/?": "Display help"},
    },
    "cipher": {
        "description": "Display or alter encryption of directories/files",
        "flags": {
            "/e": "Encrypt specified directories",
            "/d": "Decrypt specified directories",
            "/s": "Perform operation in subdirectories",
            "/w": "Remove data from unused disk space",
            "/?": "Display help",
        },
    },
    "certutil": {
        "description": "Certificate utility",
        "flags": {
            "-hashfile": "Generate hash of a file",
            "-encode": "Encode file to Base64",
            "-decode": "Decode Base64 file",
            "-urlcache": "URL cache operations",
            "-addstore": "Add certificate to store",
            "-delstore": "Delete certificate from store",
            "/?": "Display help",
        },
    },
    "schtasks": {
        "description": "Schedule tasks to run periodically",
        "flags": {
            "/create": "Create a new scheduled task",
            "/delete": "Delete a scheduled task",
            "/query": "Display scheduled tasks",
            "/change": "Change properties of a scheduled task",
            "/run": "Run scheduled task immediately",
            "/end": "Stop a running scheduled task",
            "/?": "Display help",
        },
    },
    "at": {
        "description": "Schedule commands (legacy, use schtasks)",
        "flags": {"/?": "Display help"},
    },
    "mode": {
        "description": "Configure system devices",
        "flags": {"/?": "Display help"},
    },
    "doskey": {
        "description": "Edit command line, recall commands, create macros",
        "flags": {
            "/history": "Display all commands stored in memory",
            "/reinstall": "Install a new copy of Doskey",
            "/listsize=": "Set size of history buffer",
            "/macros": "Display all Doskey macros",
            "/macrofile=": "Install macros from file",
            "/?": "Display help",
        },
    },
    "help": {
        "description": "Display help for Windows commands",
        "flags": {},
    },
    "cmd": {
        "description": "Start a new command interpreter",
        "flags": {
            "/c": "Execute command and terminate",
            "/k": "Execute command and remain",
            "/s": "Modify treatment of string after /c or /k",
            "/q": "Turn echo off",
            "/d": "Disable AutoRun commands",
            "/a": "Output internal unicode to ANSI",
            "/u": "Output internal unicode to Unicode",
            "/v:on": "Enable delayed variable expansion",
            "/v:off": "Disable delayed variable expansion",
            "/?": "Display help",
        },
    },
    "powershell": {
        "description": "Start Windows PowerShell",
        "flags": {
            "-Command": "Execute specified commands",
            "-File": "Execute specified script file",
            "-NoProfile": "Don't load PowerShell profile",
            "-ExecutionPolicy": "Set execution policy for session",
            "-NoExit": "Don't exit after running commands",
            "-WindowStyle": "Set window style (Hidden, etc.)",
            "/?": "Display help",
        },
    },
    "wt": {
        "description": "Open Windows Terminal",
        "flags": {},
    },
    "notepad": {
        "description": "Open Notepad text editor",
        "flags": {},
    },
    "calc": {
        "description": "Open Calculator",
        "flags": {},
    },
    "mspaint": {
        "description": "Open Microsoft Paint",
        "flags": {},
    },
    "explorer": {
        "description": "Open Windows Explorer",
        "flags": {
            "/e": "Open in Explore view",
            "/select,": "Open folder with file selected",
            "/root,": "Specify root object to browse",
        },
    },
    "control": {
        "description": "Open Control Panel",
        "flags": {},
    },
    "msconfig": {
        "description": "Open System Configuration utility",
        "flags": {},
    },
    "mmc": {
        "description": "Open Microsoft Management Console",
        "flags": {},
    },
    "eventvwr": {
        "description": "Open Event Viewer",
        "flags": {},
    },
    "devmgmt.msc": {
        "description": "Open Device Manager",
        "flags": {},
    },
    "diskmgmt.msc": {
        "description": "Open Disk Management",
        "flags": {},
    },
    "services.msc": {
        "description": "Open Services manager",
        "flags": {},
    },
    "gpedit.msc": {
        "description": "Open Group Policy Editor",
        "flags": {},
    },
    "resmon": {
        "description": "Open Resource Monitor",
        "flags": {},
    },
    "perfmon": {
        "description": "Open Performance Monitor",
        "flags": {},
    },
    "winver": {
        "description": "Display Windows version dialog",
        "flags": {},
    },
    "cleanmgr": {
        "description": "Open Disk Cleanup",
        "flags": {
            "/d": "Specify the drive letter",
            "/sageset:n": "Save cleanup settings",
            "/sagerun:n": "Run cleanup with saved settings",
        },
    },
    "dxdiag": {
        "description": "Open DirectX Diagnostic Tool",
        "flags": {},
    },

    # --- Miscellaneous ---
    "assoc": {
        "description": "Display or modify file extension associations",
        "flags": {"/?": "Display help"},
    },
    "subst": {
        "description": "Associate a path with a drive letter",
        "flags": {
            "/d": "Delete a substituted drive",
            "/?": "Display help",
        },
    },
    "pushd": {
        "description": "Save the current directory then change to a new one",
        "flags": {"/?": "Display help"},
    },
    "popd": {
        "description": "Restore saved directory from pushd",
        "flags": {"/?": "Display help"},
    },
    "verify": {
        "description": "Tell Windows whether to verify files after write",
        "flags": {
            "on": "Enable verify",
            "off": "Disable verify",
        },
    },
    "recover": {
        "description": "Recover readable information from a damaged disk",
        "flags": {"/?": "Display help"},
    },
    "replace": {
        "description": "Replace files",
        "flags": {
            "/a": "Add new files only",
            "/p": "Prompt before replacing",
            "/r": "Replace read-only files",
            "/s": "Search subdirectories",
            "/w": "Wait before beginning",
            "/u": "Replace only older files",
            "/?": "Display help",
        },
    },
    "wevtutil": {
        "description": "Windows Event Log utility",
        "flags": {
            "el": "List log names",
            "gl": "Get log configuration",
            "sl": "Set log configuration",
            "qe": "Query events",
            "cli": "Clear log",
            "epl": "Export log",
            "/?": "Display help",
        },
    },
    "gpupdate": {
        "description": "Refresh Group Policy settings",
        "flags": {
            "/force": "Reapply all settings",
            "/target:computer": "Refresh computer settings only",
            "/target:user": "Refresh user settings only",
            "/?": "Display help",
        },
    },
    "gpresult": {
        "description": "Display Group Policy information",
        "flags": {
            "/r": "Display summary",
            "/v": "Verbose",
            "/z": "Super verbose",
            "/s": "Remote system",
            "/u": "User context",
            "/p": "Password",
            "/?": "Display help",
        },
    },
    "clip": {
        "description": "Copy command output to clipboard",
        "flags": {"/?": "Display help"},
    },
    "curl": {
        "description": "Transfer data from or to a server",
        "flags": {
            "-o": "Write output to file",
            "-O": "Save with remote filename",
            "-L": "Follow redirects",
            "-I": "Fetch headers only",
            "-s": "Silent mode",
            "-v": "Verbose output",
            "-X": "Specify request method",
            "-H": "Add custom header",
            "-d": "Send POST data",
            "--help": "Display help",
        },
    },
    "ssh": {
        "description": "OpenSSH client",
        "flags": {
            "-p": "Port to connect to on remote host",
            "-i": "Identity file (private key)",
            "-l": "Login name on remote machine",
            "-v": "Verbose mode",
            "-X": "Enable X11 forwarding",
            "-L": "Local port forwarding",
            "-R": "Remote port forwarding",
        },
    },
    "scp": {
        "description": "Secure copy over SSH",
        "flags": {
            "-r": "Recursively copy directories",
            "-P": "Port to connect to",
            "-i": "Identity file",
            "-v": "Verbose mode",
        },
    },
}
