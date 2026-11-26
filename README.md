# Data structures and algorithms in Python

Use the [worked editions](worked_examples/) to compare a baseline, a Python or standard-library approach, and an optimized approach under the same problem contract. Some problems have no direct built-in solution; their editions say so and show an idiomatic helper instead.

The [source archive](problems/) preserves the original programs, including multiple versions of some exercises. These are historical references: they can differ in return values, input assumptions, or complexity claims. Use [the manifest](practice_manifest.json) to find the reviewed edition and caveats for a particular exercise.

## Categories

| Category | Original sources | Worked editions |
|---|---|---|
| Two pointers | [Compaction, reversal, and n-sum](problems/two-pointers/) | [Compare approaches](worked_examples/pointers/) |
| Sliding windows | [Fixed and variable windows](problems/sliding-windows/) | [Compare approaches](worked_examples/window/) |
| Hash maps and sets | [Membership, counting, and design](problems/hash-maps-and-sets/) | [Compare approaches](worked_examples/hash/) |
| Prefix sums | [Count subarrays summing to k](problems/prefix-sums/) | [Compare approaches](worked_examples/prefix/) |
| String matching and encoding | [Search, repeated patterns, and codecs](problems/string-matching-and-encoding/) | [Compare approaches](worked_examples/matching/) |
| Sorting | [Categorical sort and score ranges](problems/sorting/) | [Compare approaches](worked_examples/sorting/) |
| Binary search | [Exact search and insertion point](problems/binary-search/) | [Compare approaches](worked_examples/search/) |
| Linked lists | [Traversal, merging, and rewiring](problems/linked-lists/) | [Compare approaches](worked_examples/linked/) |
| Fast and slow pointers | [Cycles, middle nodes, and palindromes](problems/fast-and-slow-pointers/) | [Compare approaches](worked_examples/cycle/) |
| Stacks and queues | [Bracket matching, scoring, and path cleanup](problems/stacks-and-queues/) | [Compare approaches](worked_examples/stack/) |
| Heaps and top-k | [Most frequent elements](problems/heaps-and-top-k/) | [Compare approaches](worked_examples/heap/) |
| Greedy algorithms | [Partition labels and buildable palindrome](problems/greedy/) | [Compare approaches](worked_examples/greedy/) |
| Backtracking | [Parentheses and phone keypad combinations](problems/backtracking/) | [Compare approaches](worked_examples/backtracking/) |
| Dynamic programming | [Common subsequences and palindromic substrings](problems/dynamic-programming/) | [Compare approaches](worked_examples/dp/) |

Within each category, the source files are grouped by difficulty. The manifest records the reviewed difficulty for each exercise. Python container walkthroughs and embedded demos live separately in the [tutorials](tutorials/README.md).

## Running a worked edition

Use Python 3.8 or later and run the `code_path` listed in `practice_manifest.json` directly. Each worked program uses only the standard library and runs its assertions when executed, for example:

```shell
python3 worked_examples/search/binary-search.py
```

In the manifest, `source_revision` identifies the original snapshot used by `source_paths`. `legacy_exercises` associates stable IDs with their original variant paths. `review_status` records difficulty, contract, correctness caveats, and approach coverage in the archive. `lessons` lists only validated standalone editions, keyed by those same IDs; `code_path` is relative to the repository root. [Baseball scoring](problems/stacks-and-queues/easy/baseball_game.py) remains archive-only: the single-pass stack is already the natural solution, and a library wrapper would not add a useful comparison.

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
