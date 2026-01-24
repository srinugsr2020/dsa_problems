"""
Longest Duplicate Substring (LeetCode 1044)

Problem:
Given a string `s`, consider all duplicated substrings: (contiguous) substrings of `s`
that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length.
If `s` does not have a duplicated substring, return "".

Example 1:
    Input: s = "banana"
    Output: "ana"
    
Example 2:
    Input: s = "abcd"
    Output: ""

Constraints:
    - 2 <= s.length <= 3 * 10^4
    - s consists of lowercase English letters.

Approach:
    1. Binary Search + Rolling Hash (Rabin-Karp):
       - Binary search for the length of the longest duplicate substring
       - For each length, use rolling hash to check if a duplicate exists
       - Rolling hash allows O(1) hash computation for sliding window
    
    2. Key insight: If a duplicate of length L exists, duplicates of length < L also exist
       This monotonic property allows binary search
    
    3. Use polynomial rolling hash: hash = s[0]*base^(L-1) + s[1]*base^(L-2) + ... + s[L-1]
       - When sliding window, update hash in O(1)

Time Complexity: O(n log n) average case for binary search + rolling hash
Space Complexity: O(n) for storing hash values
"""

from typing import Optional, Set


def longest_dup_substring(s: str) -> str:
    """
    Find the longest duplicate substring using binary search + rolling hash.
    
    Args:
        s: The input string
        
    Returns:
        The longest duplicate substring, or empty string if none exists
    """
    n = len(s)
    
    if n <= 1:
        return ""
    
    # Convert string to array of integers for faster computation
    # 'a' -> 0, 'b' -> 1, etc.
    nums = [ord(c) - ord('a') for c in s]
    
    # Rolling hash parameters
    # Using a large prime modulo to reduce collision probability
    base = 26  # Number of lowercase letters
    mod = 2**63 - 1  # Large prime-like number
    
    def search_duplicate(length: int) -> Optional[int]:
        """
        Check if a duplicate substring of given length exists.
        
        Uses rolling hash to efficiently check all substrings.
        
        Args:
            length: The length of substring to search for
            
        Returns:
            Starting index of first duplicate found, or None if no duplicate
        """
        if length == 0:
            return None
        
        # Compute hash of first window
        current_hash = 0
        for i in range(length):
            current_hash = (current_hash * base + nums[i]) % mod
        
        # Store seen hashes with their starting positions
        # We store positions to verify matches and avoid false positives
        seen = {current_hash: [0]}
        
        # Precompute base^length for rolling hash update
        base_power = pow(base, length, mod)
        
        # Slide the window
        for start in range(1, n - length + 1):
            # Roll the hash: remove leftmost char, add new rightmost char
            # new_hash = (old_hash - s[start-1] * base^(length-1)) * base + s[start+length-1]
            current_hash = (current_hash * base - nums[start - 1] * base_power + nums[start + length - 1]) % mod
            
            if current_hash in seen:
                # Potential match found, verify to avoid hash collision
                current_substring = s[start:start + length]
                for prev_start in seen[current_hash]:
                    if s[prev_start:prev_start + length] == current_substring:
                        return start
                seen[current_hash].append(start)
            else:
                seen[current_hash] = [start]
        
        return None
    
    # Binary search for the longest length with a duplicate
    left, right = 1, n - 1
    result_start = -1
    result_length = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        duplicate_start = search_duplicate(mid)
        
        if duplicate_start is not None:
            # Found a duplicate of length mid, try longer
            result_start = duplicate_start
            result_length = mid
            left = mid + 1
        else:
            # No duplicate of length mid, try shorter
            right = mid - 1
    
    if result_start == -1:
        return ""
    
    return s[result_start:result_start + result_length]


def longest_dup_substring_suffix_array(s: str) -> str:
    """
    Alternative approach using Suffix Array and LCP Array.
    
    This approach builds a suffix array and finds the longest common prefix
    between adjacent suffixes. More memory-intensive but interesting approach.
    
    Args:
        s: The input string
        
    Returns:
        The longest duplicate substring, or empty string if none exists
    """
    n = len(s)
    
    if n <= 1:
        return ""
    
    # Build suffix array (simplified O(n log^2 n) version)
    # Suffix array: sorted indices of all suffixes
    suffixes = sorted(range(n), key=lambda i: s[i:])
    
    # Find longest common prefix between adjacent suffixes
    def lcp(i: int, j: int) -> int:
        """Compute length of longest common prefix between suffixes starting at i and j."""
        length = 0
        while i + length < n and j + length < n and s[i + length] == s[j + length]:
            length += 1
        return length
    
    max_lcp = 0
    result_start = 0
    
    # Compare adjacent suffixes in sorted order
    for i in range(1, n):
        curr_lcp = lcp(suffixes[i - 1], suffixes[i])
        if curr_lcp > max_lcp:
            max_lcp = curr_lcp
            result_start = suffixes[i]
    
    if max_lcp == 0:
        return ""
    
    return s[result_start:result_start + max_lcp]


def longest_dup_substring_simple(s: str) -> str:
    """
    Simpler but less efficient O(n^2) approach using hash set.
    
    Checks all possible substrings starting from longest to shortest.
    Good for understanding but too slow for large inputs.
    
    Args:
        s: The input string
        
    Returns:
        The longest duplicate substring, or empty string if none exists
    """
    n = len(s)
    
    # Try from longest possible to shortest
    for length in range(n - 1, 0, -1):
        seen: Set[str] = set()
        
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if substring in seen:
                return substring
            seen.add(substring)
    
    return ""


# Test cases to verify the solution
if __name__ == "__main__":
    print("Testing longest_dup_substring (Binary Search + Rolling Hash):")
    print("-" * 60)
    
    # Test case 1: Basic example with duplicate
    s1 = "banana"
    result1 = longest_dup_substring(s1)
    print(f"Input: '{s1}' -> Output: '{result1}'")
    # "ana" appears twice at positions 1 and 3
    assert result1 in ["ana"], f"Expected 'ana', got '{result1}'"
    
    # Test case 2: No duplicate
    s2 = "abcd"
    result2 = longest_dup_substring(s2)
    print(f"Input: '{s2}' -> Output: '{result2}'")
    assert result2 == "", f"Expected '', got '{result2}'"
    
    # Test case 3: Single character duplicates
    s3 = "aa"
    result3 = longest_dup_substring(s3)
    print(f"Input: '{s3}' -> Output: '{result3}'")
    assert result3 == "a", f"Expected 'a', got '{result3}'"
    
    # Test case 4: Longer duplicate
    s4 = "abcabc"
    result4 = longest_dup_substring(s4)
    print(f"Input: '{s4}' -> Output: '{result4}'")
    assert result4 == "abc", f"Expected 'abc', got '{result4}'"
    
    # Test case 5: Overlapping duplicates
    s5 = "aaa"
    result5 = longest_dup_substring(s5)
    print(f"Input: '{s5}' -> Output: '{result5}'")
    assert result5 == "aa", f"Expected 'aa', got '{result5}'"
    
    # Test case 6: Complex example
    s6 = "moplvidmaagmsromagnurwjscgijtwgsaeowokcnywfzukvnxhtwjtkqgyjbtewpdfnlxzstfhpmldnmvukvdfjgzmnlhmapqnbonxsyiofmbbchqymkkzngtnmyqdbgktltcfqzlohddhrzvcpbwggkflshwzhpvvkmmwnhyhfjcpxfhzmrdsjbtfgrlkqumslcfnqmrqthlmssrgoqtztwcskmgdgtssimqxpqoqflnvmmgsrgaopaupfcusbgcwvutmbcscymqmrcfwnfctjfoayxjayoswjtncrfaoevbmfxssjovtsqwfnxahdpmxhqzgasmndgjbxmzcbxkjrlqghtoeddfzsfxgrsdrwvkxvnsabrxntbfakqxsgbpprlrtvhbwgtwbsqwqebvttbigwwgwnexvuatdfiprqdaattyicowrtcshbdqqhawrzjoqnakqgstpvyvqqvtflxbayfsmeqpccxekthapomgyfhpysbpxnlsqffsmoeoicdwhtmpevdopxorvccmncmehxkisbuyvycymlscgywtqvijiuxwoyzzjsqdnswfhhxhymvlhkyrcxdmbliimlahonwhmqxavhigxhhtabtxiwuhmhtdqtpfrrcnxpnswfpmwlsrdwmsmfpvqmuvfqxpcffiqcafsoewjmqfshifhsqxyshjvzcovgtvqdnkdsnmggotxihpxswldyxswtexpiuqrrgueidejoqhvzxbckwpmyzspkiywnupzxrmcswvqltzvwhbpomjpwnxffixnopvzptdxllcmpmjjgjrbhmgzfasfzkcdxjzvhtfimcegwbrnfdvhbkwexwsthfznxwpxgbpbmlkwxhpvcqtcvnyjwwcqqycjxvqqdmvbgsyssgtzhesvbqqbxpfudssacbjbqpvycfephntvbznylgvchpjspqedhlamhsddrdmfnvjvrvphzdhfxqmpdokfdghjnghxrhhpdahvrxpnhpyxgvpnivjrvsnfqxvlhpnqfmxhdyvdxpqsxtxpfxrhehbggvjkkhynfvjspmwmbmcxlexdkhwsrdgyjrlgmhfxbuhxbksxffawfwrdcrwpxmfgzjxnxvxoewbkptdrxgwbfnqpxjwqfnfwxcjcfkwjgnfhwgfnhwnfvjxsnfxwbfnvjxsqfnzwbnfvwqfwrgjrnfwejwbfnwhrgnfwhrnfwbknfwbnqfwhrnfbwhnrfwhbnrfhwnqfbwfbwqhnqfhwnqfbwhrnfwhbnqrfhwnqfhwnrfhwnqf"
    result6 = longest_dup_substring(s6)
    print(f"Input: long string -> Output length: {len(result6)}, Output: '{result6[:20]}...'")
    assert len(result6) > 0, "Expected a non-empty result for complex string"
    
    # Test suffix array approach
    print("\nTesting suffix array approach:")
    print("-" * 60)
    result_sa = longest_dup_substring_suffix_array(s1)
    print(f"Suffix Array - Input: '{s1}' -> Output: '{result_sa}'")
    assert result_sa in ["ana"], f"Expected 'ana', got '{result_sa}'"
    
    # Verify both approaches give same length results
    for test_str in [s1, s2, s3, s4, s5]:
        r1 = longest_dup_substring(test_str)
        r2 = longest_dup_substring_suffix_array(test_str)
        assert len(r1) == len(r2), f"Mismatch for '{test_str}': '{r1}' vs '{r2}'"
        print(f"Both approaches agree for '{test_str}': length={len(r1)}")
    
    print("\n✅ All test cases passed!")
