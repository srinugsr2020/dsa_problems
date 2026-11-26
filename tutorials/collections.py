"""
=============================================================================
PYTHON COLLECTIONS MODULE - COMPREHENSIVE GUIDE
=============================================================================

The collections module provides specialized container data types that extend
the built-in containers (dict, list, set, tuple) with additional functionality.

Key Classes Covered:
- namedtuple: Tuple subclass with named fields
- deque: Double-ended queue with O(1) append/pop from both ends
- Counter: Dict subclass for counting hashable objects
- OrderedDict: Dict that remembers insertion order (less needed in Python 3.7+)
- defaultdict: Dict with default factory for missing keys
- ChainMap: Single view of multiple dictionaries
=============================================================================
"""

from collections import namedtuple, deque, Counter, OrderedDict, defaultdict, ChainMap

# =============================================================================
# SECTION 1: NAMEDTUPLE
# =============================================================================

print("=" * 60)
print("SECTION 1: NAMEDTUPLE")
print("=" * 60)

print("""
namedtuple creates tuple subclasses with named fields.
- Immutable like regular tuples
- Accessible by name AND index
- Memory efficient (no __dict__)
- Self-documenting code
""")

# -----------------------------------------------------------------------------
# Creating namedtuple classes
# -----------------------------------------------------------------------------
# Method 1: List of field names
Point = namedtuple('Point', ['x', 'y'])
# Method 2: Space-separated string
Person = namedtuple('Person', 'name age city')
# Method 3: Comma-separated string
Color = namedtuple('Color', 'red, green, blue')

print("1.1 Creating instances:")
p1 = Point(10, 20)
p2 = Point(x=30, y=40)
alice = Person('Alice', 30, 'NYC')
red = Color(255, 0, 0)

print(f"    Point(10, 20) = {p1}")
print(f"    Point(x=30, y=40) = {p2}")
print(f"    Person('Alice', 30, 'NYC') = {alice}")

# -----------------------------------------------------------------------------
# Accessing fields
# -----------------------------------------------------------------------------
print("\n1.2 Accessing fields (by name AND index):")
print(f"    p1.x = {p1.x}, p1[0] = {p1[0]}")
print(f"    alice.name = {alice.name}, alice.age = {alice.age}")

# -----------------------------------------------------------------------------
# namedtuple methods
# -----------------------------------------------------------------------------
print("\n1.3 namedtuple methods:")
print(f"    alice._fields = {alice._fields}")
print(f"    alice._asdict() = {alice._asdict()}")

# _replace creates new instance with modified values
bob = alice._replace(name='Bob', age=25)
print(f"    alice._replace(name='Bob', age=25) = {bob}")

# _make creates instance from iterable
data = ['Charlie', 35, 'LA']
charlie = Person._make(data)
print(f"    Person._make(['Charlie', 35, 'LA']) = {charlie}")

# -----------------------------------------------------------------------------
# Default values (Python 3.7+)
# -----------------------------------------------------------------------------
print("\n1.4 Default values:")
Employee = namedtuple('Employee', ['name', 'dept', 'salary'], defaults=['Unknown', 50000])
emp1 = Employee('John')
emp2 = Employee('Jane', 'Engineering', 75000)
print(f"    Employee('John') = {emp1}")
print(f"    Employee('Jane', 'Engineering', 75000) = {emp2}")

# -----------------------------------------------------------------------------
# Practical example
# -----------------------------------------------------------------------------
print("\n1.5 Practical example - Database records:")
Book = namedtuple('Book', 'title author year isbn')
books = [
    Book('1984', 'George Orwell', 1949, '978-0451524935'),
    Book('Brave New World', 'Aldous Huxley', 1932, '978-0060850524'),
    Book('Fahrenheit 451', 'Ray Bradbury', 1953, '978-1451673319'),
]
print("    Books published before 1950:")
for book in books:
    if book.year < 1950:
        print(f"    - {book.title} by {book.author} ({book.year})")


# =============================================================================
# SECTION 2: DEQUE (DOUBLE-ENDED QUEUE)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: DEQUE (DOUBLE-ENDED QUEUE)")
print("=" * 60)

print("""
deque provides O(1) append and pop from both ends.
- Faster than list for left-side operations
- Thread-safe append and pop
- Optional maxlen for bounded deques
- Great for queues, stacks, and sliding windows
""")

# -----------------------------------------------------------------------------
# Creating deques
# -----------------------------------------------------------------------------
print("\n2.1 Creating deques:")
dq = deque([1, 2, 3, 4, 5])
print(f"    deque([1,2,3,4,5]) = {dq}")

empty = deque()
from_string = deque('hello')
print(f"    deque('hello') = {from_string}")

# Bounded deque (fixed max size)
bounded = deque([1, 2, 3], maxlen=5)
print(f"    deque([1,2,3], maxlen=5) = {bounded}")

# -----------------------------------------------------------------------------
# Adding elements
# -----------------------------------------------------------------------------
print("\n2.2 Adding elements:")
dq = deque([2, 3, 4])
print(f"    Original: {dq}")

dq.append(5)        # Add to right
print(f"    append(5): {dq}")

dq.appendleft(1)    # Add to left
print(f"    appendleft(1): {dq}")

dq.extend([6, 7])   # Extend right
print(f"    extend([6,7]): {dq}")

dq.extendleft([0, -1])  # Extend left (note: reversed order!)
print(f"    extendleft([0,-1]): {dq}")

# -----------------------------------------------------------------------------
# Removing elements
# -----------------------------------------------------------------------------
print("\n2.3 Removing elements:")
dq = deque([1, 2, 3, 4, 5])
print(f"    Original: {dq}")

right = dq.pop()
print(f"    pop() returned {right}: {dq}")

left = dq.popleft()
print(f"    popleft() returned {left}: {dq}")

dq.remove(3)  # Remove first occurrence
print(f"    remove(3): {dq}")

# -----------------------------------------------------------------------------
# Rotation
# -----------------------------------------------------------------------------
print("\n2.4 Rotation:")
dq = deque([1, 2, 3, 4, 5])
print(f"    Original: {dq}")

dq.rotate(2)  # Rotate right by 2
print(f"    rotate(2): {dq}")

dq.rotate(-2)  # Rotate left by 2
print(f"    rotate(-2): {dq}")

# -----------------------------------------------------------------------------
# Bounded deque behavior
# -----------------------------------------------------------------------------
print("\n2.5 Bounded deque (automatic discard):")
bounded = deque([1, 2, 3], maxlen=5)
print(f"    deque([1,2,3], maxlen=5): {bounded}")

bounded.extend([4, 5, 6, 7])  # Exceeds maxlen
print(f"    extend([4,5,6,7]): {bounded}")
print("    (Left elements automatically discarded)")

# -----------------------------------------------------------------------------
# Practical example - Sliding window
# -----------------------------------------------------------------------------
print("\n2.6 Practical example - Sliding window max:")
def sliding_window_max(nums, k):
    """Find max in each sliding window of size k."""
    result = []
    window = deque()  # Stores indices
    
    for i, num in enumerate(nums):
        # Remove elements outside window
        while window and window[0] < i - k + 1:
            window.popleft()
        
        # Remove smaller elements (won't be max)
        while window and nums[window[-1]] < num:
            window.pop()
        
        window.append(i)
        
        # Window is full, record max
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
print(f"    nums = {nums}, k = 3")
print(f"    Sliding max: {sliding_window_max(nums, 3)}")


# =============================================================================
# SECTION 3: COUNTER
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: COUNTER")
print("=" * 60)

print("""
Counter is a dict subclass for counting hashable objects.
- Counts occurrences automatically
- Supports arithmetic operations (+, -, &, |)
- Easy access to most common elements
- Missing keys return 0 (not KeyError)
""")

# -----------------------------------------------------------------------------
# Creating Counters
# -----------------------------------------------------------------------------
print("\n3.1 Creating Counters:")
# From iterable
c1 = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(f"    Counter(['a','b','c','a','b','a']) = {c1}")

# From string
c2 = Counter('mississippi')
print(f"    Counter('mississippi') = {c2}")

# From keyword arguments
c3 = Counter(cats=4, dogs=2, birds=1)
print(f"    Counter(cats=4, dogs=2, birds=1) = {c3}")

# From dict
c4 = Counter({'red': 3, 'blue': 2})
print(f"    Counter({{'red': 3, 'blue': 2}}) = {c4}")

# -----------------------------------------------------------------------------
# Accessing counts
# -----------------------------------------------------------------------------
print("\n3.2 Accessing counts:")
c = Counter('abracadabra')
print(f"    Counter('abracadabra') = {c}")
print(f"    c['a'] = {c['a']}")
print(f"    c['z'] = {c['z']}")  # Missing key returns 0

# -----------------------------------------------------------------------------
# most_common()
# -----------------------------------------------------------------------------
print("\n3.3 most_common():")
print(f"    c.most_common() = {c.most_common()}")
print(f"    c.most_common(2) = {c.most_common(2)}")

# -----------------------------------------------------------------------------
# elements() - iterator over elements
# -----------------------------------------------------------------------------
print("\n3.4 elements():")
c = Counter(a=3, b=2, c=1)
print(f"    Counter(a=3, b=2, c=1).elements() = {list(c.elements())}")

# -----------------------------------------------------------------------------
# Updating counters
# -----------------------------------------------------------------------------
print("\n3.5 Updating counters:")
c = Counter(a=3, b=1)
print(f"    Original: {c}")

c.update({'a': 1, 'b': 2, 'c': 3})  # Add counts
print(f"    update({{'a':1,'b':2,'c':3}}): {c}")

c.subtract({'a': 2, 'b': 1})  # Subtract counts
print(f"    subtract({{'a':2,'b':1}}): {c}")

# -----------------------------------------------------------------------------
# Arithmetic operations
# -----------------------------------------------------------------------------
print("\n3.6 Arithmetic operations:")
c1 = Counter(a=3, b=1, c=2)
c2 = Counter(a=1, b=2, d=1)
print(f"    c1 = {c1}")
print(f"    c2 = {c2}")

print(f"    c1 + c2 = {c1 + c2}")  # Add (combines counts)
print(f"    c1 - c2 = {c1 - c2}")  # Subtract (keeps positive)
print(f"    c1 & c2 = {c1 & c2}")  # Intersection (min)
print(f"    c1 | c2 = {c1 | c2}")  # Union (max)

# -----------------------------------------------------------------------------
# Practical example - Word frequency
# -----------------------------------------------------------------------------
print("\n3.7 Practical example - Word frequency:")
text = """The quick brown fox jumps over the lazy dog.
The dog was not amused. The fox was quick."""

words = text.lower().replace('.', '').split()
word_freq = Counter(words)

print(f"    Top 5 words: {word_freq.most_common(5)}")
print(f"    Total words: {sum(word_freq.values())}")
print(f"    Unique words: {len(word_freq)}")


# =============================================================================
# SECTION 4: DEFAULTDICT
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: DEFAULTDICT")
print("=" * 60)

print("""
defaultdict is a dict subclass with a default factory for missing keys.
- Never raises KeyError for missing keys
- Automatically creates default values
- Cleaner code for grouping, counting, and accumulating
""")

# -----------------------------------------------------------------------------
# Creating defaultdicts
# -----------------------------------------------------------------------------
print("\n4.1 Creating defaultdicts:")

# With list factory
dd_list = defaultdict(list)
dd_list['a'].append(1)
dd_list['a'].append(2)
dd_list['b'].append(3)
print(f"    defaultdict(list): {dict(dd_list)}")

# With int factory (default 0)
dd_int = defaultdict(int)
dd_int['count'] += 1
dd_int['count'] += 1
print(f"    defaultdict(int): {dict(dd_int)}")

# With set factory
dd_set = defaultdict(set)
dd_set['vowels'].add('a')
dd_set['vowels'].add('e')
print(f"    defaultdict(set): {dict(dd_set)}")

# With lambda for custom default
dd_lambda = defaultdict(lambda: 'Unknown')
dd_lambda['name'] = 'Alice'
print(f"    defaultdict(lambda: 'Unknown'): name={dd_lambda['name']}, city={dd_lambda['city']}")

# -----------------------------------------------------------------------------
# Comparison with regular dict
# -----------------------------------------------------------------------------
print("\n4.2 Comparison with regular dict:")
print("""
    Regular dict (verbose):        defaultdict (clean):
    
    if key not in d:               d = defaultdict(list)
        d[key] = []                d[key].append(value)
    d[key].append(value)
""")

# -----------------------------------------------------------------------------
# Practical example - Grouping
# -----------------------------------------------------------------------------
print("\n4.3 Practical example - Grouping by first letter:")
words = ['apple', 'banana', 'avocado', 'blueberry', 'cherry', 'apricot']
grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)

print(f"    Words: {words}")
print(f"    Grouped by first letter:")
for letter, word_list in sorted(grouped.items()):
    print(f"        {letter}: {word_list}")

# -----------------------------------------------------------------------------
# Practical example - Counting with nested dict
# -----------------------------------------------------------------------------
print("\n4.4 Practical example - Nested defaultdict:")
# Count occurrences of characters per word
def nested_dict():
    return defaultdict(int)

word_char_count = defaultdict(nested_dict)
words = ['hello', 'world', 'hello']

for word in words:
    for char in word:
        word_char_count[word][char] += 1

print(f"    Character counts per word:")
for word, counts in word_char_count.items():
    print(f"        {word}: {dict(counts)}")


# =============================================================================
# SECTION 5: ORDEREDDICT
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: ORDEREDDICT")
print("=" * 60)

print("""
OrderedDict remembers the order in which items were added.
- In Python 3.7+, regular dict also maintains order
- OrderedDict still useful for:
  - move_to_end() method
  - Order-sensitive equality comparisons
  - Explicit documentation of order importance
""")

# -----------------------------------------------------------------------------
# Creating OrderedDict
# -----------------------------------------------------------------------------
print("\n5.1 Creating OrderedDict:")
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"    OrderedDict([('a',1),('b',2),('c',3)]) = {od}")

# -----------------------------------------------------------------------------
# move_to_end()
# -----------------------------------------------------------------------------
print("\n5.2 move_to_end():")
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"    Original: {od}")

od.move_to_end('a')
print(f"    move_to_end('a'): {od}")

od.move_to_end('c', last=False)  # Move to beginning
print(f"    move_to_end('c', last=False): {od}")

# -----------------------------------------------------------------------------
# Order-sensitive equality
# -----------------------------------------------------------------------------
print("\n5.3 Order-sensitive equality:")
od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}

print(f"    OrderedDict comparison: od1 == od2 = {od1 == od2}")
print(f"    Regular dict comparison: d1 == d2 = {d1 == d2}")

# -----------------------------------------------------------------------------
# Practical example - LRU Cache
# -----------------------------------------------------------------------------
print("\n5.4 Practical example - Simple LRU Cache:")

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove oldest

lru = LRUCache(3)
lru.put('a', 1)
lru.put('b', 2)
lru.put('c', 3)
print(f"    After put a,b,c: {dict(lru.cache)}")

lru.get('a')  # Access 'a', moves to end
print(f"    After get('a'): {dict(lru.cache)}")

lru.put('d', 4)  # Exceeds capacity, removes 'b'
print(f"    After put('d'): {dict(lru.cache)}")


# =============================================================================
# SECTION 6: CHAINMAP
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: CHAINMAP")
print("=" * 60)

print("""
ChainMap groups multiple dicts into a single view.
- Searches dicts in order (first found wins)
- Updates/inserts go to the first dict only
- Useful for layered configurations
- No data copying (views the original dicts)
""")

# -----------------------------------------------------------------------------
# Creating ChainMap
# -----------------------------------------------------------------------------
print("\n6.1 Creating ChainMap:")
defaults = {'color': 'blue', 'size': 'medium', 'font': 'Arial'}
user_prefs = {'color': 'red'}
session = {'size': 'large'}

config = ChainMap(session, user_prefs, defaults)
print(f"    defaults = {defaults}")
print(f"    user_prefs = {user_prefs}")
print(f"    session = {session}")
print(f"    ChainMap result:")
print(f"        color = {config['color']}")   # From user_prefs
print(f"        size = {config['size']}")     # From session
print(f"        font = {config['font']}")     # From defaults

# -----------------------------------------------------------------------------
# ChainMap properties
# -----------------------------------------------------------------------------
print("\n6.2 ChainMap properties:")
print(f"    config.maps = {config.maps}")
print(f"    list(config) = {list(config)}")

# -----------------------------------------------------------------------------
# Modifying ChainMap
# -----------------------------------------------------------------------------
print("\n6.3 Modifying ChainMap:")
config['theme'] = 'dark'  # Goes to first dict (session)
print(f"    After config['theme'] = 'dark':")
print(f"    session = {session}")

# -----------------------------------------------------------------------------
# new_child() - add a new layer
# -----------------------------------------------------------------------------
print("\n6.4 new_child():")
temp_settings = config.new_child({'debug': True})
print(f"    temp_settings['debug'] = {temp_settings['debug']}")
print(f"    temp_settings['color'] = {temp_settings['color']}")  # Still works

# -----------------------------------------------------------------------------
# parents - all maps except first
# -----------------------------------------------------------------------------
print("\n6.5 parents property:")
print(f"    config.parents = {config.parents}")

# -----------------------------------------------------------------------------
# Practical example - Configuration layers
# -----------------------------------------------------------------------------
print("\n6.6 Practical example - Configuration layers:")

def get_config():
    # Simulated configuration sources
    system_defaults = {
        'debug': False,
        'log_level': 'WARNING',
        'max_connections': 100,
    }
    
    config_file = {
        'log_level': 'INFO',
        'database': 'prod_db',
    }
    
    env_vars = {
        'debug': True,  # Override for development
    }
    
    # Most specific first
    return ChainMap(env_vars, config_file, system_defaults)

app_config = get_config()
print("    Configuration (priority: env > file > defaults):")
for key in ['debug', 'log_level', 'max_connections', 'database']:
    print(f"        {key} = {app_config[key]}")


# =============================================================================
# SECTION 7: SUMMARY AND WHEN TO USE
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: SUMMARY AND WHEN TO USE")
print("=" * 60)

print("""
WHEN TO USE EACH:

namedtuple:
  - Fixed record structures (like database rows)
  - Returning multiple values from functions
  - When you need named access to tuple elements
  - When immutability is desired

deque:
  - Queue implementations (FIFO)
  - Stack implementations (LIFO)
  - Sliding window problems
  - When you need O(1) append/pop from both ends
  - Bounded collections with automatic discard

Counter:
  - Counting occurrences of items
  - Finding most common elements
  - Multiset operations
  - Histogram / frequency analysis

defaultdict:
  - Grouping items by key
  - Counting with automatic initialization
  - Building nested structures
  - When you want to avoid KeyError

OrderedDict:
  - When you need move_to_end()
  - When order-sensitive equality matters
  - LRU cache implementations
  - When you want to document that order matters

ChainMap:
  - Layered configuration (defaults, user, session)
  - Scope chains (local, global, builtin)
  - When you need a unified view of multiple dicts
  - When you don't want to merge dicts (preserve originals)
""")


print("\n" + "=" * 60)
print("END OF COLLECTIONS MODULE TUTORIAL")
print("=" * 60)
