"""
=============================================================================
PYTHON TUPLES - COMPREHENSIVE GUIDE
=============================================================================

Tuples are immutable, ordered sequences that can hold elements of any type.
Once created, their contents cannot be changed, making them hashable and
suitable for use as dictionary keys.

Key Characteristics:
- Immutable: Cannot be modified after creation
- Ordered: Elements maintain their insertion order
- Indexed: Elements accessible via zero-based indices
- Heterogeneous: Can contain mixed data types
- Hashable: Can be used as dictionary keys (if all elements are hashable)
- Memory efficient: Slightly more efficient than lists
=============================================================================
"""

# =============================================================================
# SECTION 1: CREATING TUPLES
# =============================================================================

print("=" * 60)
print("SECTION 1: CREATING TUPLES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Method 1: Literal syntax using parentheses ()
# Most common way to create tuples
# -----------------------------------------------------------------------------
coordinates = (10, 20, 30)
print("\n1.1 Literal syntax (parentheses):")
print(f"    coordinates = {coordinates}")

# -----------------------------------------------------------------------------
# Method 2: Tuple packing (without parentheses)
# Python automatically packs comma-separated values into tuple
# -----------------------------------------------------------------------------
packed = 1, 2, 3, 4, 5
print("\n1.2 Tuple packing (no parentheses):")
print(f"    packed = 1, 2, 3, 4, 5 -> {packed}")
print(f"    type: {type(packed)}")

# -----------------------------------------------------------------------------
# Method 3: Single element tuple (MUST have trailing comma)
# Without comma, it's just a value in parentheses
# -----------------------------------------------------------------------------
single = (42,)          # This is a tuple
not_tuple = (42)        # This is just an integer!
print("\n1.3 Single element tuple (trailing comma required):")
print(f"    (42,) -> {single}, type: {type(single)}")
print(f"    (42)  -> {not_tuple}, type: {type(not_tuple)}")

# -----------------------------------------------------------------------------
# Method 4: Empty tuple
# -----------------------------------------------------------------------------
empty1 = ()
empty2 = tuple()
print("\n1.4 Empty tuples:")
print(f"    () = {empty1}")
print(f"    tuple() = {empty2}")

# -----------------------------------------------------------------------------
# Method 5: Using tuple() constructor
# Converts iterables to tuples
# -----------------------------------------------------------------------------
from_list = tuple([1, 2, 3])
from_string = tuple("hello")
from_range = tuple(range(1, 6))
print("\n1.5 tuple() constructor:")
print(f"    tuple([1,2,3]) = {from_list}")
print(f"    tuple('hello') = {from_string}")
print(f"    tuple(range(1,6)) = {from_range}")

# -----------------------------------------------------------------------------
# Method 6: Nested tuples
# Tuples can contain other tuples
# -----------------------------------------------------------------------------
nested = ((1, 2), (3, 4), (5, 6))
print("\n1.6 Nested tuples:")
print(f"    {nested}")

# -----------------------------------------------------------------------------
# Method 7: Mixed data types
# Tuples can hold any type of data
# -----------------------------------------------------------------------------
mixed = ("Alice", 25, True, 3.14, [1, 2, 3])
print("\n1.7 Mixed data types:")
print(f"    {mixed}")


# =============================================================================
# SECTION 2: ACCESSING TUPLE ELEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: ACCESSING TUPLE ELEMENTS")
print("=" * 60)

data = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(f"\n    data = {data}")

# -----------------------------------------------------------------------------
# Positive indexing (0-based, left to right)
# -----------------------------------------------------------------------------
print("\n2.1 Positive indexing:")
print(f"    data[0] = {data[0]}")
print(f"    data[4] = {data[4]}")

# -----------------------------------------------------------------------------
# Negative indexing (right to left, -1 is last)
# -----------------------------------------------------------------------------
print("\n2.2 Negative indexing:")
print(f"    data[-1] = {data[-1]}")
print(f"    data[-3] = {data[-3]}")

# -----------------------------------------------------------------------------
# Slicing: tuple[start:stop:step]
# Returns a NEW tuple (original unchanged)
# -----------------------------------------------------------------------------
print("\n2.3 Slicing [start:stop:step]:")
print(f"    data[2:5] = {data[2:5]}")
print(f"    data[:4] = {data[:4]}")
print(f"    data[6:] = {data[6:]}")
print(f"    data[::2] = {data[::2]}")
print(f"    data[::-1] = {data[::-1]}")  # Reversed tuple

# -----------------------------------------------------------------------------
# Accessing nested tuple elements
# -----------------------------------------------------------------------------
nested = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("\n2.4 Nested tuple access:")
print(f"    nested[1][2] = {nested[1][2]}")  # Row 1, Column 2 = 6


# =============================================================================
# SECTION 3: TUPLE UNPACKING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: TUPLE UNPACKING")
print("=" * 60)

# -----------------------------------------------------------------------------
# Basic unpacking - assign tuple elements to variables
# Number of variables must match tuple length
# -----------------------------------------------------------------------------
point = (10, 20, 30)
x, y, z = point
print("\n3.1 Basic unpacking:")
print(f"    point = {point}")
print(f"    x, y, z = point -> x={x}, y={y}, z={z}")

# -----------------------------------------------------------------------------
# Unpacking in function returns
# Functions often return multiple values as tuples
# -----------------------------------------------------------------------------
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 1, 4, 1, 5, 9, 2, 6]
minimum, maximum = get_min_max(nums)
print("\n3.2 Function return unpacking:")
print(f"    min, max = {minimum}, {maximum}")

# -----------------------------------------------------------------------------
# Extended unpacking with * (Python 3+)
# Use * to capture remaining elements as a list
# -----------------------------------------------------------------------------
first, *middle, last = (1, 2, 3, 4, 5)
print("\n3.3 Extended unpacking (*):")
print(f"    first, *middle, last = (1,2,3,4,5)")
print(f"    first = {first}")
print(f"    middle = {middle}")  # This is a list!
print(f"    last = {last}")

head, *tail = (1, 2, 3, 4, 5)
print("\n3.4 Head and tail pattern:")
print(f"    head = {head}, tail = {tail}")

*init, last = (1, 2, 3, 4, 5)
print("\n3.5 Init and last pattern:")
print(f"    init = {init}, last = {last}")

# -----------------------------------------------------------------------------
# Swapping variables using tuple unpacking
# No temporary variable needed!
# -----------------------------------------------------------------------------
a, b = 10, 20
print("\n3.6 Swapping variables:")
print(f"    Before: a={a}, b={b}")
a, b = b, a
print(f"    After:  a={a}, b={b}")

# -----------------------------------------------------------------------------
# Unpacking in for loops
# -----------------------------------------------------------------------------
points = [(1, 2), (3, 4), (5, 6)]
print("\n3.7 Unpacking in loops:")
for x, y in points:
    print(f"    x={x}, y={y}")


# =============================================================================
# SECTION 4: TUPLE IMMUTABILITY
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: TUPLE IMMUTABILITY")
print("=" * 60)

# -----------------------------------------------------------------------------
# Tuples cannot be modified
# Attempting to modify raises TypeError
# -----------------------------------------------------------------------------
t = (1, 2, 3)
print("\n4.1 Tuples are immutable:")
print(f"    t = {t}")
print("    t[0] = 99  # This raises TypeError!")
# t[0] = 99  # Uncommenting this would raise TypeError

# -----------------------------------------------------------------------------
# However, mutable objects INSIDE tuples can be modified
# The tuple still points to the same object
# -----------------------------------------------------------------------------
mixed = (1, 2, [3, 4])
print("\n4.2 Mutable objects inside tuples:")
print(f"    Before: {mixed}")
mixed[2].append(5)  # Modifying the list inside tuple
print(f"    After mixed[2].append(5): {mixed}")

# -----------------------------------------------------------------------------
# Creating a new tuple from existing tuples
# Since tuples are immutable, we create new ones
# -----------------------------------------------------------------------------
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2  # Concatenation creates new tuple
print("\n4.3 Concatenation (creates new tuple):")
print(f"    t1 + t2 = {t3}")

t4 = t1 * 3  # Repetition creates new tuple
print("\n4.4 Repetition (creates new tuple):")
print(f"    t1 * 3 = {t4}")


# =============================================================================
# SECTION 5: TUPLE METHODS AND OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: TUPLE METHODS AND OPERATIONS")
print("=" * 60)

# Tuples only have 2 methods (because they're immutable)
sample = (1, 2, 3, 2, 4, 2, 5)
print(f"\n    sample = {sample}")

# -----------------------------------------------------------------------------
# count() - Count occurrences of a value
# -----------------------------------------------------------------------------
print("\n5.1 count():")
print(f"    sample.count(2) = {sample.count(2)}")
print(f"    sample.count(9) = {sample.count(9)}")

# -----------------------------------------------------------------------------
# index() - Find first occurrence index
# Raises ValueError if not found
# -----------------------------------------------------------------------------
print("\n5.2 index():")
print(f"    sample.index(2) = {sample.index(2)}")
print(f"    sample.index(2, 2) = {sample.index(2, 2)}")  # Start from index 2

# -----------------------------------------------------------------------------
# Membership testing (in / not in)
# -----------------------------------------------------------------------------
print("\n5.3 Membership testing:")
print(f"    3 in sample = {3 in sample}")
print(f"    9 in sample = {9 in sample}")
print(f"    9 not in sample = {9 not in sample}")

# -----------------------------------------------------------------------------
# Length, min, max, sum
# -----------------------------------------------------------------------------
nums = (3, 1, 4, 1, 5, 9, 2, 6)
print(f"\n5.4 Built-in functions with tuple {nums}:")
print(f"    len(nums) = {len(nums)}")
print(f"    min(nums) = {min(nums)}")
print(f"    max(nums) = {max(nums)}")
print(f"    sum(nums) = {sum(nums)}")


# =============================================================================
# SECTION 6: TUPLE COMPARISONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: TUPLE COMPARISONS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Tuples are compared element by element (lexicographically)
# -----------------------------------------------------------------------------
print("\n6.1 Tuple comparisons:")
print(f"    (1, 2, 3) == (1, 2, 3) = {(1, 2, 3) == (1, 2, 3)}")
print(f"    (1, 2, 3) < (1, 2, 4) = {(1, 2, 3) < (1, 2, 4)}")
print(f"    (1, 2) < (1, 2, 0) = {(1, 2) < (1, 2, 0)}")  # Shorter tuple is smaller
print(f"    ('a', 'b') < ('b', 'a') = {('a', 'b') < ('b', 'a')}")

# -----------------------------------------------------------------------------
# Sorting with tuples (natural ordering)
# Useful for sorting by multiple criteria
# -----------------------------------------------------------------------------
students = [
    ('Alice', 'A', 15),
    ('Bob', 'B', 15),
    ('Charlie', 'A', 16),
    ('Diana', 'A', 15),
]

# Sort by grade, then by name
sorted_students = sorted(students, key=lambda s: (s[1], s[0]))
print("\n6.2 Sorting with tuple keys:")
print("    Sorted by grade, then name:")
for student in sorted_students:
    print(f"    {student}")


# =============================================================================
# SECTION 7: TUPLES AS DICTIONARY KEYS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: TUPLES AS DICTIONARY KEYS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Tuples are hashable (if all elements are hashable)
# This makes them suitable as dictionary keys
# -----------------------------------------------------------------------------
print("\n7.1 Tuples as dictionary keys:")

# Location-based data
locations = {
    (40.7128, -74.0060): "New York City",
    (34.0522, -118.2437): "Los Angeles",
    (41.8781, -87.6298): "Chicago",
}
print("    Location dictionary:")
for coords, city in locations.items():
    print(f"    {coords} -> {city}")

# -----------------------------------------------------------------------------
# Multi-key dictionary (composite keys)
# -----------------------------------------------------------------------------
print("\n7.2 Composite keys (multi-dimensional lookup):")
grades = {
    ('Alice', 'Math'): 95,
    ('Alice', 'English'): 88,
    ('Bob', 'Math'): 82,
    ('Bob', 'English'): 91,
}
print(f"    grades[('Alice', 'Math')] = {grades[('Alice', 'Math')]}")
print(f"    grades[('Bob', 'English')] = {grades[('Bob', 'English')]}")

# -----------------------------------------------------------------------------
# Counting with tuple keys
# -----------------------------------------------------------------------------
from collections import Counter

moves = [(0, 1), (1, 0), (0, 1), (-1, 0), (0, 1)]
move_counts = Counter(moves)
print("\n7.3 Counting movements:")
print(f"    moves = {moves}")
print(f"    Counter = {dict(move_counts)}")


# =============================================================================
# SECTION 8: NAMEDTUPLES (ENHANCED TUPLES)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: NAMEDTUPLES (ENHANCED TUPLES)")
print("=" * 60)

from collections import namedtuple

# -----------------------------------------------------------------------------
# Create a named tuple class
# Like a lightweight class with named fields
# -----------------------------------------------------------------------------
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')  # String syntax also works

print("\n8.1 Creating namedtuple instances:")
p1 = Point(10, 20)
p2 = Point(x=30, y=40)  # Keyword arguments
print(f"    p1 = Point(10, 20) = {p1}")
print(f"    p2 = Point(x=30, y=40) = {p2}")

# -----------------------------------------------------------------------------
# Access by name OR index
# -----------------------------------------------------------------------------
print("\n8.2 Accessing namedtuple fields:")
print(f"    p1.x = {p1.x}")
print(f"    p1[0] = {p1[0]}")
print(f"    p1.y = {p1.y}")
print(f"    p1[1] = {p1[1]}")

# -----------------------------------------------------------------------------
# Namedtuple methods
# -----------------------------------------------------------------------------
alice = Person('Alice', 30, 'NYC')
print(f"\n8.3 Namedtuple methods:")
print(f"    alice = {alice}")
print(f"    alice._fields = {alice._fields}")
print(f"    alice._asdict() = {alice._asdict()}")

# Create new instance with some values replaced
bob = alice._replace(name='Bob', age=25)
print(f"    alice._replace(name='Bob', age=25) = {bob}")


# =============================================================================
# SECTION 9: TUPLE VS LIST - WHEN TO USE
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: TUPLE VS LIST - WHEN TO USE")
print("=" * 60)

print("""
9.1 Use TUPLES when:
    - Data should not change (coordinates, RGB colors)
    - Returning multiple values from functions
    - Dictionary keys (must be hashable)
    - Heterogeneous data (different types, like a record)
    - Performance matters (slightly faster than lists)

9.2 Use LISTS when:
    - Data needs to be modified (add, remove, change)
    - Homogeneous collections (same type items)
    - Order matters and will change
    - Need list methods (append, extend, sort, etc.)

9.3 Memory comparison:
""")

import sys
list_example = [1, 2, 3, 4, 5]
tuple_example = (1, 2, 3, 4, 5)
print(f"    List  {list_example}: {sys.getsizeof(list_example)} bytes")
print(f"    Tuple {tuple_example}: {sys.getsizeof(tuple_example)} bytes")


# =============================================================================
# SECTION 10: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 10: PRACTICAL EXAMPLES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Example 1: RGB Colors (immutable data)
# -----------------------------------------------------------------------------
print("\n10.1 RGB Colors:")
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = {'red': RED, 'green': GREEN, 'blue': BLUE}
for name, rgb in colors.items():
    print(f"    {name}: RGB{rgb}")

# -----------------------------------------------------------------------------
# Example 2: Geographic coordinates
# -----------------------------------------------------------------------------
print("\n10.2 Geographic coordinates:")
def calculate_distance(coord1, coord2):
    """Simple distance calculation."""
    x1, y1 = coord1
    x2, y2 = coord2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

point_a = (0, 0)
point_b = (3, 4)
distance = calculate_distance(point_a, point_b)
print(f"    Distance from {point_a} to {point_b} = {distance}")

# -----------------------------------------------------------------------------
# Example 3: Database-like records
# -----------------------------------------------------------------------------
print("\n10.3 Database records:")
Employee = namedtuple('Employee', ['id', 'name', 'department', 'salary'])
employees = [
    Employee(1, 'Alice', 'Engineering', 75000),
    Employee(2, 'Bob', 'Marketing', 65000),
    Employee(3, 'Charlie', 'Engineering', 80000),
]

# Filter and display
engineering = [e for e in employees if e.department == 'Engineering']
print("    Engineering department:")
for emp in engineering:
    print(f"    ID: {emp.id}, Name: {emp.name}, Salary: ${emp.salary:,}")


print("\n" + "=" * 60)
print("END OF TUPLES TUTORIAL")
print("=" * 60)
