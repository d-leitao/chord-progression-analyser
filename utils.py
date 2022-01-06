def letterToInt(letter_note: str) -> int:
    """Map note letter to integer notation (C-B -> 0-11)."""
    mapping = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4,
            'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9,
            'A#': 10, 'Bb': 10, 'B': 11}
    int_note = standardize(mapping[letter_note])
    return int_note


def intToLetter(int_note: int) -> str:
    """Map integer notation to note letter (0-11 -> C-B)."""
    mapping = {0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#',
            7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'}
    letter_note = standardize(mapping[int_note])
    return letter_note


def standardize(unstd_int_note: int) -> int:
    """Standardize values outside of integer notation range (0-11)."""
    int_note = unstd_int_note
    while int_note < 0:
        int_note += 12
    int_note = int_note % 12
    return int_note
