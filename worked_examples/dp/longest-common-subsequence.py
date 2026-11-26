"""Return the longest shared subsequence length, without requiring adjacency."""

from itertools import combinations


def baseline(first: str, second: str) -> int:
    short, long = sorted((first, second), key=len)
    for length in range(len(short), 0, -1):
        for candidate in combinations(short, length):
            remaining = iter(long)
            if all(char in remaining for char in candidate):
                return length
    return 0


def python_table(first: str, second: str) -> int:
    table = [[0] * (len(second) + 1) for _ in range(len(first) + 1)]
    for i, char in enumerate(first, 1):
        for j, other in enumerate(second, 1):
            if char == other:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[-1][-1]


def optimized(first: str, second: str) -> int:
    short, long = sorted((first, second), key=len)
    if not short:
        return 0
    row = [0] * (len(short) + 1)
    for char in long:
        northwest = 0
        for col, other in enumerate(short, 1):
            north = row[col]
            row[col] = northwest + 1 if char == other else max(north, row[col - 1])
            northwest = north
    return row[-1]


if __name__ == "__main__":
    for lcs in baseline, python_table, optimized:
        assert lcs("axbycx", "abc") == lcs("abc", "axbycx") == 3
        assert lcs("acb", "abc") == 2
        assert lcs("aaaa", "aa") == 2
        assert lcs("xyz", "abc") == 0
        assert lcs("abc", "") == 0
