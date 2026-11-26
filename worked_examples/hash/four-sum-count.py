"""Count index quadruples taking one entry from each input."""

from collections import Counter
from itertools import product


def baseline(a, b, c, d):
    if not (a and b and c and d):
        return 0
    return sum(x + y + z + w == 0 for x in a for y in b for z in c for w in d)


def pythonic(a, b, c, d):
    if not (a and b and c and d):
        return 0
    sums = Counter(x + y for x, y in product(a, b))
    return sum(sums[-(z + w)] for z, w in product(c, d))


def optimized(a, b, c, d):
    if not (a and b and c and d):
        return 0
    left, right = (Counter(a), Counter(b)), (Counter(c), Counter(d))
    if len(left[0]) * len(left[1]) > len(right[0]) * len(right[1]):
        left, right = right, left
    sums = Counter()
    for (x, count_x), (y, count_y) in product(left[0].items(), left[1].items()):
        sums[x + y] += count_x * count_y
    return sum(sums[-(z + w)] * count_z * count_w
               for (z, count_z), (w, count_w) in product(right[0].items(), right[1].items()))


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve([1, 1, 1], [-1, -1], [0, 0], [0]) == 12
        assert solve([-2, 3], [-1, 2], [0, 1], [0]) == 1
        assert solve([0], [], [0], [0]) == 0
