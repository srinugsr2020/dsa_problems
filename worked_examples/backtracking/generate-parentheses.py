"""Generate well-formed parentheses for n >= 0, in lexicographic order."""

from __future__ import annotations

from itertools import combinations
from typing import Iterable


def balanced(chars: Iterable[str]) -> bool:
    depth = 0
    for char in chars:
        depth += 1 if char == "(" else -1
        if depth < 0:
            return False
    return depth == 0


def baseline(n: int) -> list[str]:
    answer = []
    path = []

    def try_all() -> None:
        if len(path) == 2 * n:
            if balanced(path):
                answer.append("".join(path))
            return
        for choice in "()":
            path.append(choice)
            try_all()
            path.pop()

    try_all()
    return answer


def python_combinations(n: int) -> list[str]:
    answer = []
    for opens in combinations(range(2 * n), n):
        path = [")"] * (2 * n)
        for index in opens:
            path[index] = "("
        if balanced(path):
            answer.append("".join(path))
    return answer


def optimized(n: int) -> list[str]:
    answer = []
    path = []

    def build(opens: int, closes: int) -> None:
        if closes == n:
            answer.append("".join(path))
            return
        if opens < n:
            path.append("(")
            build(opens + 1, closes)
            path.pop()
        if closes < opens:
            path.append(")")
            build(opens, closes + 1)
            path.pop()

    build(0, 0)
    return answer


if __name__ == "__main__":
    for generate in baseline, python_combinations, optimized:
        assert generate(0) == [""]
        assert generate(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
        result = generate(4)
        assert len(result) == len(set(result)) == 14
        assert all(len(value) == 8 and balanced(value) for value in result)
