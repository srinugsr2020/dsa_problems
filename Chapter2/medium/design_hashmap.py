"""
Design HashMap Problem

Problem Statement:
------------------
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:
- MyHashMap() initializes the object with an empty map
- put(key, value) inserts a (key, value) pair. If the key already exists, update the value
- get(key) returns the value mapped to key, or -1 if key doesn't exist
- remove(key) removes the key and its value if it exists

Constraints:
------------
- 0 <= key, value <= 10^6
- At most 10^4 calls will be made to put, get, and remove

Examples:
---------
Example 1:
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)      # map is now [[1,1]]
    myHashMap.put(2, 2)      # map is now [[1,1], [2,2]]
    myHashMap.get(1)         # returns 1
    myHashMap.get(3)         # returns -1 (not found)
    myHashMap.put(2, 1)      # update value, map is now [[1,1], [2,1]]
    myHashMap.get(2)         # returns 1
    myHashMap.remove(2)      # remove key 2, map is now [[1,1]]
    myHashMap.get(2)         # returns -1 (not found)

Hints:
------
1. Use an array of buckets (separate chaining for collision handling)
2. Hash function: key % bucket_size
3. Each bucket can be a linked list or a list of (key, value) pairs
4. Choose bucket size as a prime number to reduce collisions

Design Considerations:
- How to handle hash collisions? (chaining vs open addressing)
- What's the optimal bucket size?
- Should we implement dynamic resizing?

Expected Time Complexity: O(n/k) average where n = keys, k = buckets. O(1) with good distribution
Expected Space Complexity: O(k + n) for k buckets and n key-value pairs
"""


class ListNode:
    """Node for linked list used in separate chaining."""
    
    def __init__(self, key: int = -1, value: int = -1, next_node: 'ListNode' = None):
        self.key = key
        self.value = value
        self.next = next_node


class MyHashMap:
    """
    HashMap implementation using separate chaining with linked lists.
    
    Uses an array of buckets where each bucket is a linked list.
    Collisions are handled by chaining - adding to the linked list.
    """
    
    def __init__(self):
        """Initialize HashMap with a prime number of buckets."""
        # Prime number reduces collision clustering
        self._size = 1009
        # Each bucket starts with a dummy head node
        self._buckets = [ListNode() for _ in range(self._size)]
    
    def _hash(self, key: int) -> int:
        """Compute hash index for a key."""
        return key % self._size
    
    def put(self, key: int, value: int) -> None:
        """
        Insert or update a key-value pair.
        
        Args:
            key: The key to insert/update
            value: The value to associate with the key
        """
        index = self._hash(key)
        curr = self._buckets[index]
        
        # Search for existing key in the chain
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value  # Update existing
                return
            curr = curr.next
        
        # Key not found, add new node at the end
        curr.next = ListNode(key, value)
    
    def get(self, key: int) -> int:
        """
        Get the value associated with a key.
        
        Args:
            key: The key to look up
        
        Returns:
            The value if found, -1 otherwise
        """
        index = self._hash(key)
        curr = self._buckets[index].next  # Skip dummy head
        
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        
        return -1
    
    def remove(self, key: int) -> None:
        """
        Remove a key and its associated value.
        
        Args:
            key: The key to remove
        """
        index = self._hash(key)
        curr = self._buckets[index]
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next  # Remove node
                return
            curr = curr.next


class MyHashMapSimple:
    """
    Simple HashMap using Python lists for buckets (no linked list nodes).
    
    Each bucket is a list of [key, value] pairs.
    """
    
    def __init__(self):
        """Initialize with prime number of buckets."""
        self._size = 1009
        self._buckets = [[] for _ in range(self._size)]
    
    def _hash(self, key: int) -> int:
        """Compute hash index."""
        return key % self._size
    
    def put(self, key: int, value: int) -> None:
        """Insert or update key-value pair."""
        index = self._hash(key)
        bucket = self._buckets[index]
        
        # Check if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = [key, value]  # Update
                return
        
        # Key not found, append
        bucket.append([key, value])
    
    def get(self, key: int) -> int:
        """Get value for key, or -1 if not found."""
        index = self._hash(key)
        bucket = self._buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return -1
    
    def remove(self, key: int) -> None:
        """Remove key if it exists."""
        index = self._hash(key)
        bucket = self._buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


class MyHashMapOpenAddressing:
    """
    HashMap using open addressing (linear probing) for collision handling.
    
    Instead of chaining, we find the next available slot.
    Uses a special marker for deleted slots.
    """
    
    EMPTY = None
    DELETED = "DELETED"
    
    def __init__(self):
        """Initialize with fixed size array."""
        self._size = 10007  # Prime number
        self._keys = [self.EMPTY] * self._size
        self._values = [self.EMPTY] * self._size
    
    def _hash(self, key: int) -> int:
        """Compute initial hash index."""
        return key % self._size
    
    def _find_slot(self, key: int) -> int:
        """Find the slot for a key (existing or new)."""
        index = self._hash(key)
        first_deleted = -1
        
        while self._keys[index] is not self.EMPTY:
            if self._keys[index] == key:
                return index  # Found existing key
            if self._keys[index] == self.DELETED and first_deleted == -1:
                first_deleted = index  # Remember first deleted slot
            index = (index + 1) % self._size  # Linear probe
        
        # Return first deleted slot if found, otherwise empty slot
        return first_deleted if first_deleted != -1 else index
    
    def put(self, key: int, value: int) -> None:
        """Insert or update key-value pair."""
        index = self._find_slot(key)
        self._keys[index] = key
        self._values[index] = value
    
    def get(self, key: int) -> int:
        """Get value for key, or -1 if not found."""
        index = self._hash(key)
        
        while self._keys[index] is not self.EMPTY:
            if self._keys[index] == key:
                return self._values[index]
            index = (index + 1) % self._size
        
        return -1
    
    def remove(self, key: int) -> None:
        """Remove key using tombstone marker."""
        index = self._hash(key)
        
        while self._keys[index] is not self.EMPTY:
            if self._keys[index] == key:
                self._keys[index] = self.DELETED
                self._values[index] = self.EMPTY
                return
            index = (index + 1) % self._size


# Test cases
if __name__ == "__main__":
    print("=" * 50)
    print("Testing MyHashMap (Linked List Chaining)")
    print("=" * 50)
    
    hash_map = MyHashMap()
    
    # Test case from problem
    hash_map.put(1, 1)
    hash_map.put(2, 2)
    print(f"get(1): {hash_map.get(1)}, expected: 1")
    print(f"get(3): {hash_map.get(3)}, expected: -1")
    
    hash_map.put(2, 1)  # Update
    print(f"get(2) after update: {hash_map.get(2)}, expected: 1")
    
    hash_map.remove(2)
    print(f"get(2) after remove: {hash_map.get(2)}, expected: -1")
    
    # Test collision handling
    print("\nTesting collision handling:")
    hash_map2 = MyHashMap()
    # Keys that hash to same bucket (1009 apart)
    hash_map2.put(1, 100)
    hash_map2.put(1010, 200)  # 1010 % 1009 = 1
    hash_map2.put(2019, 300)  # 2019 % 1009 = 1
    print(f"get(1): {hash_map2.get(1)}, expected: 100")
    print(f"get(1010): {hash_map2.get(1010)}, expected: 200")
    print(f"get(2019): {hash_map2.get(2019)}, expected: 300")
    
    print("\n" + "=" * 50)
    print("Testing MyHashMapSimple (List-based)")
    print("=" * 50)
    
    hash_map_simple = MyHashMapSimple()
    hash_map_simple.put(1, 1)
    hash_map_simple.put(2, 2)
    print(f"get(1): {hash_map_simple.get(1)}, expected: 1")
    hash_map_simple.put(2, 1)
    print(f"get(2) after update: {hash_map_simple.get(2)}, expected: 1")
    hash_map_simple.remove(2)
    print(f"get(2) after remove: {hash_map_simple.get(2)}, expected: -1")
    
    print("\n" + "=" * 50)
    print("Testing MyHashMapOpenAddressing (Linear Probing)")
    print("=" * 50)
    
    hash_map_open = MyHashMapOpenAddressing()
    hash_map_open.put(1, 1)
    hash_map_open.put(2, 2)
    print(f"get(1): {hash_map_open.get(1)}, expected: 1")
    print(f"get(3): {hash_map_open.get(3)}, expected: -1")
    hash_map_open.put(2, 1)
    print(f"get(2) after update: {hash_map_open.get(2)}, expected: 1")
    hash_map_open.remove(2)
    print(f"get(2) after remove: {hash_map_open.get(2)}, expected: -1")
    
    # Test that removed slot can be reused
    hash_map_open.put(2, 99)
    print(f"get(2) after re-add: {hash_map_open.get(2)}, expected: 99")
