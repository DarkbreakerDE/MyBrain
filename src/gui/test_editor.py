import os
import subprocess
import tempfile
import re

import difflib

# ANSI-Farben
RED = "\x1b[31m"
GREEN = "\x1b[32m"
RESET = "\x1b[0m"


def edit_text_external(initial_text: str) -> str:

    with tempfile.NamedTemporaryFile(suffix=".txt", mode="w+", delete=False) as tmp:
        tmp.write(initial_text)
        tmp.flush()
        tmp_path = tmp.name

    # Editor öffnen

    subprocess.call(["konsole", "--noclose", "-e", f"nvim {tmp_path}"])

    # Nach Bearbeitung einlesen
    with open(tmp_path, "r") as tmp:
        edited_text = tmp.read()

    os.unlink(tmp_path)  # Temp-Datei löschen
    return edited_text


def strip_ansi_colors(text: str) -> str:
    ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", text)


def remove_red_ansi_blocks(text: str) -> str:
    # Entferne alles, was in ROT markiert ist (und die Markierung selbst)
    red_block = re.compile(rf"{re.escape(RED)}(.*?){re.escape(RESET)}", re.DOTALL)
    text = red_block.sub("", text)

    # Optionale: alle anderen ANSI-Reste entfernen
    ansi_clean = re.compile(r"\x1b\[[0-9;]*m")
    return ansi_clean.sub("", text)


def inline_colored_diff(old: str, new: str) -> str:
    result = []
    matcher = difflib.SequenceMatcher(None, old, new)

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            result.append(old[i1:i2])
        elif tag == "delete":
            result.append(f"{RED}{old[i1:i2]}{RESET}")
        elif tag == "insert":
            result.append(f"{GREEN}{new[j1:j2]}{RESET}")
        elif tag == "replace":
            result.append(f"{RED}{old[i1:i2]}{RESET}")
            result.append(f"{GREEN}{new[j1:j2]}{RESET}")
    return "".join(result)
