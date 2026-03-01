"""=============================================================================
MEDIUM (Dynamic Programming): Longest Common Subsequence
=============================================================================

Given two strings text1 and text2, return the length of their longest
common subsequence (LCS). A subsequence is a sequence that can be derived
by deleting zero or more characters without changing the relative order.

Examples:
    text1 = "abcde", text2 = "ace"   ->  3   ("ace")
    text1 = "abc",   text2 = "abc"   ->  3   ("abc")
    text1 = "abc",   text2 = "def"   ->  0

Constraints:
    - 1 <= len(text1), len(text2) <= 1000

Target:
    - Time:  O(m * n)
    - Space: O(min(m, n))  with space-optimised DP

Hints:
    - dp[i][j] = LCS of text1[:i] and text2[:j]
    - If text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    - Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

-----------------------------------------------------------------------------
YOUR TASK
-----------------------------------------------------------------------------
Implement `longest_common_subsequence(text1: str, text2: str) -> int`.
"""

from __future__ import annotations


def longest_common_subsequence(text1: str, text2: str) -> int:
    """Return the length of the longest common subsequence."""

    # Ensure text2 is the shorter string for space optimisation
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    m, n = len(text1), len(text2)

    # Only need two rows: previous and current
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        # Swap rows
        prev, curr = curr, [0] * (n + 1)

    return prev[n]


def _run_samples() -> None:
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("", "abc") == 0
    assert longest_common_subsequence("oxcpqrsvwf", "shmtulqrypy") == 2
    assert longest_common_subsequence("abcba", "abcbcba") == 5


if __name__ == "__main__":
    _run_samples()
    print("All sample tests passed.")
