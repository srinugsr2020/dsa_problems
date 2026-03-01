"""
=============================================================================
PYTHON DICTIONARIES - COMPREHENSIVE GUIDE
=============================================================================

Dictionaries are mutable, unordered (Python 3.7+ maintains insertion order)
collections of key-value pairs. Keys must be immutable (strings, numbers, tuples).

Key Characteristics:
- Fast O(1) average lookup, insert, and delete operations
- Keys must be unique and hashable
- Values can be any Python object
- Maintains insertion order (Python 3.7+)
=============================================================================
"""

# =============================================================================
# SECTION 1: CREATING DICTIONARIES
# =============================================================================

print("=" * 60)
print("SECTION 1: CREATING DICTIONARIES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Method 1: Literal syntax using curly braces {}
# Most common and readable way to create dictionaries
# -----------------------------------------------------------------------------
dict1 = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'address': '123 Main St'
}
print("\n1.1 Literal syntax (curly braces):")
print(f"    dict1 = {dict1}")

# -----------------------------------------------------------------------------
# Method 2: Using dict() constructor with keyword arguments
# Clean syntax when keys are valid Python identifiers (no spaces/special chars)
# -----------------------------------------------------------------------------
dict2 = dict(
    name='Bob',
    age=25,
    city='Los Angeles',
    address='456 Elm St'
)
print("\n1.2 dict() with keyword arguments:")
print(f"    dict2 = {dict2}")

# -----------------------------------------------------------------------------
# Method 3: Using dict() with a list of tuples
# Useful when building dictionaries from paired data
# Note: Use parentheses () to call dict, not square brackets []
# -----------------------------------------------------------------------------
dict3 = dict([
    ('name', 'Charlie'),
    ('age', 35),
    ('city', 'Chicago'),
    ('address', '789 Oak St')
])
print("\n1.3 dict() with list of tuples:")
print(f"    dict3 = {dict3}")

# -----------------------------------------------------------------------------
# Method 4: Using zip() to combine two lists into a dictionary
# Perfect for creating dictionaries from parallel lists
# -----------------------------------------------------------------------------
places = ['New York', 'Los Angeles', 'Chicago']
teams = ['Yankees', 'Lakers', 'Bulls']
dict4 = dict(zip(places, teams))
print("\n1.4 dict() with zip():")
print(f"    places = {places}")
print(f"    teams = {teams}")
print(f"    dict4 = {dict4}")

# -----------------------------------------------------------------------------
# Method 5: Using fromkeys() to create a dictionary with default values
# Great for initializing counters or default configurations
# -----------------------------------------------------------------------------
inventory = dict.fromkeys(["apple", "orange", "banana", "mango"], 0)
print("\n1.5 dict.fromkeys() with default value:")
print(f"    inventory = {inventory}")

# -----------------------------------------------------------------------------
# Method 6: Nested dictionaries and complex values
# Dictionaries can contain lists, other dictionaries, or any Python object
# -----------------------------------------------------------------------------
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 35,
    "spouse": "Jane",
    "children": ["Ralph", "Betty", "Bob"],  # List as value
    "pets": {"dog": "Frieda", "cat": "Sox"},  # Nested dictionary
}
print("\n1.6 Nested dictionary:")
print(f"    person = {person}")

# -----------------------------------------------------------------------------
# Method 7: Dictionary comprehension
# Concise way to create dictionaries using a loop expression
# -----------------------------------------------------------------------------
squares = {i: i * i for i in range(1, 6)}
print("\n1.7 Dictionary comprehension:")
print(f"    squares = {squares}")


# =============================================================================
# SECTION 2: ACCESSING DICTIONARY ELEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: ACCESSING DICTIONARY ELEMENTS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Access values using square bracket notation
# Raises KeyError if key doesn't exist
# -----------------------------------------------------------------------------
print("\n2.1 Direct access with []:")
print(f"    person['first_name'] = {person['first_name']}")
print(f"    person['pets']['dog'] = {person['pets']['dog']}")  # Nested access
print(f"    person['children'][0] = {person['children'][0]}")  # List in dict

# -----------------------------------------------------------------------------
# Get all keys, values, and key-value pairs
# These return view objects that reflect dictionary changes
# -----------------------------------------------------------------------------
print("\n2.2 Dictionary views:")
print(f"    person.keys()   = {list(person.keys())}")
print(f"    person.values() = {list(person.values())}")
print(f"    squares.items() = {list(squares.items())}")


# =============================================================================
# SECTION 3: UPDATING DICTIONARIES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: UPDATING DICTIONARIES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Create a base configuration dictionary
# -----------------------------------------------------------------------------
config = {
    "color": "green",
    "width": 42,
    "height": 100,
    "font": "Courier",
}
print("\n3.1 Original config:")
print(f"    config = {config}")

# -----------------------------------------------------------------------------
# Method 1: update() with another dictionary
# Existing keys are overwritten, new keys are added
# -----------------------------------------------------------------------------
user_config = {
    "path": "/home",
    "color": "red",      # Overwrites existing 'color'
    "font": "Arial",     # Overwrites existing 'font'
    "position": (200, 100),  # New key added
}
config.update(user_config)
print("\n3.2 After config.update(user_config):")
print(f"    config = {config}")

# -----------------------------------------------------------------------------
# Method 2: update() with a list of tuples
# Alternative syntax for updating multiple key-value pairs
# -----------------------------------------------------------------------------
config.update([("width", 200), ("api_key", 1234)])
print("\n3.3 After config.update([tuples]):")
print(f"    config = {config}")


# =============================================================================
# SECTION 4: DELETING DICTIONARY ELEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: DELETING DICTIONARY ELEMENTS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Method 1: del statement
# Removes the key-value pair, does NOT return the value
# Raises KeyError if key doesn't exist
# -----------------------------------------------------------------------------
del config['height']
print("\n4.1 After del config['height']:")
print(f"    config = {config}")

# -----------------------------------------------------------------------------
# Method 2: pop() method
# Removes and RETURNS the value for the specified key
# Can provide a default value to avoid KeyError
# -----------------------------------------------------------------------------
removed_font = config.pop('font')
print("\n4.2 After config.pop('font'):")
print(f"    config = {config}")
print(f"    Removed value: '{removed_font}'")

# -----------------------------------------------------------------------------
# Method 3: popitem() method
# Removes and returns the LAST inserted key-value pair as a tuple
# Follows LIFO (Last-In, First-Out) order
# Raises KeyError if dictionary is empty
# -----------------------------------------------------------------------------
key, value = config.popitem()
print("\n4.3 After config.popitem():")
print(f"    config = {config}")
print(f"    Removed pair: '{key}' -> '{value}'")


# =============================================================================
# SECTION 5: SORTING DICTIONARIES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: SORTING DICTIONARIES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Create a student grades dictionary
# -----------------------------------------------------------------------------
students = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
    "Fiona": 95.6,
    "George": 73.4,
    "Hannah": 81.2,
}
print("\n5.1 Original students dictionary:")
print(f"    {students}")

# -----------------------------------------------------------------------------
# Sort by value (ascending order - lowest grade first)
# sorted() returns a list of tuples, dict() converts back to dictionary
# lambda x: x[1] extracts the value (grade) for comparison
# -----------------------------------------------------------------------------
students = dict(sorted(students.items(), key=lambda x: x[1]))
print("\n5.2 Sorted by grade (ascending):")
print(f"    {students}")

# -----------------------------------------------------------------------------
# Sort by value (descending order - highest grade first)
# reverse=True reverses the sort order
# -----------------------------------------------------------------------------
students = dict(sorted(students.items(), key=lambda item: item[1], reverse=True))
print("\n5.3 Sorted by grade (descending):")
print(f"    {students}")


# =============================================================================
# SECTION 6: ITERATING OVER DICTIONARIES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: ITERATING OVER DICTIONARIES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Method 1: enumerate() for numbered iteration
# Provides index along with the key during iteration
# Note: Iterating over dict directly gives keys only
# -----------------------------------------------------------------------------
print("\n6.1 Using enumerate() for numbered list:")
for i, student in enumerate(students):
    print(f"    {i + 1}. {student}: {students[student]}")

# -----------------------------------------------------------------------------
# Method 2: reversed() for reverse iteration
# Iterates through keys in reverse insertion order
# Works because Python 3.7+ dictionaries maintain insertion order
# -----------------------------------------------------------------------------
print("\n6.2 Using reversed() for reverse order:")
for student in reversed(students):
    print(f"    {student}: {students[student]}")

# -----------------------------------------------------------------------------
# Method 3: items() for key-value pair iteration
# Most Pythonic way to iterate when you need both key and value
# -----------------------------------------------------------------------------
print("\n6.3 Using items() for key-value pairs:")
for name, grade in students.items():
    print(f"    {name} scored {grade}")


# =============================================================================
# SECTION 7: USEFUL DICTIONARY METHODS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: USEFUL DICTIONARY METHODS")
print("=" * 60)

# -----------------------------------------------------------------------------
# get() - Safe access with default value
# Returns None (or specified default) if key doesn't exist
# Avoids KeyError exceptions
# -----------------------------------------------------------------------------
sample = {"a": 1, "b": 2}
print("\n7.1 get() with default value:")
print(f"    sample.get('a') = {sample.get('a')}")           # Returns 1
print(f"    sample.get('z') = {sample.get('z')}")           # Returns None
print(f"    sample.get('z', 0) = {sample.get('z', 0)}")     # Returns 0 (default)

# -----------------------------------------------------------------------------
# setdefault() - Get value or set default if missing
# Returns existing value if key exists, otherwise sets and returns default
# -----------------------------------------------------------------------------
print("\n7.2 setdefault():")
print(f"    sample.setdefault('b', 99) = {sample.setdefault('b', 99)}")  # Returns 2 (exists)
print(f"    sample.setdefault('c', 99) = {sample.setdefault('c', 99)}")  # Sets and returns 99
print(f"    sample = {sample}")

# -----------------------------------------------------------------------------
# copy() - Create a shallow copy
# Changes to the copy don't affect the original (for simple values)
# -----------------------------------------------------------------------------
original = {"x": 10, "y": 20}
shallow_copy = original.copy()
shallow_copy["x"] = 999
print("\n7.3 copy() - shallow copy:")
print(f"    original = {original}")
print(f"    shallow_copy = {shallow_copy}")

# -----------------------------------------------------------------------------
# clear() - Remove all items
# Dictionary becomes empty but object remains the same
# -----------------------------------------------------------------------------
to_clear = {"temp": 1, "data": 2}
print("\n7.4 clear():")
print(f"    Before: {to_clear}")
to_clear.clear()
print(f"    After:  {to_clear}")


# =============================================================================
# SECTION 8: DICTIONARY COMPREHENSIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: DICTIONARY COMPREHENSIONS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Basic comprehension - transform data into dictionary
# -----------------------------------------------------------------------------
cubes = {x: x ** 3 for x in range(1, 6)}
print("\n8.1 Basic comprehension (cubes):")
print(f"    {cubes}")

# -----------------------------------------------------------------------------
# Comprehension with condition - filter while creating
# -----------------------------------------------------------------------------
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}
print("\n8.2 Comprehension with condition (even squares):")
print(f"    {even_squares}")

# -----------------------------------------------------------------------------
# Transform existing dictionary
# -----------------------------------------------------------------------------
prices = {"apple": 1.50, "banana": 0.75, "orange": 2.00}
discounted = {item: price * 0.9 for item, price in prices.items()}
print("\n8.3 Transform dictionary (10% discount):")
print(f"    Original:   {prices}")
print(f"    Discounted: {discounted}")

# -----------------------------------------------------------------------------
# Swap keys and values
# -----------------------------------------------------------------------------
grades_map = {"A": 90, "B": 80, "C": 70}
reverse_map = {v: k for k, v in grades_map.items()}
print("\n8.4 Swap keys and values:")
print(f"    Original: {grades_map}")
print(f"    Swapped:  {reverse_map}")


print("\n" + "=" * 60)
print("END OF DICTIONARY TUTORIAL")
print("=" * 60)
