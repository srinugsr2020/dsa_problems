"""Medium (Prefix / Encoding): Encode and Decode a List of Strings

Problem:
Design two functions:
    encode(words)  -> single string
    decode(s)      -> original list of strings

The encoding must be lossless — `decode(encode(words)) == words` for any list
of strings, including strings that contain spaces, newlines, or any delimiter.

This is a classic distributed-systems interview question because it mirrors
how data is serialized when passing a list of field values through a single
channel (e.g., Kafka message body, S3 object name, URL query string).

Example:
    words = ["lint", "co|de", "love", "you"]
    encode(words) -> some opaque string
    decode(encode(words)) == ["lint", "co|de", "love", "you"]

Pattern:
- Length-prefix encoding: store `len(word)#` before each word.
  This makes the delimiter unambiguous regardless of the word's content.

Why NOT a simple delimiter (e.g., '|' or '\n')?
- If any word contains the delimiter, splitting on it will corrupt the output.

Data Engineering angle:
- Exactly how Parquet / Arrow / Protocol Buffers encode variable-length string
  columns: length-prefix so readers know how many bytes to consume per field.
- Also used in Redis RESP protocol and in row-based binary formats.
"""

from __future__ import annotations

from typing import List


# ---------------------------------------------------------------------------
# Length-prefix codec
# ---------------------------------------------------------------------------

def encode(words: List[str]) -> str:
    """Encode a list of strings into a single string using length-prefix format.

    Format per word: "<length>#<word_bytes>"
    '#' is the separator between the length integer and the word body.
    It is safe because we always read exactly `length` bytes after '#'.

    Time:  O(total characters)
    Space: O(total characters)
    """

    parts: List[str] = []
    for word in words:
        # Prefix the word with its byte length so the decoder knows how far to read.
        parts.append(f"{len(word)}#{word}")
    return "".join(parts)


def decode(s: str) -> List[str]:
    """Decode a length-prefix-encoded string back into the original list.

    Time:  O(total characters)
    Space: O(total characters)
    """

    words: List[str] = []
    i = 0

    while i < len(s):
        # Find the '#' separator to extract the length.
        j = i
        while s[j] != "#":
            j += 1

        length = int(s[i:j])   # Number of characters in the next word

        # Slice exactly `length` characters after the '#'.
        word = s[j + 1 : j + 1 + length]
        words.append(word)

        # Advance past the length prefix, '#', and the word body.
        i = j + 1 + length

    return words


def _run_tests() -> None:
    def roundtrip(words: List[str]) -> None:
        """Assert that encode -> decode is lossless."""
        assert decode(encode(words)) == words, (
            f"Roundtrip failed for: {words!r}"
        )

    roundtrip([])                                   # Empty list
    roundtrip([""])                                 # Single empty string
    roundtrip(["", ""])                             # Multiple empty strings
    roundtrip(["hello", "world"])                   # Basic case
    roundtrip(["lint", "co|de", "love", "you"])    # Contains pipe (non-safe delimiter)
    roundtrip(["a#b", "c#d"])                       # Contains '#' inside words
    roundtrip(["line1\nline2", "tab\there"])        # Newlines and tabs
    roundtrip(["one"])                              # Single word
    roundtrip(["12#abc", "5#xyz"])                  # Word looks like a length prefix

    # Verify the encoded format uses length prefixes
    encoded = encode(["ab", "cde"])
    assert encoded == "2#ab3#cde", f"Unexpected format: {encoded!r}"


if __name__ == "__main__":
    _run_tests()
    print("OK - medium_encode_decode_strings")
