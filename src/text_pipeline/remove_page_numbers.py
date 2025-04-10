import regex


def _find_best_consecutive_sequence(data, threshold_min_len_chain):
    """
    Diese Funktion erhält eine Liste von int-Listen.
    Ziel ist es, eine zusammenhängende Teilfolge zu finden,
    bei der aus jeder benachbarten Liste genau ein Element entnommen wird,
    und zwar so, dass jede Zahl exakt um 1 größer als die vorherige ist.
    Falls mehrere Teilfolgen gleicher Länge existieren, wird die
    lexikografisch kleinste gewählt (z. B. [0,1] wird [1,2] vorgezogen).

    Rückgabe:
        Ein Dictionary, in dem der Schlüssel den Index der verwendeten Liste
        und der Wert die aus dieser Liste gewählte Zahl darstellt.
    """
    best_chain = {}
    best_sequence = None  # Liste der ausgewählten Zahlen
    best_length = 0

    # Iteriere über alle möglichen Startpositionen
    for i in range(len(data)):
        # Betrachte jeden möglichen Kandidaten in der i-ten Liste (in sortierter Reihenfolge)
        for candidate in sorted(data[i]):
            chain = {i: candidate}
            seq = [candidate]
            current = candidate
            # Versuche, die Kette in den folgenden Listen fortzusetzen
            for j in range(i + 1, len(data)):
                next_required = current + 1
                if next_required in data[j]:
                    chain[j] = next_required
                    seq.append(next_required)
                    current = next_required
                else:
                    break

            # Aktualisiere das beste Ergebnis:
            # Zuerst wird die längste Kette bevorzugt,
            # bei gleicher Länge die lexikografisch kleinste Folge.
            if len(seq) > best_length:
                best_length = len(seq)
                best_chain = chain.copy()
                best_sequence = seq.copy()
            elif len(seq) == best_length and len(seq) > 0:
                # Wenn noch keine beste Sequenz gesetzt ist, oder
                # diese Sequenz lexikografisch kleiner ist, aktualisiere.
                if best_sequence is None or seq < best_sequence:
                    best_chain = chain.copy()
                    best_sequence = seq.copy()

    return (
        best_chain if (len(best_chain) >= threshold_min_len_chain * len(data)) else {}
    )


def _extract_numbers_only_int(text):
    return list(
        map(
            int,
            regex.findall(r"(?<![\d\[\(\-\+]|\d[\.\,])\d+(?![\d\]\)]|[\.\,]\d)", text),
        )
    )


def _get_numbers_from_n_strings(data, threshold_n_strings):
    header_numbers = []
    footer_numbers = []
    for page in data:
        header_string = " ".join(page[:threshold_n_strings])
        footer_string = " ".join(page[-threshold_n_strings:])

        header_number = _extract_numbers_only_int(header_string)
        footer_number = _extract_numbers_only_int(footer_string)

        header_numbers.append(header_number)
        footer_numbers.append(footer_number)

    return header_numbers, footer_numbers


def _remove_number(text, number):
    number_str = str(number)

    # Allgemeines Muster: alleinstehend, in Wort eingebettet, aber nicht in [ ] oder mit Nachkomma
    working_text, count = regex.subn(
        rf"(?<![\d\[\(\-\+]|\d[\.\,]){number_str}(?![\d\]\)]|[\.\,]\d)",
        "",
        text,
        count=1,
    )

    # Aufräumen
    if count:
        return working_text, True
    return text, False


def _remove_number_rev(text, number):
    number_str = str(number)

    # Rückwärts verarbeiten?
    text_rev = text[::-1]
    num_rev = number_str[::-1]

    # Allgemeines Muster: alleinstehend, in Wort eingebettet, aber nicht in [ ] oder mit Nachkomma
    working_text, count = regex.subn(
        rf"(?<![\d\]\)]|\d[\,\.]){num_rev}(?![\d\[\(\-\+]|[\.\,]\d)",
        "",
        text_rev,
        count=1,
    )

    # Aufräumen
    if count:
        cleaned = working_text[::-1]
        return cleaned, True
    return text, False


def remove_page_numbers(data, threshold_n_strings=2, threshold_min_len_chain=0.6):
    if len(data) < 2:
        return data
    header_numbers, footer_numbers = _get_numbers_from_n_strings(
        data, threshold_n_strings
    )

    header_consecutive_sequence = _find_best_consecutive_sequence(
        header_numbers, threshold_min_len_chain
    )

    footer_consecutive_sequence = _find_best_consecutive_sequence(
        footer_numbers, threshold_min_len_chain
    )

    for i in range(0, len(data)):
        if i in header_consecutive_sequence:
            for j, _ in enumerate(data[i][:threshold_n_strings]):
                data[i][j], success = _remove_number(
                    data[i][j], header_consecutive_sequence[i]
                )
                if success:
                    break
        if i in footer_consecutive_sequence:
            for j, _ in enumerate(reversed(data[i][-threshold_n_strings:])):
                data[i][-j - 1], success = _remove_number_rev(
                    data[i][-j - 1], footer_consecutive_sequence[i]
                )
                if success:
                    break

    return data
