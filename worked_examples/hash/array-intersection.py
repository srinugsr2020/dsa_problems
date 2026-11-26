"""Return each common integer once, in any order."""


def baseline(first, second):
    result = []
    for value in first:
        if value in second and value not in result:
            result.append(value)
    return result


def pythonic(first, second):
    return list(set(first) & set(second))


def optimized(first, second):
    if len(first) > len(second):
        first, second = second, first
    available = set(first)
    if not available:
        return []
    result = []
    for value in second:
        if value in available:
            result.append(value)
            available.remove(value)
            if not available:
                break
    return result


def sorted_inputs(first, second):
    """Same result contract, but inputs must already be sorted."""
    i = j = 0
    result = []
    while i < len(first) and j < len(second):
        a, b = first[i], second[j]
        if a < b:
            i += 1
        elif a > b:
            j += 1
        else:
            if not result or result[-1] != a:
                result.append(a)
            i += 1
            j += 1
    return result


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized, sorted_inputs):
        assert sorted(solve([-1, -1, 5, 5], [-1, 2, 5])) == [-1, 5]
        assert solve([], [2]) == solve([0, 3], [2]) == []
    assert sorted(optimized([9, 3, 3], [5, 3, 9, 9])) == [3, 9]
