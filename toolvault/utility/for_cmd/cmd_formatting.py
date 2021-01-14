"""
script to make sure, that keywords in Batch(cmd) files are in all upper case.

takes the path to an Batch file as input(sys.argv[1]) or to an folder containing batch files.
"""

# region [Imports]

# * Standard Library Imports ------------------------------------------------------------------------------------------------------------------------------------>

import os
import sys


# endregion[Imports]

# region [TODO]


# endregion [TODO]

# region [AppUserData]


# endregion [AppUserData]

# region [Logging]


# endregion[Logging]

# region [Constants]

THIS_FILE_DIR = os.path.abspath(os.path.dirname(__file__))

KEYWORDS = ["ASSOC",
            "ATTRIB",
            "BREAK",
            "BCDEDIT",
            "CACLS",
            "CALL",
            "CD",
            "CHCP",
            "CHDIR",
            "CHKDSK",
            "CHKNTFS",
            "CLS",
            "CMD",
            "COLOR",
            "COMP",
            "COMPACT",
            "CONVERT",
            "COPY",
            "DATE",
            "DEL",
            "DIR",
            "DISKPART",
            "DOSKEY",
            "DRIVERQUERY",
            "ECHO",
            "ENDLOCAL",
            "ERASE",
            "EXIT",
            "FC",
            "FIND",
            "FINDSTR",
            "FOR",
            "FORMAT",
            "FSUTIL",
            "FTYPE",
            "GOTO",
            "GPRESULT",
            "GRAFTABL",
            "HELP",
            "ICACLS",
            "IF",
            "LABEL",
            "MD",
            "MKDIR",
            "MKLINK",
            "MODE",
            "MORE",
            "MOVE",
            "OPENFILES",
            "PATH",
            "PAUSE",
            "POPD",
            "PRINT",
            "PROMPT",
            "PUSHD",
            "RD",
            "RECOVER",
            "REM",
            "REN",
            "RENAME",
            "REPLACE",
            "RMDIR",
            "ROBOCOPY",
            "SET",
            "SETLOCAL",
            "SC",
            "SCHTASKS",
            "SHIFT",
            "SHUTDOWN",
            "SORT",
            "START",
            "SUBST",
            "SYSTEMINFO",
            "TASKLIST",
            "TASKKILL",
            "TIME",
            "TITLE",
            "TREE",
            "TYPE",
            "VER",
            "VERIFY",
            "VOL",
            "XCOPY",
            "WMIC",
            "@ECHO",
            "echo.",
            'off']


# endregion[Constants]

def format_cmd_file(in_file):
    with open(in_file, 'r') as f_in:
        old_content = f_in.read()
    _new_content = []
    for line in old_content.splitlines():
        _new_line = []
        for word in line.split():
            if any(word.casefold() == keyword.casefold() for keyword in KEYWORDS):
                word = word.upper()
            _new_line.append(word)
        _new_content.append(' '.join(_new_line))
    with open(in_file, 'w') as f_out:
        f_out.write('\n'.join(_new_content))
    print('#' * 10 + ' done ' + '#' * 10)


def apply_to_all_in_folder(in_folder):
    for file in os.scandir(in_folder):
        if file.is_file() is True and (file.name.endswith('.cmd') or file.name.endswith('.bat')):
            format_cmd_file(file.path)

# region[Main_Exec]


if __name__ == '__main__':
    file_to_apply = sys.argv[1]

    if os.path.exists(file_to_apply) is False:
        raise FileNotFoundError(f"{file_to_apply} is not an existing file")

    if os.path.isdir(file_to_apply):
        apply_to_all_in_folder(file_to_apply)
    else:
        format_cmd_file(file_to_apply)

# endregion[Main_Exec]
