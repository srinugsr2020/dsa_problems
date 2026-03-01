"""
=============================================================================
PYTHON STRINGS - COMPREHENSIVE GUIDE
=============================================================================

Strings are immutable sequences of Unicode characters. They are one of the
most commonly used data types in Python for text manipulation.

Key Characteristics:
- Immutable: Cannot be modified after creation
- Ordered: Characters maintain their sequence order
- Indexed: Characters accessible via zero-based indices
- Hashable: Can be used as dictionary keys
- Unicode: Full Unicode support (emojis, international characters)
=============================================================================
"""

# =============================================================================
# SECTION 1: CREATING STRINGS
# =============================================================================

print("=" * 60)
print("SECTION 1: CREATING STRINGS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Method 1: Single and double quotes (equivalent)
# -----------------------------------------------------------------------------
single = 'Hello, World!'
double = "Hello, World!"
print("\n1.1 Single and double quotes:")
print(f"    'Hello, World!' = {single}")
print(f'    "Hello, World!" = {double}')

# -----------------------------------------------------------------------------
# Method 2: Quotes inside strings
# Use alternating quote types or escape characters
# -----------------------------------------------------------------------------
print("\n1.2 Quotes inside strings:")
#print(f"    \"It's Python!\" = {'It' + \"'s Python!\"}")
#print(f"    'He said \"Hi\"' = {'He said \"Hi\"'}")
#print(f"    Escaped: 'It\\'s Python!' = {'It\\'s Python!'}")

# -----------------------------------------------------------------------------
# Method 3: Triple quotes (multi-line strings)
# Preserves newlines and formatting
# -----------------------------------------------------------------------------
multiline = """This is a
multi-line string
that spans several lines."""
print("\n1.3 Triple quotes (multi-line):")
print(f"    {multiline}")

# -----------------------------------------------------------------------------
# Method 4: Raw strings (r-prefix)
# Backslashes are treated literally
# -----------------------------------------------------------------------------
normal = "C:\\Users\\name\\file.txt"
raw = r"C:\Users\name\file.txt"
print("\n1.4 Raw strings (r-prefix):")
print(f"    Normal: {normal}")
print(f"    Raw: {raw}")

# -----------------------------------------------------------------------------
# Method 5: String from other types
# -----------------------------------------------------------------------------
from_int = str(42)
from_float = str(3.14)
from_list = str([1, 2, 3])
print("\n1.5 str() constructor:")
print(f"    str(42) = '{from_int}'")
print(f"    str(3.14) = '{from_float}'")
print(f"    str([1,2,3]) = '{from_list}'")

# -----------------------------------------------------------------------------
# Method 6: Unicode and special characters
# -----------------------------------------------------------------------------
unicode_str = "Hello, 世界! 🎉"
print("\n1.6 Unicode support:")
print(f"    Unicode: {unicode_str}")
print(f"    \\u0041 = {'\\u0041'} -> A")


# =============================================================================
# SECTION 2: STRING INDEXING AND SLICING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: STRING INDEXING AND SLICING")
print("=" * 60)

text = "Hello, Python!"
print(f"\n    text = '{text}'")
print(f"    Indices: 0-{len(text)-1}")

# -----------------------------------------------------------------------------
# Positive indexing (left to right, 0-based)
# -----------------------------------------------------------------------------
print("\n2.1 Positive indexing:")
print(f"    text[0] = '{text[0]}'")
print(f"    text[7] = '{text[7]}'")

# -----------------------------------------------------------------------------
# Negative indexing (right to left, -1 is last)
# -----------------------------------------------------------------------------
print("\n2.2 Negative indexing:")
print(f"    text[-1] = '{text[-1]}'")
print(f"    text[-7] = '{text[-7]}'")

# -----------------------------------------------------------------------------
# Slicing: string[start:stop:step]
# Returns a NEW string (strings are immutable)
# -----------------------------------------------------------------------------
print("\n2.3 Slicing [start:stop:step]:")
print(f"    text[0:5] = '{text[0:5]}'")     # 'Hello'
print(f"    text[7:] = '{text[7:]}'")       # 'Python!'
print(f"    text[:5] = '{text[:5]}'")       # 'Hello'
print(f"    text[::2] = '{text[::2]}'")     # Every 2nd char
print(f"    text[::-1] = '{text[::-1]}'")   # Reversed

# -----------------------------------------------------------------------------
# Slice object (for reusable slices)
# -----------------------------------------------------------------------------
print("\n2.4 Slice object:")
hello_slice = slice(0, 5)
print(f"    slice(0, 5) -> text[slice] = '{text[hello_slice]}'")


# =============================================================================
# SECTION 3: STRING IMMUTABILITY
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: STRING IMMUTABILITY")
print("=" * 60)

# -----------------------------------------------------------------------------
# Strings cannot be modified in place
# -----------------------------------------------------------------------------
s = "hello"
print("\n3.1 Strings are immutable:")
print(f"    s = '{s}'")
print("    s[0] = 'H'  # TypeError: strings are immutable")

# -----------------------------------------------------------------------------
# Create new strings instead
# -----------------------------------------------------------------------------
new_s = 'H' + s[1:]
print("\n3.2 Create new string instead:")
print(f"    'H' + s[1:] = '{new_s}'")

# Strings are reused when possible (interning)
print("\n3.3 String interning:")
a = "hello"
b = "hello"
print(f"    a = 'hello', b = 'hello'")
print(f"    a is b = {a is b}")  # Often True for simple strings


# =============================================================================
# SECTION 4: STRING METHODS - CASE CONVERSION
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: STRING METHODS - CASE CONVERSION")
print("=" * 60)

sample = "Hello, World! Python 3.x"
print(f"\n    sample = '{sample}'")

# -----------------------------------------------------------------------------
# Case conversion methods (return NEW strings)
# -----------------------------------------------------------------------------
print("\n4.1 Case conversion methods:")
print(f"    lower()      = '{sample.lower()}'")
print(f"    upper()      = '{sample.upper()}'")
print(f"    capitalize() = '{sample.capitalize()}'")
print(f"    title()      = '{sample.title()}'")
print(f"    swapcase()   = '{sample.swapcase()}'")
print(f"    casefold()   = '{sample.casefold()}'")  # Aggressive lowercase


# =============================================================================
# SECTION 5: STRING METHODS - SEARCHING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: STRING METHODS - SEARCHING")
print("=" * 60)

text = "Hello, World! Hello, Python!"
print(f"\n    text = '{text}'")

# -----------------------------------------------------------------------------
# find() and rfind() - Return index or -1 if not found
# -----------------------------------------------------------------------------
print("\n5.1 find() and rfind():")
print(f"    text.find('Hello') = {text.find('Hello')}")
print(f"    text.rfind('Hello') = {text.rfind('Hello')}")  # From right
print(f"    text.find('Java') = {text.find('Java')}")  # Not found

# -----------------------------------------------------------------------------
# index() and rindex() - Like find but raises ValueError if not found
# -----------------------------------------------------------------------------
print("\n5.2 index() and rindex():")
print(f"    text.index('World') = {text.index('World')}")
# text.index('Java')  # ValueError

# -----------------------------------------------------------------------------
# count() - Count occurrences
# -----------------------------------------------------------------------------
print("\n5.3 count():")
print(f"    text.count('Hello') = {text.count('Hello')}")
print(f"    text.count('o') = {text.count('o')}")

# -----------------------------------------------------------------------------
# Membership testing (in / not in)
# -----------------------------------------------------------------------------
print("\n5.4 Membership testing:")
print(f"    'Python' in text = {'Python' in text}")
print(f"    'Java' in text = {'Java' in text}")

# -----------------------------------------------------------------------------
# startswith() and endswith()
# -----------------------------------------------------------------------------
print("\n5.5 startswith() and endswith():")
print(f"    text.startswith('Hello') = {text.startswith('Hello')}")
print(f"    text.endswith('!') = {text.endswith('!')}")
print(f"    text.startswith(('Hi', 'Hello')) = {text.startswith(('Hi', 'Hello'))}")


# =============================================================================
# SECTION 6: STRING METHODS - MODIFICATION
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: STRING METHODS - MODIFICATION")
print("=" * 60)

# Note: All methods return NEW strings (strings are immutable)

# -----------------------------------------------------------------------------
# replace() - Replace occurrences
# -----------------------------------------------------------------------------
text = "Hello, World! Hello, Python!"
print(f"\n    text = '{text}'")

print("\n6.1 replace():")
print(f"    replace('Hello', 'Hi') = '{text.replace('Hello', 'Hi')}'")
print(f"    replace('Hello', 'Hi', 1) = '{text.replace('Hello', 'Hi', 1)}'")

# -----------------------------------------------------------------------------
# strip(), lstrip(), rstrip() - Remove whitespace/characters
# -----------------------------------------------------------------------------
padded = "   Hello, World!   "
print(f"\n6.2 strip() methods on '   Hello, World!   ':")
print(f"    strip()  = '{padded.strip()}'")
print(f"    lstrip() = '{padded.lstrip()}'")
print(f"    rstrip() = '{padded.rstrip()}'")

# Remove specific characters
text = "###Hello###"
print(f"\n6.3 strip specific characters on '###Hello###':")
print(f"    strip('#') = '{text.strip('#')}'")

# -----------------------------------------------------------------------------
# center(), ljust(), rjust() - Padding
# -----------------------------------------------------------------------------
word = "Python"
print(f"\n6.4 Padding methods on 'Python':")
print(f"    center(20, '-') = '{word.center(20, '-')}'")
print(f"    ljust(20, '-')  = '{word.ljust(20, '-')}'")
print(f"    rjust(20, '-')  = '{word.rjust(20, '-')}'")
print(f"    zfill(10)       = '{word.zfill(10)}'")

# -----------------------------------------------------------------------------
# expandtabs() - Replace tabs with spaces
# -----------------------------------------------------------------------------
tabbed = "Hello\tWorld\tPython"
print(f"\n6.5 expandtabs() on 'Hello\\tWorld\\tPython':")
print(f"    expandtabs(4) = '{tabbed.expandtabs(4)}'")


# =============================================================================
# SECTION 7: STRING METHODS - SPLITTING AND JOINING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: STRING METHODS - SPLITTING AND JOINING")
print("=" * 60)

# -----------------------------------------------------------------------------
# split() - Split string into list
# -----------------------------------------------------------------------------
sentence = "Hello World Python Programming"
print(f"\n    sentence = '{sentence}'")

print("\n7.1 split():")
print(f"    split() = {sentence.split()}")
print(f"    split(' ', 2) = {sentence.split(' ', 2)}")

csv_data = "apple,banana,cherry,date"
print(f"\n7.2 split with delimiter:")
print(f"    '{csv_data}'.split(',') = {csv_data.split(',')}")

# -----------------------------------------------------------------------------
# rsplit() - Split from right
# -----------------------------------------------------------------------------
print("\n7.3 rsplit():")
print(f"    rsplit(' ', 2) = {sentence.rsplit(' ', 2)}")

# -----------------------------------------------------------------------------
# splitlines() - Split by line breaks
# -----------------------------------------------------------------------------
multiline = "Line 1\nLine 2\nLine 3"
print(f"\n7.4 splitlines():")
print(f"    '{multiline}'.splitlines() = {multiline.splitlines()}")

# -----------------------------------------------------------------------------
# join() - Join iterable with separator
# -----------------------------------------------------------------------------
words = ['Hello', 'World', 'Python']
print(f"\n7.5 join():")
print(f"    ' '.join({words}) = '{' '.join(words)}'")
print(f"    '-'.join({words}) = '{'-'.join(words)}'")
print(f"    ''.join({words}) = '{''.join(words)}'")

# -----------------------------------------------------------------------------
# partition() and rpartition() - Split into 3 parts
# -----------------------------------------------------------------------------
text = "hello@example.com"
print(f"\n7.6 partition() on '{text}':")
print(f"    partition('@') = {text.partition('@')}")
print(f"    rpartition('.') = {text.rpartition('.')}")


# =============================================================================
# SECTION 8: STRING METHODS - CHECKING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: STRING METHODS - CHECKING")
print("=" * 60)

# -----------------------------------------------------------------------------
# Character type checks (return boolean)
# -----------------------------------------------------------------------------
print("\n8.1 isalpha() - only letters:")
print(f"    'Hello'.isalpha() = {'Hello'.isalpha()}")
print(f"    'Hello123'.isalpha() = {'Hello123'.isalpha()}")

print("\n8.2 isdigit() - only digits:")
print(f"    '12345'.isdigit() = {'12345'.isdigit()}")
print(f"    '123.45'.isdigit() = {'123.45'.isdigit()}")

print("\n8.3 isalnum() - letters or digits:")
print(f"    'Hello123'.isalnum() = {'Hello123'.isalnum()}")
print(f"    'Hello 123'.isalnum() = {'Hello 123'.isalnum()}")

print("\n8.4 isspace() - only whitespace:")
print(f"    '   '.isspace() = {'   '.isspace()}")
print(f"    ' a '.isspace() = {' a '.isspace()}")

print("\n8.5 Case checking:")
print(f"    'HELLO'.isupper() = {'HELLO'.isupper()}")
print(f"    'hello'.islower() = {'hello'.islower()}")
print(f"    'Hello World'.istitle() = {'Hello World'.istitle()}")

print("\n8.6 Other checks:")
print(f"    '123'.isnumeric() = {'123'.isnumeric()}")
print(f"    'x'.isidentifier() = {'x'.isidentifier()}")
print(f"    'for'.isidentifier() = {'for'.isidentifier()}")
print(f"    'Hello'.isascii() = {'Hello'.isascii()}")
print(f"    ''.isprintable() = {''.isprintable()}")


# =============================================================================
# SECTION 9: STRING FORMATTING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: STRING FORMATTING")
print("=" * 60)

name = "Alice"
age = 30
price = 49.99

# -----------------------------------------------------------------------------
# Method 1: f-strings (Python 3.6+) - RECOMMENDED
# -----------------------------------------------------------------------------
print("\n9.1 f-strings (recommended):")
print(f"    f'Name: {{name}}' = f'Name: {name}'")
print(f"    f'Age: {{age}}' = f'Age: {age}'")
print(f"    f'Next year: {{age + 1}}' = f'Next year: {age + 1}'")

# f-string formatting
print("\n9.2 f-string format specifiers:")
print(f"    Price: ${price:.2f}")           # 2 decimal places
print(f"    Padded: {age:05d}")             # Zero-padded
print(f"    Aligned: |{name:>10}|")         # Right align
print(f"    Aligned: |{name:<10}|")         # Left align
print(f"    Aligned: |{name:^10}|")         # Center align
print(f"    Percentage: {0.85:.1%}")        # As percentage
print(f"    Binary: {42:b}, Hex: {255:x}")  # Base conversion

# -----------------------------------------------------------------------------
# Method 2: format() method
# -----------------------------------------------------------------------------
print("\n9.3 format() method:")
print("    '{} is {} years old'.format(name, age) = " + 
      "'{} is {} years old'".format(name, age))
print("    '{0} - {1} - {0}'.format('A', 'B') = " +
      "'{0} - {1} - {0}'".format('A', 'B'))
print("    '{name} is {age}'.format(name='Bob', age=25) = " +
      "'{name} is {age}'".format(name='Bob', age=25))

# -----------------------------------------------------------------------------
# Method 3: % operator (old style)
# -----------------------------------------------------------------------------
print("\n9.4 % operator (old style):")
print("    '%s is %d years old' % (name, age) = " +
      "'%s is %d years old'" % (name, age))
print("    'Price: $%.2f' % price = " + "'Price: $%.2f'" % price)

# -----------------------------------------------------------------------------
# Method 4: Template strings (for user input)
# -----------------------------------------------------------------------------
from string import Template
print("\n9.5 Template strings (safe for user input):")
t = Template('$name is $age years old')
result = t.substitute(name='Charlie', age=35)
print(f"    Template result: {result}")


# =============================================================================
# SECTION 10: STRING CONCATENATION
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 10: STRING CONCATENATION")
print("=" * 60)

# -----------------------------------------------------------------------------
# Method 1: + operator
# Creates a new string each time (inefficient for many concatenations)
# -----------------------------------------------------------------------------
print("\n10.1 + operator:")
greeting = "Hello" + " " + "World"
print(f"    'Hello' + ' ' + 'World' = '{greeting}'")

# -----------------------------------------------------------------------------
# Method 2: join() - EFFICIENT for multiple strings
# -----------------------------------------------------------------------------
print("\n10.2 join() - efficient for many strings:")
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(f"    ' '.join({words}) = '{result}'")

# -----------------------------------------------------------------------------
# Method 3: f-strings for mixed types
# -----------------------------------------------------------------------------
print("\n10.3 f-strings for mixed types:")
name = "Alice"
score = 95.5
result = f"{name} scored {score} points"
print(f"    f'{{name}} scored {{score}} points' = '{result}'")

# -----------------------------------------------------------------------------
# Performance comparison for many concatenations
# -----------------------------------------------------------------------------
print("\n10.4 Performance tip:")
print("""    BAD (O(n²)):                    GOOD (O(n)):
    result = ""                      parts = []
    for s in strings:                for s in strings:
        result += s                      parts.append(s)
                                     result = "".join(parts)
""")


# =============================================================================
# SECTION 11: COMMON STRING OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 11: COMMON STRING OPERATIONS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Repetition
# -----------------------------------------------------------------------------
print("\n11.1 String repetition:")
print(f"    'Ha' * 3 = '{'Ha' * 3}'")
print(f"    '-' * 20 = '{'-' * 20}'")

# -----------------------------------------------------------------------------
# Length
# -----------------------------------------------------------------------------
text = "Hello, World!"
print(f"\n11.2 String length:")
print(f"    len('{text}') = {len(text)}")

# -----------------------------------------------------------------------------
# Iteration
# -----------------------------------------------------------------------------
print("\n11.3 Iterating over characters:")
for i, char in enumerate("Hi!"):
    print(f"    Index {i}: '{char}'")

# -----------------------------------------------------------------------------
# Reversing
# -----------------------------------------------------------------------------
print("\n11.4 Reversing strings:")
original = "Python"
reversed_str = original[::-1]
print(f"    '{original}'[::-1] = '{reversed_str}'")

# Alternative with reversed()
reversed_str2 = ''.join(reversed(original))
print(f"    ''.join(reversed('{original}')) = '{reversed_str2}'")

# -----------------------------------------------------------------------------
# Checking palindrome
# -----------------------------------------------------------------------------
print("\n11.5 Palindrome check:")
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

test_words = ["radar", "hello", "A man a plan a canal Panama"]
for word in test_words:
    print(f"    '{word}' is palindrome: {is_palindrome(word)}")


# =============================================================================
# SECTION 12: ENCODING AND DECODING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 12: ENCODING AND DECODING")
print("=" * 60)

# -----------------------------------------------------------------------------
# Strings to bytes (encoding)
# -----------------------------------------------------------------------------
text = "Hello, 世界!"
print(f"\n    text = '{text}'")

print("\n12.1 Encoding (str -> bytes):")
utf8_bytes = text.encode('utf-8')
print(f"    encode('utf-8') = {utf8_bytes}")
print(f"    encode('ascii', errors='ignore') = {text.encode('ascii', errors='ignore')}")

# -----------------------------------------------------------------------------
# Bytes to string (decoding)
# -----------------------------------------------------------------------------
print("\n12.2 Decoding (bytes -> str):")
decoded = utf8_bytes.decode('utf-8')
print(f"    {utf8_bytes}.decode('utf-8') = '{decoded}'")

# -----------------------------------------------------------------------------
# ord() and chr() - character to/from Unicode code point
# -----------------------------------------------------------------------------
print("\n12.3 ord() and chr():")
print(f"    ord('A') = {ord('A')}")
print(f"    ord('中') = {ord('中')}")
print(f"    chr(65) = '{chr(65)}'")
print(f"    chr(20013) = '{chr(20013)}'")


# =============================================================================
# SECTION 13: REGULAR EXPRESSIONS (BRIEF)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 13: REGULAR EXPRESSIONS (BRIEF)")
print("=" * 60)

import re

text = "Contact: john@email.com or jane@example.org"
print(f"\n    text = '{text}'")

# -----------------------------------------------------------------------------
# Pattern matching
# -----------------------------------------------------------------------------
print("\n13.1 Finding patterns:")
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(f"    Emails found: {emails}")

# -----------------------------------------------------------------------------
# Substitution
# -----------------------------------------------------------------------------
print("\n13.2 Substitution:")
censored = re.sub(r'@[\w.-]+', '@[HIDDEN]', text)
print(f"    Censored: '{censored}'")

# -----------------------------------------------------------------------------
# Split with pattern
# -----------------------------------------------------------------------------
print("\n13.3 Split with pattern:")
words = re.split(r'[,\s:]+', text)
print(f"    Words: {words}")


# =============================================================================
# SECTION 14: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 14: PRACTICAL EXAMPLES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Example 1: Validate email format (simple)
# -----------------------------------------------------------------------------
print("\n14.1 Simple email validation:")
def is_valid_email(email):
    return '@' in email and '.' in email.split('@')[-1]

test_emails = ['user@example.com', 'invalid', 'no@domain']
for email in test_emails:
    print(f"    '{email}' valid: {is_valid_email(email)}")

# -----------------------------------------------------------------------------
# Example 2: Clean and normalize text
# -----------------------------------------------------------------------------
print("\n14.2 Text normalization:")
def normalize_text(text):
    return ' '.join(text.lower().split())

messy = "   Hello    World   Python   "
print(f"    Original: '{messy}'")
print(f"    Normalized: '{normalize_text(messy)}'")

# -----------------------------------------------------------------------------
# Example 3: Extract initials
# -----------------------------------------------------------------------------
print("\n14.3 Extract initials:")
def get_initials(name):
    return ''.join(word[0].upper() for word in name.split())

names = ["John Doe", "Alice Bob Carter", "Single"]
for name in names:
    print(f"    '{name}' -> '{get_initials(name)}'")

# -----------------------------------------------------------------------------
# Example 4: Word frequency
# -----------------------------------------------------------------------------
print("\n14.4 Word frequency:")
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.lower().split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(f"    Text: '{text}'")
print(f"    Frequency: {freq}")

# -----------------------------------------------------------------------------
# Example 5: Title case with exceptions
# -----------------------------------------------------------------------------
print("\n14.5 Smart title case:")
def smart_title(text, exceptions={'a', 'an', 'the', 'of', 'in', 'on'}):
    words = text.lower().split()
    result = [words[0].capitalize()]
    result.extend(
        w if w in exceptions else w.capitalize()
        for w in words[1:]
    )
    return ' '.join(result)

title = "the lord of the rings"
print(f"    Original: '{title}'")
print(f"    Smart title: '{smart_title(title)}'")


print("\n" + "=" * 60)
print("END OF STRINGS TUTORIAL")
print("=" * 60)
