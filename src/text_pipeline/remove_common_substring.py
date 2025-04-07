import math
import re
from language_data.english_filler_words import ENGLISH_FILLER_WORDS
from language_data.german_filler_words import GERMAN_FILLER_WORDS
from utils.pritty_print_list import pretty_print_list


def find_full_words(candidate_words, text):
    """
    Sucht in `text` nach Wörtern aus `candidate_words`, die als ganze Wörter vorkommen.
    Dabei wird berücksichtigt, dass Wörter in einem Satz stehen und nicht nur durch Leerzeichen getrennt sein müssen.

    Parameter:
      candidate_words: Eine Liste von Wörtern, die gesucht werden sollen.
      text: Der Text (String), in dem gesucht wird.

    Rückgabe:
      Ein Set der Wörter, die als vollständige Wörter im Text vorkommen.
    """
    # Erstelle ein Regex-Muster, das jedes Kandidatenwort als ganzes Wort (mit Wortgrenzen) sucht.
    pattern = r"\b(?:" + "|".join(re.escape(word) for word in candidate_words) + r")\b"
    # Suche unter Beachtung von Groß-/Kleinschreibung (optional mit IGNORECASE)
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    return set(matches)


def check_for_filler_words(text, threshold=0.4):
    total_list = GERMAN_FILLER_WORDS.union(ENGLISH_FILLER_WORDS)
    result = find_full_words(total_list, text)

    total_sum = sum(map(len, result))

    if total_sum <= len(text) * threshold:
        return True
    return False


def _count_digits_regex(text):
    # \d sucht nach Ziffern (0-9)
    digits = re.findall(r"\d", text)
    return len(digits)


def longest_common_substring_threshold(
    strings,
    threshold_percentage_pages,
    threshold_min_len_substring,
    threshold_min_digits,
):
    """
    Findet den längsten gemeinsamen Teilsatz (Substring), der in mindestens
    threshold (Standard: 0.6 = 60%) aller Strings der Liste vorkommt.

    Parameter:
      strings: Liste von Strings.
      threshold: Anteil der Strings, in denen der Teilsatz vorkommen muss.

    Rückgabe:
      Der längste Teilsatz, der die Bedingung erfüllt. Falls kein solcher
      Teilsatz existiert, wird ein leerer String zurückgegeben.
    """
    if not strings:
        return ""

    total = len(strings)
    required_count = math.ceil(total * threshold_percentage_pages)

    # Wähle den kürzesten String, um die Anzahl der Kandidaten zu minimieren.
    shortest = min(strings, key=len)
    n = len(shortest)

    # Durchsuche die möglichen Substrings in absteigender Länge.
    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            candidate = shortest[start : start + length]
            # Zähle, in wie vielen Strings candidate vorkommt.
            count = sum(1 for s in strings if candidate in s)
            if (
                count >= required_count
                and check_for_filler_words(candidate)
                and (
                    len(candidate) >= threshold_min_len_substring
                    or _count_digits_regex(candidate) > threshold_min_digits
                )
            ):
                return candidate  # Da wir von längster Länge starten, ist dies das längste.
    return None


def _get_n_strings(data, threshold_n_strings=2):
    header_strings = []
    footer_strings = []
    for page in data:
        header_strings.append(" ".join(page[:threshold_n_strings]))
        footer_strings.append(" ".join(page[-threshold_n_strings:]))
    # print("Header")
    # pretty_print_list(header_strings)
    # print("footer")
    # pretty_print_list(footer_strings)
    return header_strings, footer_strings


def remove_common_substring(
    data,
    threshold_n_strings=2,
    threshold_percentage_pages=0.6,
    threshold_min_len_substring=10,
    threshold_min_digits=10,
):

    while True:
        header_strings, footer_strings = _get_n_strings(data, threshold_n_strings)
        header_substring = longest_common_substring_threshold(
            header_strings,
            threshold_percentage_pages,
            threshold_min_len_substring,
            threshold_min_digits,
        )
        footer_substring = longest_common_substring_threshold(
            footer_strings,
            threshold_percentage_pages,
            threshold_min_len_substring,
            threshold_min_digits,
        )

        if header_substring:
            print("Header", header_substring)
            for i in range(0, len(data)):
                for j, _ in enumerate(data[i][:threshold_n_strings]):
                    data[i][j] = data[i][j].replace(header_substring, "")
        if footer_substring:
            print("Footer", footer_substring)
            for i in range(0, len(data)):
                for j, _ in enumerate(reversed(data[i][-threshold_n_strings:])):
                    data[i][-j - 1] = data[i][-j - 1].replace(footer_substring, "")
        if not (header_substring or footer_substring):
            break

    return data
