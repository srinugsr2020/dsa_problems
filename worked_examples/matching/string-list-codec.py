"""Frame strings as decimal character count, '#' and payload."""

from io import StringIO


def _read_frame(data, start, separator):
    header = data[start:separator]
    if (not header or not header.isascii() or not header.isdecimal()
            or (len(header) > 1 and header[0] == "0")
            or len(header) > len(str(len(data)))):
        raise ValueError("invalid length")
    stop = separator + 1 + int(header)
    if stop > len(data):
        raise ValueError("truncated payload")
    return data[separator + 1:stop], stop


def encode_baseline(words):
    result = ""
    for word in words:
        result += f"{len(word)}#{word}"
    return result


def decode_baseline(data):
    result = []
    start = 0
    while start < len(data):
        separator = start
        while separator < len(data) and data[separator] != "#":
            separator += 1
        if separator == len(data):
            raise ValueError("missing separator")
        word, start = _read_frame(data, start, separator)
        result.append(word)
    return result


def encode_pythonic(words):
    return "".join(f"{len(word)}#{word}" for word in words)


def decode_pythonic(data):
    result = []
    start = 0
    while start < len(data):
        separator = data.find("#", start)
        if separator == -1:
            raise ValueError("missing separator")
        word, start = _read_frame(data, start, separator)
        result.append(word)
    return result


def encode_optimized(words):
    writer = StringIO()
    for word in words:
        writer.write(f"{len(word)}#")
        writer.write(word)
    return writer.getvalue()


def decode_optimized(data):
    result = []
    pos = 0
    while pos < len(data):
        start = pos
        length = 0
        while pos < len(data) and "0" <= data[pos] <= "9":
            length = 10 * length + ord(data[pos]) - ord("0")
            if length > len(data):
                raise ValueError("impossible length")
            pos += 1
        if (pos == start or pos == len(data) or data[pos] != "#"
                or (pos - start > 1 and data[start] == "0")):
            raise ValueError("invalid header")
        pos += 1
        if pos + length > len(data):
            raise ValueError("truncated payload")
        result.append(data[pos:pos + length])
        pos += length
    return result


if __name__ == "__main__":
    encoders = (encode_baseline, encode_pythonic, encode_optimized)
    decoders = (decode_baseline, decode_pythonic, decode_optimized)
    for encode in encoders:
        for decode in decoders:
            words = ["", "#02", "🙂é\n", "a" * 11, ""]
            encoded = encode(iter(words))
            assert encoded == "0#3##023#🙂é\n11#" + "a" * 11 + "0#"
            assert decode(encoded) == words
            assert decode(encode([])) == [] and decode(encode([""])) == [""]
    for decode in decoders:
        for invalid in ("#", "3#xy", "1", "-1#", "01#a", "２#ab", "0#x"):
            try:
                decode(invalid)
            except ValueError:
                continue
            raise AssertionError(f"accepted malformed input {invalid!r}")
