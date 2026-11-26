"""Sort Colors

Problem:
Sort a mutable list containing only 0, 1, and 2. Modify the original list and
return None.

Examples:
- [2, 0, 2, 1, 0] becomes [0, 0, 1, 2, 2] in the same list.
- [1, 1, 1] stays unchanged.

Approaches:
- Baseline: Selection sort.
- Python / standard library: Use list.sort.
- Optimized: Dutch national flag.
"""

from __future__ import annotations

from itertools import product


def baseline(colors: list[int]) -> None:
    for left in range(len(colors)):
        smallest = left
        for right in range(left + 1, len(colors)):
            if colors[right] < colors[smallest]:
                smallest = right
        colors[left], colors[smallest] = colors[smallest], colors[left]


def python_sort(colors: list[int]) -> None:
    colors.sort()


def optimized(colors: list[int]) -> None:
    low, current, high = 0, 0, len(colors) - 1
    while current <= high:
        if colors[current] == 0:
            colors[low], colors[current] = colors[current], colors[low]
            low += 1
            current += 1
        elif colors[current] == 2:
            colors[high], colors[current] = colors[current], colors[high]
            high -= 1
        else:
            current += 1


if __name__ == "__main__":
    for size in range(6):
        for values in product(range(3), repeat=size):
            for sort in baseline, python_sort, optimized:
                colors = list(values)
                assert sort(colors) is None
                assert colors == sorted(values)
