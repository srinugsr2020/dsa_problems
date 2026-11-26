"""Reverse a list of characters in place. Return None."""


def baseline(chars):
    """O(n) time, O(n) buffer: an oracle, not the strict space solution."""
    backwards = []
    for i in range(len(chars) - 1, -1, -1):
        backwards.append(chars[i])
    for i, char in enumerate(backwards):
        chars[i] = char


def pythonic(chars):
    """list.reverse uses O(n) time and O(1) space, like the explicit swaps."""
    chars.reverse()


def optimized(chars):
    """O(n) time, O(1) extra space: spell out the opposite-end swaps."""
    for left in range(len(chars) // 2):
        right = len(chars) - 1 - left
        chars[left], chars[right] = chars[right], chars[left]


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        for text, expected in (("x!y?", "?y!x"), (" 1a", "a1 "), ("z", "z"), ("", "")):
            chars = list(text)
            alias = chars
            assert solve(chars) is None
            assert alias == list(expected)
