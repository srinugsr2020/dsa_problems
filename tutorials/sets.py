"""
=============================================================================
PYTHON SETS - COMPREHENSIVE GUIDE
=============================================================================

Sets are unordered, mutable collections of unique hashable elements.
They are optimized for membership testing, removing duplicates, and
performing mathematical set operations (union, intersection, etc.).

Key Characteristics:
- Unordered: No guaranteed order, no indexing
- Unique: Automatically removes duplicates
- Mutable: Elements can be added or removed
- Hashable elements only: Cannot contain lists, dicts, or other sets
- O(1) average lookup time: Very fast membership testing
=============================================================================
"""

# =============================================================================
# SECTION 1: CREATING SETS
# =============================================================================

print("=" * 60)
print("SECTION 1: CREATING SETS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Method 1: Literal syntax using curly braces {}
# Note: {} creates an empty dict, NOT an empty set!
# -----------------------------------------------------------------------------
fruits = {'apple', 'banana', 'cherry'}
print("\n1.1 Literal syntax (curly braces):")
print(f"    fruits = {fruits}")

# -----------------------------------------------------------------------------
# Method 2: Empty set (MUST use set(), not {})
# {} creates an empty dictionary, not a set!
# -----------------------------------------------------------------------------
empty_set = set()
empty_dict = {}
print("\n1.2 Empty set vs empty dict:")
print(f"    set() -> {empty_set}, type: {type(empty_set)}")
print(f"    {{}}   -> {empty_dict}, type: {type(empty_dict)}")

# -----------------------------------------------------------------------------
# Method 3: Using set() constructor
# Converts iterables to sets (duplicates removed)
# -----------------------------------------------------------------------------
from_list = set([1, 2, 2, 3, 3, 3])
from_string = set("hello")
from_range = set(range(1, 6))
print("\n1.3 set() constructor (duplicates removed):")
print(f"    set([1,2,2,3,3,3]) = {from_list}")
print(f"    set('hello') = {from_string}")
print(f"    set(range(1,6)) = {from_range}")

# -----------------------------------------------------------------------------
# Method 4: Set comprehension
# Similar to list comprehension but creates a set
# -----------------------------------------------------------------------------
squares = {x ** 2 for x in range(1, 6)}
evens = {x for x in range(20) if x % 2 == 0}
print("\n1.4 Set comprehension:")
print(f"    {{x**2 for x in range(1,6)}} = {squares}")
print(f"    evens from 0-19 = {evens}")

# -----------------------------------------------------------------------------
# Method 5: Removing duplicates from a list
# Common use case for sets
# -----------------------------------------------------------------------------
with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(with_duplicates))
print("\n1.5 Removing duplicates:")
print(f"    Original: {with_duplicates}")
print(f"    Unique:   {unique}")


# =============================================================================
# SECTION 2: SET PROPERTIES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: SET PROPERTIES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Sets are unordered - no indexing or slicing
# -----------------------------------------------------------------------------
numbers = {3, 1, 4, 1, 5, 9, 2, 6}
print("\n2.1 Sets are unordered:")
print(f"    {{3,1,4,1,5,9,2,6}} = {numbers}")
print("    Note: Order may vary, duplicates removed")
# print(numbers[0])  # TypeError: 'set' object is not subscriptable

# -----------------------------------------------------------------------------
# Only hashable elements allowed
# -----------------------------------------------------------------------------
print("\n2.2 Only hashable elements allowed:")
valid_set = {1, 'hello', (1, 2, 3)}  # OK: int, str, tuple
print(f"    Valid: {{1, 'hello', (1,2,3)}} = {valid_set}")
# invalid_set = {[1, 2, 3]}  # TypeError: unhashable type: 'list'
print("    Invalid: {[1,2,3]} -> TypeError (lists are unhashable)")

# -----------------------------------------------------------------------------
# Set size and emptiness
# -----------------------------------------------------------------------------
sample = {1, 2, 3, 4, 5}
print("\n2.3 Size and emptiness:")
print(f"    sample = {sample}")
print(f"    len(sample) = {len(sample)}")
print(f"    bool(sample) = {bool(sample)}")
print(f"    bool(set()) = {bool(set())}")  # Empty set is falsy


# =============================================================================
# SECTION 3: ADDING AND REMOVING ELEMENTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: ADDING AND REMOVING ELEMENTS")
print("=" * 60)

colors = {'red', 'green', 'blue'}
print(f"\n    Original: {colors}")

# -----------------------------------------------------------------------------
# add() - Add a single element
# No effect if element already exists
# -----------------------------------------------------------------------------
colors.add('yellow')
print("\n3.1 add('yellow'):")
print(f"    {colors}")

colors.add('red')  # Already exists, no change
print("\n3.2 add('red') - already exists:")
print(f"    {colors}")

# -----------------------------------------------------------------------------
# update() - Add multiple elements from an iterable
# Also called union update or |= operator
# -----------------------------------------------------------------------------
colors.update(['purple', 'orange'])
print("\n3.3 update(['purple', 'orange']):")
print(f"    {colors}")

colors.update({'pink'}, ['cyan'])  # Multiple iterables
print("\n3.4 update with multiple iterables:")
print(f"    {colors}")

# -----------------------------------------------------------------------------
# remove() - Remove element (raises KeyError if not found)
# -----------------------------------------------------------------------------
colors.remove('cyan')
print("\n3.5 remove('cyan'):")
print(f"    {colors}")
# colors.remove('black')  # KeyError: 'black'

# -----------------------------------------------------------------------------
# discard() - Remove element (NO error if not found)
# Safer than remove() when unsure if element exists
# -----------------------------------------------------------------------------
colors.discard('pink')
print("\n3.6 discard('pink'):")
print(f"    {colors}")

colors.discard('black')  # No error even though 'black' doesn't exist
print("\n3.7 discard('black') - not found, no error:")
print(f"    {colors}")

# -----------------------------------------------------------------------------
# pop() - Remove and return arbitrary element
# Raises KeyError if set is empty
# -----------------------------------------------------------------------------
popped = colors.pop()
print("\n3.8 pop() - removes arbitrary element:")
print(f"    Removed: '{popped}', Remaining: {colors}")

# -----------------------------------------------------------------------------
# clear() - Remove all elements
# -----------------------------------------------------------------------------
to_clear = {1, 2, 3}
print(f"\n3.9 clear():")
print(f"    Before: {to_clear}")
to_clear.clear()
print(f"    After:  {to_clear}")


# =============================================================================
# SECTION 4: MEMBERSHIP TESTING
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: MEMBERSHIP TESTING")
print("=" * 60)

# -----------------------------------------------------------------------------
# Sets have O(1) average membership testing - very fast!
# Much faster than lists for large collections
# -----------------------------------------------------------------------------
numbers = {1, 2, 3, 4, 5, 10, 20, 30, 40, 50}
print(f"\n    numbers = {numbers}")

print("\n4.1 Membership testing (in / not in):")
print(f"    5 in numbers = {5 in numbers}")
print(f"    99 in numbers = {99 in numbers}")
print(f"    99 not in numbers = {99 not in numbers}")

# -----------------------------------------------------------------------------
# Performance comparison: set vs list
# -----------------------------------------------------------------------------
print("\n4.2 Performance comparison:")
import time

# Create large collections
large_list = list(range(1000000))
large_set = set(range(1000000))

# Search for element near the end
target = 999999

# Time list search
start = time.perf_counter()
_ = target in large_list
list_time = time.perf_counter() - start

# Time set search
start = time.perf_counter()
_ = target in large_set
set_time = time.perf_counter() - start

print(f"    Searching for {target} in 1,000,000 items:")
print(f"    List: {list_time:.6f} seconds")
print(f"    Set:  {set_time:.6f} seconds")
print(f"    Set is ~{int(list_time/set_time) if set_time > 0 else 'much'}x faster!")


# =============================================================================
# SECTION 5: SET OPERATIONS (MATHEMATICAL)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: SET OPERATIONS (MATHEMATICAL)")
print("=" * 60)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"\n    A = {A}")
print(f"    B = {B}")

# -----------------------------------------------------------------------------
# Union: All elements from both sets
# Method: union() or |
# -----------------------------------------------------------------------------
print("\n5.1 UNION (A ∪ B) - all elements from both:")
print(f"    A.union(B) = {A.union(B)}")
print(f"    A | B = {A | B}")

# -----------------------------------------------------------------------------
# Intersection: Elements common to both sets
# Method: intersection() or &
# -----------------------------------------------------------------------------
print("\n5.2 INTERSECTION (A ∩ B) - common elements:")
print(f"    A.intersection(B) = {A.intersection(B)}")
print(f"    A & B = {A & B}")

# -----------------------------------------------------------------------------
# Difference: Elements in first set but not in second
# Method: difference() or -
# -----------------------------------------------------------------------------
print("\n5.3 DIFFERENCE (A - B) - in A but not in B:")
print(f"    A.difference(B) = {A.difference(B)}")
print(f"    A - B = {A - B}")
print(f"    B - A = {B - A}")  # Different result!

# -----------------------------------------------------------------------------
# Symmetric Difference: Elements in either but not both
# Method: symmetric_difference() or ^
# -----------------------------------------------------------------------------
print("\n5.4 SYMMETRIC DIFFERENCE (A △ B) - in either but not both:")
print(f"    A.symmetric_difference(B) = {A.symmetric_difference(B)}")
print(f"    A ^ B = {A ^ B}")

# -----------------------------------------------------------------------------
# Visual representation
# -----------------------------------------------------------------------------
print("\n5.5 Visual summary:")
print("""
         A = {1,2,3,4,5}     B = {4,5,6,7,8}
         
              ┌─────┐         ┌─────┐
              │ 1 2 │    4    │ 6 7 │
              │  3  │    5    │  8  │
              └─────┘         └─────┘
              
         A | B  = {1,2,3,4,5,6,7,8}  (Union)
         A & B  = {4,5}              (Intersection)
         A - B  = {1,2,3}            (Difference)
         A ^ B  = {1,2,3,6,7,8}      (Symmetric Difference)
""")


# =============================================================================
# SECTION 6: IN-PLACE SET OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: IN-PLACE SET OPERATIONS")
print("=" * 60)

# These methods modify the set in place instead of returning a new set

# -----------------------------------------------------------------------------
# update() / |= : Union in place
# -----------------------------------------------------------------------------
s1 = {1, 2, 3}
s1.update({3, 4, 5})
print("\n6.1 update() / |= (union in place):")
print(f"    {{1,2,3}}.update({{3,4,5}}) = {s1}")

s1 = {1, 2, 3}
s1 |= {3, 4, 5}
print(f"    {{1,2,3}} |= {{3,4,5}} = {s1}")

# -----------------------------------------------------------------------------
# intersection_update() / &= : Intersection in place
# -----------------------------------------------------------------------------
s2 = {1, 2, 3, 4, 5}
s2.intersection_update({3, 4, 5, 6, 7})
print("\n6.2 intersection_update() / &= (intersection in place):")
print(f"    {{1,2,3,4,5}}.intersection_update({{3,4,5,6,7}}) = {s2}")

# -----------------------------------------------------------------------------
# difference_update() / -= : Difference in place
# -----------------------------------------------------------------------------
s3 = {1, 2, 3, 4, 5}
s3.difference_update({3, 4})
print("\n6.3 difference_update() / -= (difference in place):")
print(f"    {{1,2,3,4,5}}.difference_update({{3,4}}) = {s3}")

# -----------------------------------------------------------------------------
# symmetric_difference_update() / ^= : Symmetric difference in place
# -----------------------------------------------------------------------------
s4 = {1, 2, 3, 4, 5}
s4.symmetric_difference_update({4, 5, 6, 7})
print("\n6.4 symmetric_difference_update() / ^= :")
print(f"    {{1,2,3,4,5}}.symmetric_difference_update({{4,5,6,7}}) = {s4}")


# =============================================================================
# SECTION 7: SET COMPARISONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: SET COMPARISONS")
print("=" * 60)

A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
C = {1, 2, 3}
D = {6, 7, 8}

print(f"\n    A = {A}")
print(f"    B = {B}")
print(f"    C = {C}")
print(f"    D = {D}")

# -----------------------------------------------------------------------------
# Subset: All elements of one set are in another
# Method: issubset() or <=
# -----------------------------------------------------------------------------
print("\n7.1 Subset (<=):")
print(f"    B.issubset(A) = {B.issubset(A)}")  # B ⊆ A
print(f"    B <= A = {B <= A}")
print(f"    B < A = {B < A}")  # Proper subset (not equal)
print(f"    B <= C = {B <= C}")  # Equal sets are subsets
print(f"    B < C = {B < C}")  # But not proper subsets

# -----------------------------------------------------------------------------
# Superset: Contains all elements of another set
# Method: issuperset() or >=
# -----------------------------------------------------------------------------
print("\n7.2 Superset (>=):")
print(f"    A.issuperset(B) = {A.issuperset(B)}")  # A ⊇ B
print(f"    A >= B = {A >= B}")
print(f"    A > B = {A > B}")  # Proper superset

# -----------------------------------------------------------------------------
# Disjoint: No common elements
# Method: isdisjoint()
# -----------------------------------------------------------------------------
print("\n7.3 Disjoint (no common elements):")
print(f"    A.isdisjoint(D) = {A.isdisjoint(D)}")
print(f"    A.isdisjoint(B) = {A.isdisjoint(B)}")

# -----------------------------------------------------------------------------
# Equality
# -----------------------------------------------------------------------------
print("\n7.4 Equality:")
print(f"    B == C = {B == C}")
print(f"    A == B = {A == B}")


# =============================================================================
# SECTION 8: FROZEN SETS (IMMUTABLE SETS)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: FROZEN SETS (IMMUTABLE SETS)")
print("=" * 60)

# -----------------------------------------------------------------------------
# frozenset is an immutable version of set
# Can be used as dictionary keys or set elements
# -----------------------------------------------------------------------------

# Creating frozen sets
fs = frozenset([1, 2, 3, 4, 5])
print("\n8.1 Creating frozenset:")
print(f"    frozenset([1,2,3,4,5]) = {fs}")

# Frozen sets support all non-mutating operations
print("\n8.2 Frozenset operations:")
print(f"    3 in fs = {3 in fs}")
print(f"    len(fs) = {len(fs)}")
print(f"    fs | {{6,7}} = {fs | {6, 7}}")  # Returns new frozenset
print(f"    fs & {{3,4,5,6}} = {fs & {3, 4, 5, 6}}")

# Cannot modify frozen sets
print("\n8.3 Frozenset is immutable:")
# fs.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
print("    fs.add(6) -> AttributeError")

# Using frozenset as dictionary key
print("\n8.4 Frozenset as dictionary key:")
permissions = {
    frozenset(['read']): 'viewer',
    frozenset(['read', 'write']): 'editor',
    frozenset(['read', 'write', 'delete']): 'admin',
}
user_perms = frozenset(['read', 'write'])
print(f"    User with {set(user_perms)} is: {permissions[user_perms]}")

# Set of sets (using frozenset)
print("\n8.5 Set of frozensets:")
set_of_sets = {frozenset([1, 2]), frozenset([3, 4]), frozenset([1, 2])}
print(f"    {set_of_sets}")


# =============================================================================
# SECTION 9: ITERATING OVER SETS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: ITERATING OVER SETS")
print("=" * 60)

colors = {'red', 'green', 'blue', 'yellow'}

# -----------------------------------------------------------------------------
# Basic iteration
# -----------------------------------------------------------------------------
print("\n9.1 Basic for loop:")
for color in colors:
    print(f"    {color}")

# -----------------------------------------------------------------------------
# With enumerate (index + value)
# Note: Index doesn't reflect any meaningful order
# -----------------------------------------------------------------------------
print("\n9.2 With enumerate:")
for i, color in enumerate(colors):
    print(f"    {i}: {color}")

# -----------------------------------------------------------------------------
# Sorted iteration
# -----------------------------------------------------------------------------
print("\n9.3 Sorted iteration:")
for color in sorted(colors):
    print(f"    {color}")


# =============================================================================
# SECTION 10: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 10: PRACTICAL EXAMPLES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Example 1: Finding unique words in text
# -----------------------------------------------------------------------------
print("\n10.1 Unique words in text:")
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.lower().split()
unique_words = set(words)
print(f"    Text: '{text}'")
print(f"    Unique words: {unique_words}")
print(f"    Count: {len(unique_words)}")

# -----------------------------------------------------------------------------
# Example 2: Common friends (intersection)
# -----------------------------------------------------------------------------
print("\n10.2 Common friends:")
alice_friends = {'Bob', 'Charlie', 'Diana', 'Eve'}
bob_friends = {'Alice', 'Charlie', 'Frank', 'Diana'}
common = alice_friends & bob_friends
print(f"    Alice's friends: {alice_friends}")
print(f"    Bob's friends: {bob_friends}")
print(f"    Common friends: {common}")

# -----------------------------------------------------------------------------
# Example 3: Permission system
# -----------------------------------------------------------------------------
print("\n10.3 Permission checking:")
required_permissions = {'read', 'write', 'execute'}
user_permissions = {'read', 'write', 'delete'}

has_all = required_permissions <= user_permissions
missing = required_permissions - user_permissions
extra = user_permissions - required_permissions

print(f"    Required: {required_permissions}")
print(f"    User has: {user_permissions}")
print(f"    Has all required? {has_all}")
print(f"    Missing: {missing}")
print(f"    Extra: {extra}")

# -----------------------------------------------------------------------------
# Example 4: Removing duplicates while preserving order
# -----------------------------------------------------------------------------
print("\n10.4 Remove duplicates (preserve order):")
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
seen = set()
unique_ordered = []
for item in data:
    if item not in seen:
        seen.add(item)
        unique_ordered.append(item)
print(f"    Original: {data}")
print(f"    Unique (ordered): {unique_ordered}")

# Alternative using dict.fromkeys (Python 3.7+)
unique_ordered2 = list(dict.fromkeys(data))
print(f"    Using dict.fromkeys: {unique_ordered2}")

# -----------------------------------------------------------------------------
# Example 5: Set-based filtering
# -----------------------------------------------------------------------------
print("\n10.5 Efficient filtering with sets:")
allowed_ids = {101, 102, 103, 104, 105}
requests = [
    {'id': 101, 'action': 'read'},
    {'id': 999, 'action': 'write'},
    {'id': 103, 'action': 'delete'},
    {'id': 888, 'action': 'read'},
]

valid_requests = [r for r in requests if r['id'] in allowed_ids]
print(f"    Allowed IDs: {allowed_ids}")
print(f"    Valid requests: {valid_requests}")


print("\n" + "=" * 60)
print("END OF SETS TUTORIAL")
print("=" * 60)
