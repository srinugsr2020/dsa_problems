"""
Top K Frequent Elements Problem

Problem Statement:
------------------
Given an integer array 'nums' and an integer 'k', return the 'k' most frequent elements.
You may return the answer in any order.

Constraints:
------------
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array]
- It is guaranteed that the answer is unique

Examples:
---------
Example 1:
    Input: nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]
    Explanation: 1 appears 3 times, 2 appears 2 times

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Hints:
------
1. First, count the frequency of each element using a hash map
2. Then find the k elements with highest frequency
3. Approach 1: Sort by frequency - O(n log n)
4. Approach 2: Use a min-heap of size k - O(n log k)
5. Approach 3: Bucket sort by frequency - O(n)

Expected Time Complexity: O(n) with bucket sort, O(n log k) with heap
Expected Space Complexity: O(n)
"""

from collections import Counter
import heapq

def top_k_frequent_map(nums: list[int], k: int) -> list[int]:
    """
    Basic approach using frequency map and sorting.
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
    Returns:
        List of k most frequent elements
    """
    map_freq = {}
    for num in nums:
        map_freq[num] = map_freq.get(num, 0) + 1
    # Sort items by frequency in descending order
    sorted_items = sorted(map_freq.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items[:k]]

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Find the k most frequent elements using bucket sort.
    
    This is the optimal O(n) solution. We create buckets where index
    represents frequency, then collect elements from highest frequency buckets.
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
    
    Returns:
        List of k most frequent elements
    
    Example:
        >>> top_k_frequent([1, 1, 1, 2, 2, 3], 2)
        [1, 2]
    """
    # Step 1: Count frequency of each element
    freq = Counter(nums)
    
    # Step 2: Create buckets where index = frequency
    # Maximum frequency possible is len(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for num, count in freq.items():
        buckets[count].append(num)
    
    # Step 3: Collect k elements from highest frequency buckets
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result


def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    """
    Alternative approach using a min-heap of size k.
    
    Maintain a heap of size k. For each element, if heap size < k, add it.
    If current frequency > smallest in heap, replace.
    
    Time: O(n log k)
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
    
    Returns:
        List of k most frequent elements
    """
    freq = Counter(nums)
    
    # Use heapq.nlargest which is optimized for this use case
    # Returns k elements with largest frequencies
    return heapq.nlargest(k, freq.keys(), key=freq.get)


def top_k_frequent_heap_manual(nums: list[int], k: int) -> list[int]:
    """
    Manual min-heap approach to understand the algorithm better.
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
    
    Returns:
        List of k most frequent elements
    """
    freq = Counter(nums)
    
    # Min-heap of (frequency, element)
    # We keep only k elements in the heap
    min_heap = []
    
    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))
        
        # If heap exceeds size k, remove smallest frequency element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # Extract elements from heap
    return [num for count, num in min_heap]


def top_k_frequent_sort(nums: list[int], k: int) -> list[int]:
    """
    Simple approach: sort by frequency.
    
    Time: O(n log n) due to sorting
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
    
    Returns:
        List of k most frequent elements
    """
    freq = Counter(nums)
    
    # Sort by frequency (descending) and take first k
    sorted_by_freq = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
    
    return sorted_by_freq[:k]


def top_k_frequent_counter(nums: list[int], k: int) -> list[int]:
    """
    Pythonic approach using Counter's most_common method.
    
    Args:
        nums: List of integers
        k: Number of top frequent elements to return
    
    Returns:
        List of k most frequent elements
    """
    freq = Counter(nums)
    return [num for num, count in freq.most_common(k)]


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(f"Test 1: nums = {nums1}, k = {k1}")
    print(f"Output: {top_k_frequent(nums1, k1)}")
    print(f"Expected: [1, 2]\n")
    
    # Test case 2
    nums2 = [1]
    k2 = 1
    print(f"Test 2: nums = {nums2}, k = {k2}")
    print(f"Output: {top_k_frequent(nums2, k2)}")
    print(f"Expected: [1]\n")
    
    # Test case 3
    nums3 = [4, 4, 4, 4, 5, 5, 5, 6, 6, 7]
    k3 = 2
    print(f"Test 3: nums = {nums3}, k = {k3}")
    print(f"Output: {top_k_frequent(nums3, k3)}")
    print(f"Expected: [4, 5]\n")
    
    # Test case 4: All elements have same frequency
    nums4 = [1, 2, 3, 4]
    k4 = 2
    print(f"Test 4: nums = {nums4}, k = {k4}")
    print(f"Output: {top_k_frequent(nums4, k4)}")
    print(f"Expected: Any 2 of [1, 2, 3, 4]\n")
    
    # Test case 5: Negative numbers
    nums5 = [-1, -1, -2, -2, -2, 3]
    k5 = 2
    print(f"Test 5: nums = {nums5}, k = {k5}")
    print(f"Output: {top_k_frequent(nums5, k5)}")
    print(f"Expected: [-2, -1]\n")
    
    # Test all approaches
    print("--- Testing all approaches ---")
    test_nums = [1, 1, 1, 2, 2, 3]
    test_k = 2
    print(f"Input: nums = {test_nums}, k = {test_k}")
    print(f"Bucket Sort: {top_k_frequent(test_nums, test_k)}")
    print(f"Heap (nlargest): {top_k_frequent_heap(test_nums, test_k)}")
    print(f"Heap (manual): {top_k_frequent_heap_manual(test_nums, test_k)}")
    print(f"Sort: {top_k_frequent_sort(test_nums, test_k)}")
    print(f"Counter.most_common: {top_k_frequent_counter(test_nums, test_k)}")
