"""
=============================================================================
PYTHON LISTS - COMPREHENSIVE GUIDE
=============================================================================

Lists are mutable, ordered sequences that can hold elements of any type.
They are one of the most versatile and commonly used data structures in Python.

Key Characteristics:
- Mutable: Elements can be added, removed, or changed
- Ordered: Elements maintain their insertion order
- Indexed: Elements accessible via zero-based indices
- Heterogeneous: Can contain mixed data types
- Dynamic: Size can grow or shrink as needed
=============================================================================
"""

# =============================================================================
# SECTION 1: CREATING LISTS
# =============================================================================

print("=" * 60)
print("SECTION 1: CREATING LISTS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Method 1: Literal syntax using square brackets []
# Most common and readable way to create lists
# -----------------------------------------------------------------------------
fruits = ['apple', 'banana', 'cherry', 'date']
print("\n1.1 Literal syntax (square brackets):")
print(f"    fruits = {fruits}")

# -----------------------------------------------------------------------------
# Method 2: Empty list creation
# Two ways to create an empty list
# -----------------------------------------------------------------------------
empty_list1 = []
empty_list2 = list()
print("\n1.2 Empty lists:")
print(f"    [] = {empty_list1}")
print(f"    list() = {empty_list2}")

# -----------------------------------------------------------------------------
# Method 3: Using list() constructor with an iterable
# Converts strings, tuples, sets, etc. to lists
# -----------------------------------------------------------------------------
from_string = list("hello")
from_tuple = list((1, 2, 3))
from_range = list(range(1, 6))
print("\n1.3 list() constructor:")
print(f"    list('hello') = {from_string}")
print(f"    list((1,2,3)) = {from_tuple}")
print(f"    list(range(1,6)) = {from_range}")

# -----------------------------------------------------------------------------
# Method 4: List comprehension
# Concise way to create lists using a loop expression
# -----------------------------------------------------------------------------
squares = [x ** 2 for x in range(1, 6)]
evens = [x for x in range(10) if x % 2 == 0]
odds = [x for x in range(10) if x % 2 != 0]
print("\n1.4 List comprehension:")
print(f"    squares = {squares}")
print(f"    evens = {evens}")

# -----------------------------------------------------------------------------
# Method 5: List multiplication (repetition)
# Creates a list with repeated elements
# -----------------------------------------------------------------------------
zeros = [0] * 5
pattern = [1, 2] * 3
print("\n1.5 List multiplication:")
print(f"    [0] * 5 = {zeros}")
print(f"    [1, 2] * 3 = {pattern}")

# -----------------------------------------------------------------------------
# Method 6: Nested lists (2D lists / matrices)
# Lists can contain other lists
# -----------------------------------------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\n1.6 Nested lists (matrix):")
for row in matrix:
    print(f"    {row}")


# =============================================================================
# SECTION 2: ACCESSING LIST ELEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: ACCESSING LIST ELEMENTS")
print("=" * 60)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
range_num = [x for x in range(10, 101, 10)]
print(f"\n    numbers = {numbers}")

# -----------------------------------------------------------------------------
# Positive indexing (0-based, left to right)
# -----------------------------------------------------------------------------
print("\n2.1 Positive indexing:")
print(f"    numbers[0] = {numbers[0]}")    # First element
print(f"    numbers[4] = {numbers[4]}")    # Fifth element

# -----------------------------------------------------------------------------
# Negative indexing (right to left, -1 is last)
# -----------------------------------------------------------------------------
print("\n2.2 Negative indexing:")
print(f"    numbers[-1] = {numbers[-1]}")  # Last element
print(f"    numbers[-3] = {numbers[-3]}")  # Third from end

# -----------------------------------------------------------------------------
# Slicing: list[start:stop:step]
# start is inclusive, stop is exclusive
# -----------------------------------------------------------------------------
print("\n2.3 Slicing [start:stop:step]:")
print(f"    numbers[2:5] = {numbers[2:5]}")      # Index 2 to 4
print(f"    numbers[:4] = {numbers[:4]}")        # First 4 elements
print(f"    numbers[6:] = {numbers[6:]}")        # From index 6 to end
print(f"    numbers[::2] = {numbers[::2]}")      # Every 2nd element
print(f"    numbers[::-1] = {numbers[::-1]}")    # Reversed list
print(f"    numbers[1:8:2] = {numbers[1:8:2]}")  # Index 1-7, step 2

# -----------------------------------------------------------------------------
# Accessing nested list elements
# -----------------------------------------------------------------------------
print("\n2.4 Nested list access:")
print(f"    matrix[1][2] = {matrix[1][2]}")  # Row 1, Column 2 = 6


# =============================================================================
# SECTION 3: MODIFYING LIST ELEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: MODIFYING LIST ELEMENTS")
print("=" * 60)

colors = ['red', 'green', 'blue', 'yellow']
print(f"\n    Original: {colors}")

# -----------------------------------------------------------------------------
# Single element modification
# -----------------------------------------------------------------------------
colors[1] = 'lime'
print("\n3.1 Single element modification:")
print(f"    colors[1] = 'lime' -> {colors}")

# -----------------------------------------------------------------------------
# Slice modification (replace multiple elements)
# -----------------------------------------------------------------------------
colors[1:3] = ['cyan', 'magenta']
print("\n3.2 Slice modification:")
print(f"    colors[1:3] = ['cyan', 'magenta'] -> {colors}")

# -----------------------------------------------------------------------------
# Insert elements using slice
# -----------------------------------------------------------------------------
nums = [1, 2, 5, 6]
nums[2:2] = [3, 4]  # Insert at index 2
print("\n3.3 Insert via slice:")
print(f"    nums[2:2] = [3, 4] -> {nums}")


# =============================================================================
# SECTION 4: ADDING ELEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: ADDING ELEMENTS")
print("=" * 60)

items = ['a', 'b', 'c']
print(f"\n    Original: {items}")

# -----------------------------------------------------------------------------
# append() - Add single element to the end
# Time Complexity: O(1) amortized
# -----------------------------------------------------------------------------
items.append('d')
print("\n4.1 append('d'):")
print(f"    {items}")

# -----------------------------------------------------------------------------
# extend() - Add multiple elements from an iterable
# Time Complexity: O(k) where k is length of iterable
# -----------------------------------------------------------------------------
items.extend(['e', 'f'])
print("\n4.2 extend(['e', 'f']):")
print(f"    {items}")

# -----------------------------------------------------------------------------
# insert() - Add element at specific index
# Time Complexity: O(n) - shifts all elements after index
# -----------------------------------------------------------------------------
items.insert(0, 'START')
items.insert(4, 'MIDDLE')
print("\n4.3 insert(index, value):")
print(f"    {items}")

# -----------------------------------------------------------------------------
# Concatenation with + operator
# Creates a NEW list (doesn't modify original)
# -----------------------------------------------------------------------------
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("\n4.4 Concatenation (+):")
print(f"    [1,2,3] + [4,5,6] = {combined}")


# =============================================================================
# SECTION 5: REMOVING ELEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: REMOVING ELEMENTS")
print("=" * 60)

data = ['a', 'b', 'c', 'd', 'e', 'b', 'f']
print(f"\n    Original: {data}")

# -----------------------------------------------------------------------------
# remove() - Remove first occurrence of value
# Raises ValueError if not found
# Time Complexity: O(n)
# -----------------------------------------------------------------------------
data.remove('b')
print("\n5.1 remove('b') - removes first 'b':")
print(f"    {data}")

# -----------------------------------------------------------------------------
# pop() - Remove and return element at index (default: last)
# Raises IndexError if empty or invalid index
# Time Complexity: O(1) for last, O(n) for others
# -----------------------------------------------------------------------------
last = data.pop()
print("\n5.2 pop() - removes and returns last:")
print(f"    Returned: '{last}', List: {data}")

second = data.pop(1)
print("\n5.3 pop(1) - removes and returns index 1:")
print(f"    Returned: '{second}', List: {data}")

# -----------------------------------------------------------------------------
# del statement - Remove by index or slice
# More flexible than pop(), doesn't return value
# -----------------------------------------------------------------------------
del data[0]
print("\n5.4 del data[0]:")
print(f"    {data}")

multi = [1, 2, 3, 4, 5, 6, 7]
del multi[2:5]
print("\n5.5 del multi[2:5] (slice deletion):")
print(f"    {multi}")

# -----------------------------------------------------------------------------
# clear() - Remove all elements
# -----------------------------------------------------------------------------
to_clear = [1, 2, 3]
to_clear.clear()
print("\n5.6 clear():")
print(f"    {to_clear}")


# =============================================================================
# SECTION 6: SEARCHING AND COUNTING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: SEARCHING AND COUNTING")
print("=" * 60)

letters = ['a', 'b', 'c', 'b', 'd', 'b', 'e']
print(f"\n    letters = {letters}")

# -----------------------------------------------------------------------------
# index() - Find first occurrence index
# Raises ValueError if not found
# Optional: start and stop parameters
# -----------------------------------------------------------------------------
print("\n6.1 index():")
print(f"    letters.index('b') = {letters.index('b')}")
print(f"    letters.index('b', 2) = {letters.index('b', 2)}")  # Start from index 2

# -----------------------------------------------------------------------------
# count() - Count occurrences of a value
# -----------------------------------------------------------------------------
print("\n6.2 count():")
print(f"    letters.count('b') = {letters.count('b')}")
print(f"    letters.count('z') = {letters.count('z')}")

# -----------------------------------------------------------------------------
# in operator - Check membership
# Time Complexity: O(n)
# -----------------------------------------------------------------------------
print("\n6.3 Membership testing (in):")
print(f"    'c' in letters = {'c' in letters}")
print(f"    'z' in letters = {'z' in letters}")


# =============================================================================
# SECTION 7: SORTING AND REVERSING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: SORTING AND REVERSING")
print("=" * 60)

# -----------------------------------------------------------------------------
# sort() - Sort list in place (modifies original)
# Returns None
# -----------------------------------------------------------------------------
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n    Original: {nums}")

nums.sort()
print("\n7.1 sort() - ascending (in-place):")
print(f"    {nums}")

nums.sort(reverse=True)
print("\n7.2 sort(reverse=True) - descending:")
print(f"    {nums}")

# -----------------------------------------------------------------------------
# sorted() - Return new sorted list (original unchanged)
# -----------------------------------------------------------------------------
words = ['banana', 'Apple', 'cherry', 'Date']
print(f"\n    Original: {words}")

sorted_words = sorted(words)
print("\n7.3 sorted() - case-sensitive:")
print(f"    {sorted_words}")

sorted_lower = sorted(words, key=str.lower, reverse=False)
print("\n7.4 sorted(key=str.lower) - case-insensitive:")
print(f"    {sorted_lower}")

# -----------------------------------------------------------------------------
# Sort with custom key function
# -----------------------------------------------------------------------------
people = [('Alice', 25), ('Bob', 30), ('Charlie', 20)]
by_age = sorted(people, key=lambda x: x[1])
print("\n7.5 sorted() with custom key:")
print(f"    Original: {people}")
print(f"    By age:   {by_age}")

# -----------------------------------------------------------------------------
# reverse() - Reverse list in place
# Returns None
# -----------------------------------------------------------------------------
items = [1, 2, 3, 4, 5]
items.reverse()
print("\n7.6 reverse() - in-place:")
print(f"    {items}")

# -----------------------------------------------------------------------------
# reversed() - Return reverse iterator (original unchanged)
# -----------------------------------------------------------------------------
original = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original))
print("\n7.7 reversed() - creates new list:")
print(f"    Original: {original}")
print(f"    Reversed: {reversed_list}")


# =============================================================================
# SECTION 8: LIST COMPREHENSIONS (ADVANCED)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: LIST COMPREHENSIONS (ADVANCED)")
print("=" * 60)

# -----------------------------------------------------------------------------
# Basic comprehension
# -----------------------------------------------------------------------------
cubes = [x ** 3 for x in range(1, 6)]
print("\n8.1 Basic: [x**3 for x in range(1,6)]")
print(f"    {cubes}")

# -----------------------------------------------------------------------------
# Comprehension with condition (filter)
# -----------------------------------------------------------------------------
evens = [x for x in range(20) if x % 2 == 0]
print("\n8.2 With filter: [x for x in range(20) if x % 2 == 0]")
print(f"    {evens}")

# -----------------------------------------------------------------------------
# Comprehension with if-else (transform)
# -----------------------------------------------------------------------------
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print("\n8.3 With if-else:")
print(f"    {labels}")

# -----------------------------------------------------------------------------
# Nested comprehension (flatten 2D list)
# -----------------------------------------------------------------------------
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print("\n8.4 Flatten nested list:")
print(f"    Matrix: {matrix}")
print(f"    Flat:   {flat}")

# -----------------------------------------------------------------------------
# Create 2D list with comprehension
# -----------------------------------------------------------------------------
grid = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("\n8.5 Create 2D list:")
print(f"    Multiplication table (3x3):")
for row in grid:
    print(f"    {row}")

# -----------------------------------------------------------------------------
# Comprehension with function calls
# -----------------------------------------------------------------------------
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
lengths = [len(word) for word in words]
print("\n8.6 With function calls:")
print(f"    Words: {words}")
print(f"    Upper: {upper_words}")
print(f"    Lengths: {lengths}")


# =============================================================================
# SECTION 9: COPYING LISTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: COPYING LISTS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Assignment creates a reference (NOT a copy)
# Changes to one affect the other
# -----------------------------------------------------------------------------
original = [1, 2, 3]
reference = original
reference[0] = 999
print("\n9.1 Assignment (creates reference):")
print(f"    original = {original}")
print(f"    reference = {reference}")
print("    (Both changed!)")

# -----------------------------------------------------------------------------
# Shallow copy methods
# Creates a new list but nested objects are still references
# -----------------------------------------------------------------------------
original = [1, 2, [3, 4]]

copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

print("\n9.2 Shallow copy methods:")
print(f"    original.copy() = {copy1}")
print(f"    original[:] = {copy2}")
print(f"    list(original) = {copy3}")

# Shallow copy issue with nested objects
copy1[2][0] = 999
print("\n9.3 Shallow copy issue with nested objects:")
print(f"    After modifying copy1[2][0] = 999:")
print(f"    original = {original}")
print(f"    copy1 = {copy1}")
print("    (Nested list changed in both!)")

# -----------------------------------------------------------------------------
# Deep copy - completely independent copy
# Use for nested structures
# -----------------------------------------------------------------------------
import copy

original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)
deep[2][0] = 999

print("\n9.4 Deep copy (copy.deepcopy):")
print(f"    original = {original}")
print(f"    deep = {deep}")
print("    (Completely independent)")


# =============================================================================
# SECTION 10: USEFUL LIST OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 10: USEFUL LIST OPERATIONS")
print("=" * 60)

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"\n    nums = {nums}")

# -----------------------------------------------------------------------------
# Built-in functions with lists
# -----------------------------------------------------------------------------
print("\n10.1 Built-in functions:")
print(f"    len(nums) = {len(nums)}")
print(f"    min(nums) = {min(nums)}")
print(f"    max(nums) = {max(nums)}")
print(f"    sum(nums) = {sum(nums)}")
print(f"    avg = sum/len = {sum(nums)/len(nums):.2f}")

# -----------------------------------------------------------------------------
# all() and any()
# -----------------------------------------------------------------------------
print("\n10.2 all() and any():")
print(f"    all([True, True, False]) = {all([True, True, False])}")
print(f"    any([True, True, False]) = {any([True, True, False])}")
print(f"    all([1, 2, 3]) = {all([1, 2, 3])}")  # Non-zero = True
print(f"    any([0, 0, 1]) = {any([0, 0, 1])}")  # At least one non-zero

# -----------------------------------------------------------------------------
# zip() - Combine multiple lists
# -----------------------------------------------------------------------------
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

zipped = list(zip(names, ages, cities))
print("\n10.3 zip() multiple lists:")
print(f"    names = {names}")
print(f"    ages = {ages}")
print(f"    cities = {cities}")
print(f"    zipped = {zipped}")

# -----------------------------------------------------------------------------
# enumerate() - Get index and value
# -----------------------------------------------------------------------------
fruits = ['apple', 'banana', 'cherry']
print("\n10.4 enumerate():")
for i, fruit in enumerate(fruits, start=10):
    print(f"    {i}. {fruit}")

# -----------------------------------------------------------------------------
# map() - Apply function to all elements
# -----------------------------------------------------------------------------
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print("\n10.5 map():")
print(f"    Original: {nums}")
print(f"    Doubled:  {doubled}")

# -----------------------------------------------------------------------------
# filter() - Filter elements by condition
# -----------------------------------------------------------------------------
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("\n10.6 filter():")
print(f"    Original: {nums}")
print(f"    Evens:    {evens}")

# -----------------------------------------------------------------------------
# reduce() - Reduce list to single value
# -----------------------------------------------------------------------------
from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print("\n10.7 reduce():")
print(f"    Product of {nums} = {product}")


# =============================================================================
# SECTION 11: ITERATING OVER LISTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 11: ITERATING OVER LISTS")
print("=" * 60)

colors = ['red', 'green', 'blue']

# -----------------------------------------------------------------------------
# Basic for loop
# -----------------------------------------------------------------------------
print("\n11.1 Basic for loop:")
for color in colors:
    print(f"    {color}")

# -----------------------------------------------------------------------------
# With enumerate (index + value)
# -----------------------------------------------------------------------------
print("\n11.2 With enumerate:")
for i, color in enumerate(colors):
    print(f"    {i}: {color}")

# -----------------------------------------------------------------------------
# Using range and len (when you need index)
# -----------------------------------------------------------------------------
print("\n11.3 Using range(len()):")
for i in range(len(colors)):
    print(f"    colors[{i}] = {colors[i]}")

# -----------------------------------------------------------------------------
# Iterating in reverse
# -----------------------------------------------------------------------------
print("\n11.4 Reverse iteration:")
for color in reversed(colors):
    print(f"    {color}")

# -----------------------------------------------------------------------------
# Iterate multiple lists together
# -----------------------------------------------------------------------------
sizes = ['S', 'M', 'L']
print("\n11.5 Iterate multiple lists (zip):")
for color, size in zip(colors, sizes):
    print(f"    {color} - {size}")


print("\n" + "=" * 60)
print("END OF LISTS TUTORIAL")
print("=" * 60)
