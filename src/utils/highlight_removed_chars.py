import difflib


def highlight_removed_chars(
    original, cleaned, color_start="\033[91m", color_end="\033[0m"
):
    """
    Vergleicht den Originaltext mit dem bereinigten Text und gibt den Originaltext zurück,
    wobei entfernte Zeichen farblich hervorgehoben werden.

    Parameter:
      original: Der ursprüngliche Text.
      cleaned: Der Text, in dem bestimmte Zeichen entfernt wurden.
      color_start: ANSI-Code zum Starten der Farbe (Standard: rot).
      color_end: ANSI-Code zum Zurücksetzen der Farbe.

    Rückgabe:
      Ein String, in dem die aus dem Original entfernten Zeichen (im Vergleich zu cleaned)
      farblich markiert sind.
    """
    diff = list(difflib.ndiff(original, cleaned))
    highlighted = ""
    for token in diff:
        if token.startswith("- "):
            # Zeichen wurde entfernt – markiere es farblich
            highlighted += f"{color_start}{token[2]}{color_end}"
        elif token.startswith("  "):
            # Zeichen wurde beibehalten
            highlighted += token[2]
        # Zeichen, die mit "+ " beginnen, werden im Original nicht angezeigt.
    return highlighted
