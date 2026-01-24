"""
LFU Cache (LeetCode 460)

Problem:
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
- LFUCache(int capacity): Initializes the object with the capacity of the data structure.
- int get(int key): Gets the value of the key if it exists, otherwise returns -1.
- void put(int key, int value): Updates the value of the key if present, or inserts the key
  if not present. When the cache reaches its capacity, it should invalidate and remove the
  least frequently used key before inserting a new item. For this problem, when there is a
  tie (multiple keys with the same frequency), the least recently used key would be evicted.

To determine the least frequently used key, a use counter is maintained for each key.
The key with the smallest use counter is the least frequently used.
When a key is first inserted or get/put, the use counter increases by 1.

The functions get and put must each run in O(1) average time complexity.

Example:
    Input:
    ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    
    Output:
    [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
    
    Explanation:
    - cnt(x) = use counter for key x
    - cache=[] will show last used order (leftmost is most recent)
    
    LFUCache lfu = new LFUCache(2);
    lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
    lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
    lfu.get(1);      // return 1, cache=[1,2], cnt(2)=1, cnt(1)=2
    lfu.put(3, 3);   // 2 is LFU, cache=[3,1], cnt(3)=1, cnt(1)=2
    lfu.get(2);      // return -1 (not found)
    lfu.get(3);      // return 3, cache=[3,1], cnt(3)=2, cnt(1)=2
    lfu.put(4, 4);   // 1 and 3 have same cnt. 1 is LRU, cache=[4,3], cnt(4)=1, cnt(3)=2
    lfu.get(1);      // return -1 (not found)
    lfu.get(3);      // return 3, cache=[3,4], cnt(4)=1, cnt(3)=3
    lfu.get(4);      // return 4, cache=[4,3], cnt(4)=2, cnt(3)=3

Constraints:
    - 1 <= capacity <= 10^4
    - 0 <= key <= 10^5
    - 0 <= value <= 10^9
    - At most 2 * 10^5 calls will be made to get and put.

Approach:
    1. Use three hash maps:
       - key_to_value: Maps key to its value
       - key_to_freq: Maps key to its frequency
       - freq_to_keys: Maps frequency to OrderedDict of keys (for LRU within same freq)
    2. Track minimum frequency to quickly find LFU key
    3. On access, move key from old frequency bucket to new frequency bucket
    4. On eviction, remove LRU key from minimum frequency bucket

Time Complexity: O(1) for both get and put operations
Space Complexity: O(capacity) for storing key-value pairs
"""

from collections import OrderedDict, defaultdict


class DLinkedNode:
    """Doubly linked list node for LFU cache."""
    
    def __init__(self, key: int = 0, value: int = 0):
        """Initialize node with key-value pair."""
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLinkedList:
    """
    Doubly linked list that maintains insertion order.
    Used to track LRU order within a frequency bucket.
    """
    
    def __init__(self):
        """Initialize empty doubly linked list with sentinel nodes."""
        # Dummy head and tail for easier list manipulation
        self._head = DLinkedNode()
        self._tail = DLinkedNode()
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0
    
    def __len__(self) -> int:
        """Return the number of nodes in the list."""
        return self._size
    
    def add_to_head(self, node: DLinkedNode) -> None:
        """Add a node right after the head (most recently used)."""
        node.prev = self._head
        node.next = self._head.next
        self._head.next.prev = node
        self._head.next = node
        self._size += 1
    
    def remove(self, node: DLinkedNode) -> None:
        """Remove a node from the list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
    
    def pop_tail(self) -> DLinkedNode:
        """Remove and return the tail node (least recently used)."""
        if self._size == 0:
            return None
        tail_node = self._tail.prev
        self.remove(tail_node)
        return tail_node


class LFUCache:
    """
    LFU Cache implementation using Hash Maps + Doubly Linked Lists.
    
    Uses three hash maps:
    - _key_to_node: For O(1) node lookup by key
    - _freq_to_list: Maps frequency to DLinkedList of nodes with that frequency
    - Minimum frequency tracking for O(1) eviction
    """
    
    def __init__(self, capacity: int):
        """
        Initialize the LFU cache with given capacity.
        
        Args:
            capacity: Maximum number of items the cache can hold
        """
        self._capacity = capacity
        self._size = 0
        self._min_freq = 0
        
        # Hash map: key -> DLinkedNode
        self._key_to_node = {}
        
        # Hash map: frequency -> DLinkedList of nodes
        self._freq_to_list = defaultdict(DLinkedList)
    
    def _update_frequency(self, node: DLinkedNode) -> None:
        """
        Update the frequency of a node (move it to the next frequency bucket).
        
        Args:
            node: The node whose frequency needs to be updated
        """
        old_freq = node.freq
        new_freq = old_freq + 1
        
        # Remove from old frequency list
        self._freq_to_list[old_freq].remove(node)
        
        # If the old frequency list is empty and it was min_freq, increment min_freq
        if len(self._freq_to_list[old_freq]) == 0:
            del self._freq_to_list[old_freq]
            if self._min_freq == old_freq:
                self._min_freq = new_freq
        
        # Update node's frequency and add to new frequency list
        node.freq = new_freq
        self._freq_to_list[new_freq].add_to_head(node)
    
    def get(self, key: int) -> int:
        """
        Get the value for a key from the cache.
        
        If the key exists, increment its frequency.
        
        Args:
            key: The key to look up
            
        Returns:
            The value if found, -1 otherwise
        """
        if key not in self._key_to_node:
            return -1
        
        node = self._key_to_node[key]
        self._update_frequency(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """
        Add or update a key-value pair in the cache.
        
        If the key exists, update value and increment frequency.
        If it's new and cache is full, evict LFU key (LRU if tie).
        
        Args:
            key: The key to add/update
            value: The value to set
        """
        if self._capacity == 0:
            return
        
        if key in self._key_to_node:
            # Key exists, update value and frequency
            node = self._key_to_node[key]
            node.value = value
            self._update_frequency(node)
        else:
            # New key
            if self._size >= self._capacity:
                # Evict the LFU (and LRU if tied) key
                lfu_list = self._freq_to_list[self._min_freq]
                lfu_node = lfu_list.pop_tail()
                
                if lfu_node:
                    del self._key_to_node[lfu_node.key]
                    self._size -= 1
                    
                    # Clean up empty frequency list
                    if len(lfu_list) == 0:
                        del self._freq_to_list[self._min_freq]
            
            # Create and add new node
            new_node = DLinkedNode(key, value)
            self._key_to_node[key] = new_node
            self._freq_to_list[1].add_to_head(new_node)
            self._min_freq = 1  # New node has frequency 1
            self._size += 1


class LFUCacheSimple:
    """
    Simplified LFU Cache using OrderedDict for each frequency bucket.
    
    This approach is cleaner but relies on Python's OrderedDict
    for maintaining LRU order within each frequency.
    """
    
    def __init__(self, capacity: int):
        """
        Initialize the LFU cache with given capacity.
        
        Args:
            capacity: Maximum number of items the cache can hold
        """
        self._capacity = capacity
        self._min_freq = 0
        
        # key -> (value, frequency)
        self._cache = {}
        
        # frequency -> OrderedDict of keys (maintains LRU order)
        self._freq_to_keys = defaultdict(OrderedDict)
    
    def _update_frequency(self, key: int) -> None:
        """Update key's frequency and move to appropriate bucket."""
        value, freq = self._cache[key]
        
        # Remove from old frequency bucket
        del self._freq_to_keys[freq][key]
        
        # Update min_freq if needed
        if len(self._freq_to_keys[freq]) == 0:
            del self._freq_to_keys[freq]
            if self._min_freq == freq:
                self._min_freq = freq + 1
        
        # Add to new frequency bucket
        new_freq = freq + 1
        self._cache[key] = (value, new_freq)
        self._freq_to_keys[new_freq][key] = None  # Value doesn't matter
    
    def get(self, key: int) -> int:
        """Get value and update frequency."""
        if key not in self._cache:
            return -1
        
        self._update_frequency(key)
        return self._cache[key][0]
    
    def put(self, key: int, value: int) -> None:
        """Put key-value and handle eviction if needed."""
        if self._capacity == 0:
            return
        
        if key in self._cache:
            # Update existing key
            _, freq = self._cache[key]
            self._cache[key] = (value, freq)
            self._update_frequency(key)
        else:
            # Evict if at capacity
            if len(self._cache) >= self._capacity:
                # Get LRU key from LFU bucket (first item in OrderedDict)
                lfu_keys = self._freq_to_keys[self._min_freq]
                evict_key, _ = lfu_keys.popitem(last=False)
                del self._cache[evict_key]
                
                if len(lfu_keys) == 0:
                    del self._freq_to_keys[self._min_freq]
            
            # Add new key
            self._cache[key] = (value, 1)
            self._freq_to_keys[1][key] = None
            self._min_freq = 1


# Test cases to verify the solution
if __name__ == "__main__":
    print("Testing LFUCache (DLinkedList implementation):")
    print("-" * 50)
    
    # Test case from LeetCode example
    lfu = LFUCache(2)
    lfu.put(1, 1)
    print("put(1, 1)")
    
    lfu.put(2, 2)
    print("put(2, 2)")
    
    result = lfu.get(1)
    print(f"get(1) = {result}")  # Expected: 1
    assert result == 1, f"Expected 1, got {result}"
    
    lfu.put(3, 3)  # Evicts key 2 (LFU with freq=1)
    print("put(3, 3) - evicts key 2")
    
    result = lfu.get(2)
    print(f"get(2) = {result}")  # Expected: -1
    assert result == -1, f"Expected -1, got {result}"
    
    result = lfu.get(3)
    print(f"get(3) = {result}")  # Expected: 3
    assert result == 3, f"Expected 3, got {result}"
    
    lfu.put(4, 4)  # Evicts key 1 (LRU among LFU with freq=2)
    print("put(4, 4) - evicts key 1")
    
    result = lfu.get(1)
    print(f"get(1) = {result}")  # Expected: -1
    assert result == -1, f"Expected -1, got {result}"
    
    result = lfu.get(3)
    print(f"get(3) = {result}")  # Expected: 3
    assert result == 3, f"Expected 3, got {result}"
    
    result = lfu.get(4)
    print(f"get(4) = {result}")  # Expected: 4
    assert result == 4, f"Expected 4, got {result}"
    
    print("\nTesting LFUCacheSimple (OrderedDict implementation):")
    print("-" * 50)
    
    lfu2 = LFUCacheSimple(2)
    lfu2.put(1, 1)
    lfu2.put(2, 2)
    
    result = lfu2.get(1)
    print(f"get(1) = {result}")  # Expected: 1
    assert result == 1, f"Expected 1, got {result}"
    
    lfu2.put(3, 3)
    result = lfu2.get(2)
    print(f"get(2) = {result}")  # Expected: -1
    assert result == -1, f"Expected -1, got {result}"
    
    result = lfu2.get(3)
    print(f"get(3) = {result}")  # Expected: 3
    assert result == 3, f"Expected 3, got {result}"
    
    # Test capacity 0
    print("\nTesting capacity 0:")
    lfu3 = LFUCache(0)
    lfu3.put(1, 1)
    result = lfu3.get(1)
    print(f"get(1) = {result}")  # Expected: -1
    assert result == -1, f"Expected -1, got {result}"
    
    # Test single capacity
    print("\nTesting capacity 1:")
    lfu4 = LFUCache(1)
    lfu4.put(1, 1)
    result = lfu4.get(1)
    print(f"get(1) = {result}")  # Expected: 1
    assert result == 1, f"Expected 1, got {result}"
    
    lfu4.put(2, 2)  # Evicts key 1
    result = lfu4.get(1)
    print(f"get(1) after eviction = {result}")  # Expected: -1
    assert result == -1, f"Expected -1, got {result}"
    
    result = lfu4.get(2)
    print(f"get(2) = {result}")  # Expected: 2
    assert result == 2, f"Expected 2, got {result}"
    
    print("\n✅ All test cases passed!")
