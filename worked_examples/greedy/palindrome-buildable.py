"""Find the largest palindrome length obtainable by rearranging characters."""

from collections import Counter


def baseline(text: str) -> int:
    unmatched = []
    pairs = 0
    for char in text:
        if char in unmatched:
            unmatched.remove(char)
            pairs += 1
        else:
            unmatched.append(char)
    return 2 * pairs + bool(unmatched)


def python_counter(text: str) -> int:
    counts = Counter(text)
    unpaired = sum(count % 2 for count in counts.values())
    return len(text) - unpaired + bool(unpaired)


def optimized(text: str) -> int:
    odd = set()
    for char in text:
        if char in odd:
            odd.remove(char)
        else:
            odd.add(char)
    return len(text) - len(odd) + bool(odd)


if __name__ == "__main__":
    for max_length in baseline, python_counter, optimized:
        assert max_length("abbccd") == 5
        assert max_length("abcabc") == 6
        assert max_length("Xx") == 1
        assert max_length("") == 0
