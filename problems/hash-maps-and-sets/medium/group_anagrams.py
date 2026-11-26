"""Group Anagrams

Problem:
Group strings that can be rearranged into one another. Each group contains
strings with exactly the same characters and counts. Keep duplicates and empty
strings, treat uppercase and lowercase as different, and return groups in any
order.

Examples:
- ["eat", "tea", "tan", "ate"] can return [["eat", "tea", "ate"], ["tan"]].
- ["a", "A", "a", ""] can return [["a", "a"], ["A"], [""]]: case matters and
  duplicates are kept.

Approaches:
- Baseline: Search representative signatures.
- Python / standard library: Group by sorted tuples.
- Optimized: Hash count signatures.
"""

from collections import Counter, defaultdict


def baseline(words):
    groups = []
    for word in words:
        counts = Counter(word)
        for key, group in groups:
            if key == counts:
                group.append(word)
                break
        else:
            groups.append((counts, [word]))
    return [group for _, group in groups]


def pythonic(words):
    groups = defaultdict(list)
    for word in words:
        groups[tuple(sorted(word))].append(word)
    return list(groups.values())


def optimized(words):
    groups = defaultdict(list)
    for word in words:
        groups[frozenset(Counter(word).items())].append(word)
    return list(groups.values())


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        words = ["éa", "é", "aé", "", "éa", "", "Éa"]
        expected = [["éa", "aé", "éa"], ["é"], ["", ""], ["Éa"]]
        assert sorted(map(sorted, solve(words))) == sorted(map(sorted, expected))
        assert solve([]) == []
