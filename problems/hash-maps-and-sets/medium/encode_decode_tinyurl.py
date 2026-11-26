"""Encode and Decode Short URLs

Problem:
Build an in-memory URL shortener with encode(url) and decode(alias). Encoding
the same nonempty URL twice gives the same alias, and different URLs get
different aliases. Decode only a complete alias issued by this instance; return
an empty string for anything else.

Examples:
- Encoding https://example.org/é twice returns the same alias; decoding it
  returns the original URL.
- A bare code, malformed alias, or alias unknown to this instance decodes to an
  empty string.

Approaches:
- Baseline: Search a list of URLs.
- Python / standard library: Two dictionaries and decimal IDs.
- Optimized: Dense indices encoded as base62.
"""

from string import ascii_letters, digits

PREFIX = "https://short.example/"
ALPHABET = digits + ascii_letters


class Baseline:
    def __init__(self):
        self.urls = []

    def encode(self, url):
        try:
            position = self.urls.index(url)
        except ValueError:
            position = len(self.urls)
            self.urls.append(url)
        return PREFIX + str(position)

    def decode(self, alias):
        if not self.urls or not alias.startswith(PREFIX):
            return ""
        length = len(alias) - len(PREFIX)
        if not 0 < length <= len(str(len(self.urls) - 1)):
            return ""
        code = alias[len(PREFIX):]
        if not code.isascii() or not code.isdecimal() or (length > 1 and code[0] == "0"):
            return ""
        position = int(code)
        return self.urls[position] if position < len(self.urls) else ""


class Pythonic:
    def __init__(self):
        self.forward = {}
        self.reverse = {}

    def encode(self, url):
        if url not in self.forward:
            alias = PREFIX + str(len(self.forward))
            self.forward[url] = alias
            self.reverse[alias] = url
        return self.forward[url]

    def decode(self, alias):
        return self.reverse.get(alias, "")


class Optimized:
    def __init__(self):
        self.positions = {}
        self.urls = []

    def encode(self, url):
        position = self.positions.get(url)
        if position is None:
            position = self.positions[url] = len(self.urls)
            self.urls.append(url)
        code = []
        while True:
            position, digit = divmod(position, len(ALPHABET))
            code.append(ALPHABET[digit])
            if position == 0:
                return PREFIX + "".join(reversed(code))

    def decode(self, alias):
        pos = len(PREFIX)
        if not alias.startswith(PREFIX) or pos == len(alias):
            return ""
        if alias[pos] == "0" and len(alias) - pos > 1:
            return ""
        value = 0
        for i in range(pos, len(alias)):
            digit = ALPHABET.find(alias[i])
            if digit == -1:
                return ""
            value = value * len(ALPHABET) + digit
            if value >= len(self.urls):
                return ""
        return self.urls[value]


if __name__ == "__main__":
    for Codec in (Baseline, Pythonic, Optimized):
        codec = Codec()
        urls = [f"https://example.org/é/{i}" for i in range(66)]
        aliases = [codec.encode(url) for url in urls]
        assert len(set(aliases)) == len(urls)
        assert [codec.decode(alias) for alias in aliases] == urls
        assert codec.encode(urls[0]) == aliases[0]
        assert codec.decode(aliases[0][len(PREFIX):]) == ""
        assert codec.decode(PREFIX + "00") == codec.decode(PREFIX + "%") == ""
        assert codec.decode(PREFIX + "9" * 5000) == ""
        assert Codec().decode(aliases[0]) == ""
