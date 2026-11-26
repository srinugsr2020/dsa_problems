"""
Partition Labels Problem (Greedy + Two Pointers Approach)

Problem Statement:
------------------
You are given a string s. We want to partition the string into as many parts as 
possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, 
the resultant string should be s.

Return a list of integers representing the size of these parts.

Constraints:
------------
- 1 <= s.length <= 500
- s consists of lowercase English letters

Examples:
---------
Example 1:
    Input: s = "ababcbacadefegdehijhklij"
    Output: [9, 7, 8]
    Explanation:
        The partition is "ababcbaca", "defegde", "hijhklij".
        This is a partition so that each letter appears in at most one part.
        A partition like "ababcbacadefegde", "hijhklij" is incorrect, 
        because it splits s into less parts.

Example 2:
    Input: s = "eccbbbbdec"
    Output: [10]
    Explanation:
        The entire string must be one partition because 'e' appears at 
        both the start and end, and 'c' appears in between.

Example 3:
    Input: s = "abcdef"
    Output: [1, 1, 1, 1, 1, 1]
    Explanation:
        Each character appears only once, so we can partition at every character.

Example 4:
    Input: s = "aaa"
    Output: [3]
    Explanation:
        All three 'a's must be in the same partition.

Example 5:
    Input: s = "abccaddbeffe"
    Output: [8, 4]
    Explanation:
        "abccaddb" (contains all occurrences of a, b, c, d)
        "effe" (contains all occurrences of e, f)

Understanding the Problem:
--------------------------
The key insight is that if a character appears in a partition, ALL occurrences 
of that character must be in the same partition.

Think of it this way:
- If 'a' appears at index 0 and index 8, then indices 0-8 must be in the same partition
- If within indices 0-8, 'b' appears and its last occurrence is at index 6, 
  we still need to extend to index 8 (because of 'a')
- If within indices 0-8, 'c' appears and its last occurrence is at index 12,
  now we need to extend the partition to index 12

Strategy:
---------
1. Find the last occurrence of each character in the string
2. Traverse the string while tracking the furthest point we must reach
3. As we encounter characters, update the end point to the maximum of 
   current end and the last occurrence of the current character
4. When we reach the current end point, we can create a partition

Visual Example:
---------------
s = "ababcbacadefegdehijhklij"
     0123456789...

Step 1: Find last occurrence of each character:
    a -> 8  (last 'a' at index 8)
    b -> 5  (last 'b' at index 5)
    c -> 7  (last 'c' at index 7)
    d -> 14 (last 'd' at index 14)
    e -> 15 (last 'e' at index 15)
    f -> 11 (last 'f' at index 11)
    g -> 13 (last 'g' at index 13)
    h -> 19 (last 'h' at index 19)
    i -> 22 (last 'i' at index 22)
    j -> 23 (last 'j' at index 23)
    k -> 20 (last 'k' at index 20)
    l -> 21 (last 'l' at index 21)

Step 2: Traverse and track partition boundaries:

Index 0: char='a', last['a']=8, end=8
Index 1: char='b', last['b']=5, end=8 (no change)
Index 2: char='a', last['a']=8, end=8 (no change)
Index 3: char='b', last['b']=5, end=8 (no change)
Index 4: char='c', last['c']=7, end=8 (no change)
Index 5: char='b', last['b']=5, end=8 (no change)
Index 6: char='a', last['a']=8, end=8 (no change)
Index 7: char='c', last['c']=7, end=8 (no change)
Index 8: char='a', last['a']=8, end=8 (reached end!)
        → Partition 1: length = 9 (indices 0-8)

Index 9: char='d', last['d']=14, end=14
Index 10: char='e', last['e']=15, end=15
Index 11: char='f', last['f']=11, end=15 (no change)
Index 12: char='e', last['e']=15, end=15 (no change)
Index 13: char='g', last['g']=13, end=15 (no change)
Index 14: char='d', last['d']=14, end=15 (no change)
Index 15: char='e', last['e']=15, end=15 (reached end!)
        → Partition 2: length = 7 (indices 9-15)

Index 16: char='h', last['h']=19, end=19
Index 17: char='i', last['i']=22, end=22
Index 18: char='j', last['j']=23, end=23
Index 19: char='h', last['h']=19, end=23 (no change)
Index 20: char='k', last['k']=20, end=23 (no change)
Index 21: char='l', last['l']=21, end=23 (no change)
Index 22: char='i', last['i']=22, end=23 (no change)
Index 23: char='j', last['j']=23, end=23 (reached end!)
        → Partition 3: length = 8 (indices 16-23)

Result: [9, 7, 8]

Algorithm Outline:
------------------
1. Create a dictionary/map to store the last occurrence index of each character
   - Iterate through the string once to populate this map

2. Initialize variables:
   - start: beginning of current partition (initially 0)
   - end: end of current partition (initially 0)
   - result: list to store partition sizes

3. Iterate through the string with index i:
   - Update end = max(end, last_occurrence[s[i]])
   - If i == end (we've reached the end of current partition):
     * Calculate partition size: end - start + 1
     * Add size to result
     * Update start = i + 1 (start of next partition)

4. Return result

Key Insights:
-------------
1. Greedy approach: We want as many partitions as possible, so we make a cut 
   as soon as we can
2. We can only make a cut when we've seen all occurrences of every character 
   in the current partition
3. The "end" pointer extends whenever we encounter a character whose last 
   occurrence is further ahead
4. When current index reaches "end", we know we can safely partition here

Why This Works:
---------------
- By tracking the last occurrence of each character, we know the minimum 
  extent of any partition
- As we traverse, we continuously update the end boundary to accommodate 
  all characters we've seen so far
- When we reach the end boundary, we're guaranteed that all characters in 
  this partition are complete (no more occurrences ahead)

Edge Cases to Consider:
-----------------------
1. Single character string: "a" -> [1]
2. All same characters: "aaa" -> [3]
3. All unique characters: "abc" -> [1, 1, 1]
4. Characters appearing at extremes: "aba" -> [3]
5. Entire string is one partition: "abccba" -> [6]
6. Two characters interleaved: "ababab" -> [6]

Common Pitfalls:
----------------
1. Forgetting to handle the last partition
2. Off-by-one errors when calculating partition size
3. Not updating the end boundary correctly (must use max)
4. Trying to partition without finding last occurrences first

Follow-up Questions:
--------------------
1. Can you solve it in one pass? (Hint: You need two passes - one to find 
   last occurrences, one to partition)
2. What if we wanted the minimum number of partitions instead of maximum?
   (Answer: That would be [len(s)] - entire string)
3. What if we needed to return the actual partition strings instead of sizes?
4. How would you modify this for uppercase letters or other characters?

Expected Time Complexity: O(n) where n is the length of string
    - O(n) to find last occurrences
    - O(n) to traverse and partition
    - Total: O(n)

Expected Space Complexity: O(1) 
    - Only 26 lowercase letters, so the map is O(26) = O(1)
    - Result list doesn't count as extra space (it's the output)
"""


def partition_labels(s: str) -> list[int]:
    """
    Partition the string into as many parts as possible where each letter 
    appears in at most one part.
    
    Args:
        s: A string consisting of lowercase English letters
    
    Returns:
        A list of integers representing the size of each partition
    
    Example:
        >>> partition_labels("ababcbacadefegdehijhklij")
        [9, 7, 8]
        >>> partition_labels("eccbbbbdec")
        [10]
        >>> partition_labels("abcdef")
        [1, 1, 1, 1, 1, 1]
    """
    part_list = []
    last_occurrence = {char: idx for idx, char in enumerate(s)}
    start, end = 0, 0
    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])
        if i == end:
            part_list.append(end - start + 1)
            start = i + 1
    return part_list


# Test cases
if __name__ == "__main__":
    # Test case 1: Example from problem description
    s1 = "ababcbacadefegdehijhklij"
    print(f"Test 1: s = '{s1}'")
    result1 = partition_labels(s1)
    print(f"Output: {result1}")
    print(f"Expected: [9, 7, 8]\n")
    
    # Test case 2: Entire string is one partition
    s2 = "eccbbbbdec"
    print(f"Test 2: s = '{s2}'")
    result2 = partition_labels(s2)
    print(f"Output: {result2}")
    print(f"Expected: [10]\n")
    
    # Test case 3: All unique characters
    s3 = "abcdef"
    print(f"Test 3: s = '{s3}'")
    result3 = partition_labels(s3)
    print(f"Output: {result3}")
    print(f"Expected: [1, 1, 1, 1, 1, 1]\n")
    
    # Test case 4: All same characters
    s4 = "aaa"
    print(f"Test 4: s = '{s4}'")
    result4 = partition_labels(s4)
    print(f"Output: {result4}")
    print(f"Expected: [3]\n")
    
    # Test case 5: Two partitions
    s5 = "abccaddbeffe"
    print(f"Test 5: s = '{s5}'")
    result5 = partition_labels(s5)
    print(f"Output: {result5}")
    print(f"Expected: [8, 4]\n")
    
    # Test case 6: Single character
    s6 = "a"
    print(f"Test 6: s = '{s6}'")
    result6 = partition_labels(s6)
    print(f"Output: {result6}")
    print(f"Expected: [1]\n")
    
    # Test case 7: Characters at extremes
    s7 = "aba"
    print(f"Test 7: s = '{s7}'")
    result7 = partition_labels(s7)
    print(f"Output: {result7}")
    print(f"Expected: [3]\n")
    
    # Test case 8: Multiple small partitions
    s8 = "abcabc"
    print(f"Test 8: s = '{s8}'")
    result8 = partition_labels(s8)
    print(f"Output: {result8}")
    print(f"Expected: [6]\n")
    
    # Test case 9: Alternating pattern
    s9 = "ababab"
    print(f"Test 9: s = '{s9}'")
    result9 = partition_labels(s9)
    print(f"Output: {result9}")
    print(f"Expected: [6]\n")
    
    # Test case 10: Complex partitioning
    s10 = "abcdefghabij"
    print(f"Test 10: s = '{s10}'")
    result10 = partition_labels(s10)
    print(f"Output: {result10}")
    print(f"Expected: [9, 1, 1, 1]\n")
    
    # Test case 11: Two characters only
    s11 = "aabbaa"
    print(f"Test 11: s = '{s11}'")
    result11 = partition_labels(s11)
    print(f"Output: {result11}")
    print(f"Expected: [6]\n")
    
    # Test case 12: Longer string with clear partitions
    s12 = "abcdefghijklmnopqrstuvwxyz"
    print(f"Test 12: s = '{s12}'")
    result12 = partition_labels(s12)
    print(f"Output: {result12}")
    print(f"Expected: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]\n")
