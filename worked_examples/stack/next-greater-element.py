"""Find the first strictly greater value for each query in a unique reference."""


def next_greater_scanning(queries, reference):
    results = []
    for query in queries:
        start = reference.index(query)
        answer = -1
        for i in range(start + 1, len(reference)):
            if reference[i] > query:
                answer = reference[i]
                break
        results.append(answer)
    return results


def next_greater_indexed(queries, reference):
    positions = {value: i for i, value in enumerate(reference)}

    def find(query):
        indices = range(positions[query] + 1, len(reference))
        return next((reference[i] for i in indices if reference[i] > query), -1)

    return [find(query) for query in queries]


def next_greater_stack(queries, reference):
    answers = dict.fromkeys(reference, -1)
    waiting = []
    for value in reference:
        while waiting and waiting[-1] < value:
            answers[waiting.pop()] = value
        waiting.append(value)
    return [answers[query] for query in queries]


if __name__ == "__main__":
    for solve in (next_greater_scanning, next_greater_indexed, next_greater_stack):
        reference = [2, 1, 3, 5, 4]
        assert solve([4, 2, 5, 1, 3], reference) == [-1, 3, -1, 3, 5]
        assert reference == [2, 1, 3, 5, 4]
        assert solve([6, 8, 7], [8, 7, 6, 9]) == [9, 9, 9]
        assert solve([2, 4], [4, 3, 2, 1]) == [-1, -1]
        assert solve([0], [0]) == [-1]
        assert solve([], []) == []
