"""
=============================================================================
PYTHON HEAPS (heapq module) - COMPREHENSIVE GUIDE
=============================================================================

The heapq module provides an implementation of the min-heap data structure.
Heaps are binary trees where parent nodes have values less than or equal to
their children (min-heap property).

Key Characteristics:
- Min-heap: Smallest element is always at index 0
- O(log n) push and pop operations
- O(n) heapify operation
- O(1) access to minimum element
- Implemented using a list (array-based heap)
=============================================================================
"""

import heapq

# =============================================================================
# SECTION 1: HEAP BASICS
# =============================================================================

print("=" * 60)
print("SECTION 1: HEAP BASICS")
print("=" * 60)

print("""
Heap Property (Min-Heap):
- Parent is always smaller than or equal to children
- Smallest element is at the root (index 0)
- NOT a sorted list, but partially ordered

Heap as Array:
- For element at index i:
  - Left child: 2*i + 1
  - Right child: 2*i + 2
  - Parent: (i-1) // 2

              1 (index 0)
             / \\
            3   2 (index 1, 2)
           / \\
          7   4 (index 3, 4)
          
  Array representation: [1, 3, 2, 7, 4]
""")

# =============================================================================
# SECTION 2: CREATING HEAPS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 2: CREATING HEAPS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Method 1: heapify() - Transform list into heap in-place
# Time Complexity: O(n)
# -----------------------------------------------------------------------------
print("\n2.1 heapify() - Transform list to heap:")
data = [5, 3, 8, 1, 2, 9, 4]
print(f"    Original list: {data}")
heapq.heapify(data)
print(f"    After heapify: {data}")
print(f"    Minimum: {data[0]}")

# -----------------------------------------------------------------------------
# Method 2: Start with empty list and push elements
# Time Complexity: O(n log n) for n elements
# -----------------------------------------------------------------------------
print("\n2.2 Building heap by pushing:")
heap = []
for value in [5, 3, 8, 1, 2]:
    heapq.heappush(heap, value)
    print(f"    Push {value}: {heap}")


# =============================================================================
# SECTION 3: HEAP OPERATIONS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 3: HEAP OPERATIONS")
print("=" * 60)

# -----------------------------------------------------------------------------
# heappush() - Add element to heap
# Time Complexity: O(log n)
# -----------------------------------------------------------------------------
print("\n3.1 heappush():")
heap = [1, 3, 5, 7]
print(f"    Before: {heap}")
heapq.heappush(heap, 2)
print(f"    After heappush(2): {heap}")

# -----------------------------------------------------------------------------
# heappop() - Remove and return smallest element
# Time Complexity: O(log n)
# -----------------------------------------------------------------------------
print("\n3.2 heappop():")
heap = [1, 3, 2, 7, 4]
print(f"    Before: {heap}")
smallest = heapq.heappop(heap)
print(f"    heappop() returned: {smallest}")
print(f"    After: {heap}")

# -----------------------------------------------------------------------------
# heappushpop() - Push then pop (more efficient than separate operations)
# Time Complexity: O(log n)
# -----------------------------------------------------------------------------
print("\n3.3 heappushpop():")
heap = [1, 3, 5, 7]
print(f"    Before: {heap}")
result = heapq.heappushpop(heap, 2)
print(f"    heappushpop(2) returned: {result}")
print(f"    After: {heap}")

# -----------------------------------------------------------------------------
# heapreplace() - Pop then push (more efficient than separate operations)
# Time Complexity: O(log n)
# -----------------------------------------------------------------------------
print("\n3.4 heapreplace():")
heap = [1, 3, 5, 7]
print(f"    Before: {heap}")
result = heapq.heapreplace(heap, 4)
print(f"    heapreplace(4) returned: {result}")
print(f"    After: {heap}")

print("\n3.5 Difference between heappushpop and heapreplace:")
print("""
    heappushpop(heap, item):
        - Push item first, then pop smallest
        - If item is smallest, returns item (never added to heap)
        
    heapreplace(heap, item):
        - Pop smallest first, then push item
        - Always returns original minimum
        - Raises IndexError if heap is empty
""")


# =============================================================================
# SECTION 4: FINDING N LARGEST/SMALLEST
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 4: FINDING N LARGEST/SMALLEST")
print("=" * 60)

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"\n    data = {data}")

# -----------------------------------------------------------------------------
# nlargest() and nsmallest()
# Time Complexity: O(n log k) where k is number of elements requested
# -----------------------------------------------------------------------------
print("\n4.1 nlargest() and nsmallest():")
print(f"    3 largest: {heapq.nlargest(3, data)}")
print(f"    3 smallest: {heapq.nsmallest(3, data)}")

# -----------------------------------------------------------------------------
# With key function
# -----------------------------------------------------------------------------
print("\n4.2 With key function:")
students = [
    {'name': 'Alice', 'grade': 88},
    {'name': 'Bob', 'grade': 95},
    {'name': 'Charlie', 'grade': 72},
    {'name': 'Diana', 'grade': 91},
]

top_2 = heapq.nlargest(2, students, key=lambda s: s['grade'])
bottom_2 = heapq.nsmallest(2, students, key=lambda s: s['grade'])

print(f"    Top 2 students: {[s['name'] for s in top_2]}")
print(f"    Bottom 2 students: {[s['name'] for s in bottom_2]}")

# -----------------------------------------------------------------------------
# When to use nlargest/nsmallest vs sorting
# -----------------------------------------------------------------------------
print("\n4.3 Efficiency guidelines:")
print("""
    For finding k elements from n elements:
    
    - k = 1: Use min() or max() - O(n)
    - k is small: Use nlargest/nsmallest - O(n log k)
    - k is close to n: Use sorted() with slicing - O(n log n)
    - Need all elements: Use sorted() - O(n log n)
""")


# =============================================================================
# SECTION 5: MAX-HEAP (USING NEGATION)
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 5: MAX-HEAP (USING NEGATION)")
print("=" * 60)

print("""
Python's heapq only provides min-heap.
For max-heap behavior, negate values when pushing/popping.
""")

# -----------------------------------------------------------------------------
# Max-heap implementation
# -----------------------------------------------------------------------------
print("\n5.1 Max-heap using negation:")

class MaxHeap:
    """Wrapper class for max-heap behavior."""
    
    def __init__(self):
        self._heap = []
    
    def push(self, value):
        heapq.heappush(self._heap, -value)
    
    def pop(self):
        return -heapq.heappop(self._heap)
    
    def peek(self):
        return -self._heap[0] if self._heap else None
    
    def __len__(self):
        return len(self._heap)
    
    def __repr__(self):
        return f"MaxHeap({[-x for x in self._heap]})"

max_heap = MaxHeap()
for val in [3, 1, 4, 1, 5, 9, 2, 6]:
    max_heap.push(val)
    print(f"    Push {val}: max = {max_heap.peek()}")

print(f"\n    Popping in order:")
while max_heap:
    print(f"    {max_heap.pop()}", end=" ")
print()

# -----------------------------------------------------------------------------
# Inline max-heap usage
# -----------------------------------------------------------------------------
print("\n5.2 Inline max-heap (without wrapper):")
data = [3, 1, 4, 1, 5, 9, 2, 6]
max_heap = [-x for x in data]
heapq.heapify(max_heap)
print(f"    Data: {data}")
print(f"    Max element: {-max_heap[0]}")


# =============================================================================
# SECTION 6: HEAP WITH CUSTOM OBJECTS
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 6: HEAP WITH CUSTOM OBJECTS")
print("=" * 60)

# -----------------------------------------------------------------------------
# Method 1: Using tuples (priority, data)
# Priority value is compared first
# -----------------------------------------------------------------------------
print("\n6.1 Tuple approach (priority, data):")
tasks = []
heapq.heappush(tasks, (2, "Medium priority task"))
heapq.heappush(tasks, (1, "High priority task"))
heapq.heappush(tasks, (3, "Low priority task"))

print("    Processing tasks by priority:")
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"    Priority {priority}: {task}")

# -----------------------------------------------------------------------------
# Method 2: Using tuples with tie-breaker
# When priorities are equal, a counter ensures stability
# -----------------------------------------------------------------------------
print("\n6.2 With tie-breaker counter:")

class PriorityQueue:
    """Priority queue with FIFO ordering for equal priorities."""
    
    def __init__(self):
        self._heap = []
        self._counter = 0  # Tie-breaker for equal priorities
    
    def push(self, item, priority):
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1
    
    def pop(self):
        if self._heap:
            priority, _, item = heapq.heappop(self._heap)
            return item
        raise IndexError("pop from empty priority queue")
    
    def __bool__(self):
        return bool(self._heap)

pq = PriorityQueue()
pq.push("Task A", 1)
pq.push("Task B", 1)  # Same priority as A
pq.push("Task C", 2)

print("    Tasks with same priority maintain FIFO order:")
while pq:
    print(f"    {pq.pop()}")

# -----------------------------------------------------------------------------
# Method 3: Using dataclass with comparison
# -----------------------------------------------------------------------------
print("\n6.3 Using dataclass with __lt__:")
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Task:
    priority: int
    name: str = field(compare=False)  # Don't compare by name
    
task_heap = []
heapq.heappush(task_heap, Task(2, "Write tests"))
heapq.heappush(task_heap, Task(1, "Fix bug"))
heapq.heappush(task_heap, Task(3, "Deploy"))

print("    Tasks from dataclass heap:")
while task_heap:
    task = heapq.heappop(task_heap)
    print(f"    Priority {task.priority}: {task.name}")


# =============================================================================
# SECTION 7: HEAP SORT
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 7: HEAP SORT")
print("=" * 60)

# -----------------------------------------------------------------------------
# Heap sort implementation
# Time Complexity: O(n log n)
# Not in-place when using heapq
# -----------------------------------------------------------------------------
print("\n7.1 Heap sort implementation:")

def heap_sort(iterable):
    """Sort using heap. Returns new sorted list."""
    h = list(iterable)
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(h))]

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_data = heap_sort(data)
print(f"    Original: {data}")
print(f"    Sorted:   {sorted_data}")

# -----------------------------------------------------------------------------
# Comparison with built-in sort
# -----------------------------------------------------------------------------
print("\n7.2 Comparison with built-in sort:")
print("""
    Method          Time        Space       Stable?
    ------------------------------------------------
    heapsort        O(n log n)  O(n)        No
    sorted()        O(n log n)  O(n)        Yes
    list.sort()     O(n log n)  O(1)        Yes
    
    Note: Python's built-in sort (Timsort) is usually faster in practice.
""")


# =============================================================================
# SECTION 8: MERGING SORTED ITERABLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 8: MERGING SORTED ITERABLES")
print("=" * 60)

# -----------------------------------------------------------------------------
# heapq.merge() - Merge multiple sorted inputs into single sorted output
# Time Complexity: O(n log k) where k is number of iterables
# Returns iterator (lazy evaluation)
# -----------------------------------------------------------------------------
print("\n8.1 merge() - Merge sorted iterables:")
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = [0, 5, 10, 15]

merged = list(heapq.merge(list1, list2, list3))
print(f"    list1: {list1}")
print(f"    list2: {list2}")
print(f"    list3: {list3}")
print(f"    merged: {merged}")

# -----------------------------------------------------------------------------
# merge() with key function
# -----------------------------------------------------------------------------
print("\n8.2 merge() with key function:")
names1 = ["alice", "charlie", "eve"]
names2 = ["bob", "diana", "frank"]

merged_names = list(heapq.merge(names1, names2, key=str.lower))
print(f"    Merged alphabetically: {merged_names}")

# -----------------------------------------------------------------------------
# Practical example - External sort / K-way merge
# -----------------------------------------------------------------------------
print("\n8.3 Practical example - K-way merge of files:")
print("""
    # Simulated: merging multiple sorted files
    files = [
        open('sorted1.txt'),  # Each file is sorted
        open('sorted2.txt'),
        open('sorted3.txt'),
    ]
    
    # Merge all files efficiently
    for line in heapq.merge(*files):
        process(line)
    
    # Time: O(n log k) where n = total lines, k = number of files
""")


# =============================================================================
# SECTION 9: PRACTICAL EXAMPLES
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 9: PRACTICAL EXAMPLES")
print("=" * 60)

# -----------------------------------------------------------------------------
# Example 1: Running Median
# -----------------------------------------------------------------------------
print("\n9.1 Running Median (using two heaps):")

class RunningMedian:
    """Maintain running median using max-heap and min-heap."""
    
    def __init__(self):
        self.low = []   # Max-heap (negated) for lower half
        self.high = []  # Min-heap for upper half
    
    def add(self, num):
        # Add to low (max-heap)
        heapq.heappush(self.low, -num)
        
        # Balance: largest of low should be <= smallest of high
        if self.low and self.high and (-self.low[0] > self.high[0]):
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        
        # Balance sizes: low can have at most 1 more element
        if len(self.low) > len(self.high) + 1:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        elif len(self.high) > len(self.low):
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)
    
    def get_median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2

rm = RunningMedian()
stream = [2, 1, 5, 7, 2, 0, 5]
print(f"    Stream: {stream}")
print("    Running medians:")
for num in stream:
    rm.add(num)
    print(f"    Add {num}: median = {rm.get_median()}")

# -----------------------------------------------------------------------------
# Example 2: K Closest Points
# -----------------------------------------------------------------------------
print("\n9.2 K Closest Points to Origin:")

def k_closest(points, k):
    """Find k closest points to origin (0, 0)."""
    # Use max-heap of size k (negate distances)
    # This gives us the k smallest distances
    return heapq.nsmallest(
        k, 
        points, 
        key=lambda p: p[0]**2 + p[1]**2
    )

points = [(1, 3), (-2, 2), (5, 8), (0, 1), (3, 3)]
closest = k_closest(points, 3)
print(f"    Points: {points}")
print(f"    3 closest to origin: {closest}")

# -----------------------------------------------------------------------------
# Example 3: Task Scheduler
# -----------------------------------------------------------------------------
print("\n9.3 Simplified Task Scheduler:")

def schedule_tasks(tasks, cooldown):
    """
    Schedule tasks with cooldown period between same tasks.
    Returns total time units needed.
    """
    from collections import Counter
    
    count = Counter(tasks)
    max_heap = [-c for c in count.values()]
    heapq.heapify(max_heap)
    
    time = 0
    while max_heap:
        cycle = []
        for _ in range(cooldown + 1):
            if max_heap:
                count = heapq.heappop(max_heap)
                if count < -1:  # More instances remaining
                    cycle.append(count + 1)
            time += 1
            
            if not max_heap and not cycle:
                break
        
        for c in cycle:
            heapq.heappush(max_heap, c)
    
    return time

tasks = ['A', 'A', 'A', 'B', 'B', 'B']
cooldown = 2
total_time = schedule_tasks(tasks, cooldown)
print(f"    Tasks: {tasks}, Cooldown: {cooldown}")
print(f"    Total time: {total_time}")

# -----------------------------------------------------------------------------
# Example 4: Merge K Sorted Lists (LeetCode classic)
# -----------------------------------------------------------------------------
print("\n9.4 Merge K Sorted Lists:")

def merge_k_lists(lists):
    """Merge k sorted lists into one sorted list."""
    result = []
    heap = []  # (value, list_index, element_index)
    
    # Initialize heap with first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # If more elements in this list, add next one
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged = merge_k_lists(lists)
print(f"    Lists: {lists}")
print(f"    Merged: {merged}")


# =============================================================================
# SECTION 10: TIME COMPLEXITY SUMMARY
# =============================================================================

print("\n" + "=" * 60)
print("SECTION 10: TIME COMPLEXITY SUMMARY")
print("=" * 60)

print("""
HEAP OPERATIONS TIME COMPLEXITY:

Operation           Time Complexity    Description
-----------------------------------------------------------------
heapify(list)       O(n)              Transform list into heap
heappush(heap, x)   O(log n)          Add element to heap
heappop(heap)       O(log n)          Remove and return smallest
heappushpop(h, x)   O(log n)          Push then pop (optimized)
heapreplace(h, x)   O(log n)          Pop then push (optimized)
heap[0]             O(1)              Access smallest element
nlargest(k, iter)   O(n log k)        Find k largest elements
nsmallest(k, iter)  O(n log k)        Find k smallest elements
merge(*iters)       O(n log k)        Merge k sorted iterables

WHEN TO USE HEAPS:

✅ Use heaps when:
  - You need the min/max element frequently
  - Priority queue implementation
  - Finding k largest/smallest elements
  - Merging sorted streams
  - Event-driven simulation

❌ Don't use heaps when:
  - You need to search for arbitrary elements
  - You need to delete arbitrary elements
  - You need the data fully sorted
  - Random access by index is required
""")


print("\n" + "=" * 60)
print("END OF HEAPS TUTORIAL")
print("=" * 60)
