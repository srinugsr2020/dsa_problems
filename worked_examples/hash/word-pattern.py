"""Match pattern characters bijectively to whitespace-separated words."""


def baseline(pattern, text):
    words = text.split()
    return len(pattern) == len(words) and all(
        (pattern[i] == pattern[j]) == (words[i] == words[j])
        for j in range(len(words)) for i in range(j)
    )


def pythonic(pattern, text):
    def signature(items):
        ids = {}
        return [ids.setdefault(item, len(ids)) for item in items]

    return signature(pattern) == signature(text.split())


def optimized(pattern, text):
    words = text.split()
    if len(pattern) != len(words):
        return False
    forward, reverse = {}, {}
    for c, word in zip(pattern, words):
        if forward.setdefault(c, word) != word:
            return False
        if reverse.setdefault(word, c) != c:
            return False
    return True


if __name__ == "__main__":
    for solve in (baseline, pythonic, optimized):
        assert solve("aba", "\tcat  dog\ncat ") and solve("", " \t")
        assert not solve("aa", "dog cat")
        assert not solve("ab", "cat cat") and not solve("aba", "cat dog")
