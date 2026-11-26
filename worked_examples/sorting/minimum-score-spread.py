"""Choose exactly k scores with minimum spread; assume 1 <= k <= len(scores)."""

from __future__ import annotations

from itertools import combinations


def baseline(scores: list[int], k: int) -> int:
    return min(max(group) - min(group) for group in combinations(scores, k))


def python_windows(scores: list[int], k: int) -> int:
    ordered = sorted(scores)
    return min(high - low for low, high in zip(ordered, ordered[k - 1:]))


def optimized(scores: list[int], k: int) -> int:
    if k == 1:
        return 0
    ordered = sorted(scores)
    smallest = ordered[k - 1] - ordered[0]
    for end in range(k, len(ordered)):
        smallest = min(smallest, ordered[end] - ordered[end - k + 1])
    return smallest


if __name__ == "__main__":
    for minimum_spread in baseline, python_windows, optimized:
        scores = [8, 2, 5, 2]
        assert minimum_spread(scores, 2) == 0
        assert minimum_spread(scores, 3) == 3
        assert minimum_spread(scores, 4) == 6
        assert minimum_spread(scores, 1) == 0
        assert scores == [8, 2, 5, 2]
