"""Valid Parentheses

Problem:
Decide whether parentheses, square brackets and braces are correctly matched and
nested. Empty input is valid; reject non-bracket characters.

Examples:
- {[()()]}[] returns True.
- ([)] returns False because the pairs cross.

Approaches:
- Baseline: Look backward for each opener.
- Python / standard library: Reduce with a regex.
- Optimized: Track unmatched openers.
"""

import re


OPENERS = "([{"
CLOSERS = {")": "(", "]": "[", "}": "{"}
PAIR = re.compile(r"\(\)|\[\]|\{\}")


def valid_by_looking_back(text):
    depth = 0
    for i, char in enumerate(text):
        if char in OPENERS:
            depth += 1
        elif char in CLOSERS:
            if not depth:
                return False
            depth -= 1
            skipped = 0
            for j in range(i - 1, -1, -1):
                previous = text[j]
                if previous in CLOSERS:
                    skipped += 1
                elif skipped:
                    skipped -= 1
                else:
                    if previous != CLOSERS[char]:
                        return False
                    break
        else:
            return False
    return depth == 0


def valid_by_rewriting(text):
    while text:
        text, removed = PAIR.subn("", text)
        if not removed:
            return False
    return True


def valid_by_stack(text):
    opened = []
    for char in text:
        if char in OPENERS:
            opened.append(char)
        elif char not in CLOSERS or not opened or opened.pop() != CLOSERS[char]:
            return False
    return not opened


if __name__ == "__main__":
    for solve in (valid_by_looking_back, valid_by_rewriting, valid_by_stack):
        assert solve("")
        assert solve("{[()()]}[]")
        assert not solve("([)]")
        assert not solve("([]}")
        assert not solve(")()(")
        assert not solve("[[]")
        assert not solve("([a])")
        assert not solve("( )")
    assert valid_by_stack("(" * 4096 + ")" * 4096)
    assert not valid_by_stack("(" * 4096 + ")" * 4095 + "]")
