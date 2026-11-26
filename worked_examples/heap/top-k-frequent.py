"""Return k most frequent integers, breaking ties by first occurrence."""

from __future__ import annotations

from collections import Counter


def baseline(values: list[int], k: int) -> list[int]:
    distinct = dict.fromkeys(values)
    return sorted(distinct, key=values.count, reverse=True)[:k]


def python_counter(values: list[int], k: int) -> list[int]:
    return [value for value, _ in Counter(values).most_common(k)]


def optimized(values: list[int], k: int) -> list[int]:
    if k == 0:
        return []
    counts = Counter(values)
    buckets = [[] for _ in range(len(values) + 1)]
    for value, frequency in counts.items():
        buckets[frequency].append(value)

    answer = []
    for frequency in range(len(values), 0, -1):
        for value in buckets[frequency]:
            answer.append(value)
            if len(answer) == k:
                return answer
    return answer


if __name__ == "__main__":
    for top_k in baseline, python_counter, optimized:
        assert top_k([5, 2, 7, 2, 7, 7, 5], 2) == [7, 5]
        assert top_k([5, 2, 7, 2, 7, 7, 5], 3) == [7, 5, 2]
        assert top_k([-1, 0, -1], 0) == []
        assert top_k([], 0) == []
