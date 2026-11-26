# Data structures and algorithms in Python

Start in [`problems/`](problems/). There is **one file per exercise**, grouped by topic and difficulty. Each file starts with the problem statement and input/output examples. The worked files then put the baseline, Python or standard-library approach, and optimized approach together. When there is no direct built-in, the Python approach demonstrates a useful helper or a straightforward alternative.

## Categories

| Category | Exercises |
|---|---|
| Two pointers | [Compaction, reversal, and n-sum](problems/two-pointers/) |
| Sliding windows | [Fixed and variable windows](problems/sliding-windows/) |
| Hash maps and sets | [Membership, counting, and design](problems/hash-maps-and-sets/) |
| Prefix sums | [Count subarrays summing to k](problems/prefix-sums/) |
| String matching and encoding | [Search, repeated patterns, and codecs](problems/string-matching-and-encoding/) |
| Sorting | [Categorical sort and score ranges](problems/sorting/) |
| Binary search | [Exact search and insertion point](problems/binary-search/) |
| Linked lists | [Traversal, merging, and rewiring](problems/linked-lists/) |
| Fast and slow pointers | [Cycles, middle nodes, and palindromes](problems/fast-and-slow-pointers/) |
| Stacks and queues | [Bracket matching, scoring, and path cleanup](problems/stacks-and-queues/) |
| Heaps and top-k | [Most frequent elements](problems/heaps-and-top-k/) |
| Greedy algorithms | [Partition labels and buildable palindrome](problems/greedy/) |
| Backtracking | [Parentheses and phone keypad combinations](problems/backtracking/) |
| Dynamic programming | [Common subsequences and palindromic substrings](problems/dynamic-programming/) |

Python container walkthroughs and embedded demos live separately in the [tutorials](tutorials/README.md).

## Running an exercise

Use Python 3.8 or later. Each worked program uses only the standard library and runs its assertions when executed, for example:

```shell
python3 problems/backtracking/medium/generate_parenthesis.py
```

[Baseball scoring](problems/stacks-and-queues/easy/baseball_game.py) has one stack solution rather than three artificial variations.

The [practice manifest](practice_manifest.json) records reviewed difficulty and historical caveats in `review_status`, and detailed approach comparisons and `code_path` in `lessons`. Its `source_paths` maps each original path at `source_revision` to the current exercise file; multiple historical variants can map to the same file. The originals remain in the [Git snapshot](https://github.com/srinugsr2020/dsa_problems/tree/8ae4b8540769f0d0e5ec0ca3867bb698d18b9df1).

## Recommended next exercises (not published here)

The [historical roadmap](tutorials/README.md#practice-problems) lists ideas, not extra source files. Prioritize these gaps:

| Exercise | Why add it |
|---|---|
| Binary-tree level order | Introduce queue-based BFS and per-level grouping. |
| Number of islands | Practice grid traversal, visited state, and the difference between recursion and an explicit worklist. |
| Trie prefix search | Introduce prefix lookup and distinguish a stored word from a prefix. |
| Maximum subarray | Introduce a compact dynamic-programming state and the all-negative edge case. |
| Single number | Introduce XOR cancellation and specify the assumption that all other values occur twice. |
| Merge intervals | Practice sorting endpoints, scanning overlaps, and defining whether touching intervals merge. |
| Product except self | Extend prefix-sum thinking to prefix and suffix products; handle zeros without division. |

## Reference Books
1. [Grokking the Coding Interview](https://www.educative.io/courses/grokking-the-coding-interview)
2. [Elements of Programming Interviews in Python](https://elementsofprogramminginterviews.com/)
3. [Cracking the Coding Interview](https://www.crackingthecodinginterview.com/)
4. [LeetCode](https://leetcode.com/)
5. [GeeksforGeeks](https://www.geeksforgeeks.org/)
6. [InterviewBit](https://www.interviewbit.com/)
7. [CodeSignal](https://codesignal.com/)
8. [HackerRank](https://www.hackerrank.com/domains/tutorials/10-days-of-javascript)
9. [CodeWars](https://www.codewars.com/)
10. [Project Euler](https://projecteuler.net/)
11. [TopCoder](https://www.topcoder.com/)
12. [SPOJ](https://www.spoj.com/)
13. [CodeChef](https://www.codechef.com/)
14. [AtCoder](https://atcoder.jp/)
15. [Kaggle](https://www.kaggle.com/)
16. [Google Coding Competitions](https://codingcompetitions.withgoogle.com/)
17. [Facebook Hacker Cup](https://www.facebook.com/codingcompetitions/hacker-cup)
18. [Microsoft Coding Competitions](https://www.microsoft.com/en-us/research/blog/inviting-students-to-microsoft-coding-competitions/)
19. [Amazon Coding Competitions](https://www.amazon.jobs/en/teams/internships-for-students)
20. [Apple Coding Competitions](https://developer.apple.com/wwdc/)
21. Coding Interview Patterns: Nail Your Next Coding Interview
