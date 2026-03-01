# Python Data Structures - Comprehensive Guide

A collection of comprehensive tutorials covering Python's built-in data structures and the `collections` module, along with pattern-based practice problems.

---

## Table of Contents

- [Tutorials](#tutorials)
  - [Lists](#1-lists)
  - [Strings](#2-strings)
  - [Dictionaries](#3-dictionaries)
  - [Tuples](#4-tuples)
  - [Sets](#5-sets)
  - [Arrays](#6-arrays)
  - [Heaps](#7-heaps)
  - [Collections Module](#8-collections-module)
- [Practice Problems](#practice-problems)
  - [Lists Practice](#lists-practice)
  - [Strings Practice](#strings-practice)
  - [Dictionaries Practice](#dictionaries-practice)
  - [Sets Practice](#sets-practice)
  - [Tuples Practice](#tuples-practice)

---

## Tutorials

### 1. Lists

> **File:** [lists.py](lists.py)

Mutable, ordered sequences that can hold elements of any type — one of the most versatile data structures in Python.

**Key Characteristics:** Mutable | Ordered | Indexed | Heterogeneous | Dynamic sizing

| Section | Topic |
|---------|-------|
| 1 | Creating Lists |
| 2 | Accessing List Elements |
| 3 | Modifying List Elements |
| 4 | Adding Elements |
| 5 | Removing Elements |
| 6 | Searching and Counting |
| 7 | Sorting and Reversing |
| 8 | List Comprehensions (Advanced) |
| 9 | Copying Lists |
| 10 | Useful List Operations |
| 11 | Iterating Over Lists |

---

### 2. Strings

> **File:** [strings.py](strings.py)

Immutable sequences of Unicode characters — the primary data type for text manipulation.

**Key Characteristics:** Immutable | Ordered | Indexed | Hashable | Full Unicode support

| Section | Topic |
|---------|-------|
| 1 | Creating Strings |
| 2 | String Indexing and Slicing |
| 3 | String Immutability |
| 4 | String Methods — Case Conversion |
| 5 | String Methods — Searching |
| 6 | String Methods — Modification |
| 7 | String Methods — Splitting and Joining |
| 8 | String Methods — Checking |
| 9 | String Formatting |
| 10 | String Concatenation |
| 11 | Common String Operations |
| 12 | Encoding and Decoding |
| 13 | Regular Expressions (Brief) |
| 14 | Practical Examples |

---

### 3. Dictionaries

> **File:** [dictionary.py](dictionary.py)

Mutable collections of key-value pairs with O(1) average lookup. Maintains insertion order in Python 3.7+.

**Key Characteristics:** O(1) lookup/insert/delete | Unique hashable keys | Insertion-ordered (3.7+)

| Section | Topic |
|---------|-------|
| 1 | Creating Dictionaries |
| 2 | Accessing Dictionary Elements |
| 3 | Updating Dictionaries |
| 4 | Deleting Dictionary Elements |
| 5 | Sorting Dictionaries |
| 6 | Iterating Over Dictionaries |
| 7 | Useful Dictionary Methods |
| 8 | Dictionary Comprehensions |

---

### 4. Tuples

> **File:** [tuples.py](tuples.py)

Immutable, ordered sequences — hashable and suitable for use as dictionary keys.

**Key Characteristics:** Immutable | Ordered | Indexed | Hashable | Memory efficient

| Section | Topic |
|---------|-------|
| 1 | Creating Tuples |
| 2 | Accessing Tuple Elements |
| 3 | Tuple Unpacking |
| 4 | Tuple Immutability |
| 5 | Tuple Methods and Operations |
| 6 | Tuple Comparisons |
| 7 | Tuples as Dictionary Keys |
| 8 | NamedTuples (Enhanced Tuples) |
| 9 | Tuple vs List — When to Use |
| 10 | Practical Examples |

---

### 5. Sets

> **File:** [sets.py](sets.py)

Unordered, mutable collections of unique hashable elements — optimized for membership testing and mathematical set operations.

**Key Characteristics:** Unordered | Unique elements | O(1) lookup | Hashable elements only

| Section | Topic |
|---------|-------|
| 1 | Creating Sets |
| 2 | Set Properties |
| 3 | Adding and Removing Elements |
| 4 | Membership Testing |
| 5 | Set Operations (Mathematical) |
| 6 | In-Place Set Operations |
| 7 | Set Comparisons |
| 8 | Frozen Sets (Immutable Sets) |
| 9 | Iterating Over Sets |
| 10 | Practical Examples |

---

### 6. Arrays

> **File:** [arrays.py](arrays.py)

Type-constrained, memory-efficient arrays using the built-in `array` module — ideal for bulk operations on numeric data.

**Key Characteristics:** Type-constrained | Memory efficient | Faster numeric operations | C-interoperable

| Section | Topic |
|---------|-------|
| 1 | Creating Arrays |
| 2 | Memory Efficiency |
| 3 | Accessing and Modifying Elements |
| 4 | Array Methods |
| 5 | Converting To/From Other Types |
| 6 | File Operations |
| 7 | Array vs List Performance |
| 8 | Practical Examples |
| 9 | Comparison with NumPy |
| 10 | Summary |

---

### 7. Heaps

> **File:** [heaps.py](heaps.py)

Min-heap data structure via the `heapq` module — efficient for priority queues and top-N queries.

**Key Characteristics:** Min-heap | O(log n) push/pop | O(1) min access | O(n) heapify

| Section | Topic |
|---------|-------|
| 1 | Heap Basics |
| 2 | Creating Heaps |
| 3 | Heap Operations |
| 4 | Finding N Largest/Smallest |
| 5 | Max-Heap (Using Negation) |
| 6 | Heap with Custom Objects |
| 7 | Heap Sort |
| 8 | Merging Sorted Iterables |
| 9 | Practical Examples |
| 10 | Time Complexity Summary |

---

### 8. Collections Module

> **File:** [collections_module.py](collections_module.py)

Specialized container data types that extend the built-in containers with additional functionality.

| Section | Class | Description |
|---------|-------|-------------|
| 1 | `namedtuple` | Tuple subclass with named fields |
| 2 | `deque` | Double-ended queue with O(1) append/pop from both ends |
| 3 | `Counter` | Dict subclass for counting hashable objects |
| 4 | `defaultdict` | Dict with default factory for missing keys |
| 5 | `OrderedDict` | Dict that remembers insertion order |
| 6 | `ChainMap` | Single view of multiple dictionaries |
| 7 | Summary | When to use each class |

---

## Practice Problems

Pattern-based practice problems organized by data structure and algorithmic technique. Each file includes a problem statement, reference solution, and `assert`-based tests.

### Lists Practice

> **Folder:** [practice/lists/](practice/lists/)  |  **README:** [practice/lists/README.md](practice/lists/README.md)

#### `array_manipulation/` — in-place transforms, greedy passes, index tricks
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_reverse_list_copy.py](practice/lists/array_manipulation/easy_reverse_list_copy.py) | Easy | Reverse a list without modifying input |
| [easy_rotate_right_by_k.py](practice/lists/array_manipulation/easy_rotate_right_by_k.py) | Easy | Right-rotate a list by k steps in-place |
| [easy_running_sum.py](practice/lists/array_manipulation/easy_running_sum.py) | Easy | Running / cumulative sum |
| [easy_majority_element.py](practice/lists/array_manipulation/easy_majority_element.py) | Easy | Majority element — Boyer-Moore Voting |
| [easy_best_time_buy_sell_stock.py](practice/lists/array_manipulation/easy_best_time_buy_sell_stock.py) | Easy | Max profit from one buy-sell |
| [medium_find_all_duplicates.py](practice/lists/array_manipulation/medium_find_all_duplicates.py) | Medium | Find all duplicates via index-negation |
| [medium_sort_colors_dutch_flag.py](practice/lists/array_manipulation/medium_sort_colors_dutch_flag.py) | Medium | Dutch National Flag (3 pointers) |
| [medium_maximum_subarray_kadane.py](practice/lists/array_manipulation/medium_maximum_subarray_kadane.py) | Medium | Kadane's Algorithm |

#### `hashmap/` — fast key lookup and frequency counting
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_contains_duplicate.py](practice/lists/hashmap/easy_contains_duplicate.py) | Easy | Detect any duplicate via hashset |
| [easy_two_sum_indices.py](practice/lists/hashmap/easy_two_sum_indices.py) | Easy | Two Sum — complement lookup |
| [medium_longest_consecutive_sequence.py](practice/lists/hashmap/medium_longest_consecutive_sequence.py) | Medium | Longest consecutive streak — O(n) set trick |
| [medium_subarray_sum_equals_k.py](practice/lists/hashmap/medium_subarray_sum_equals_k.py) | Medium | Count subarrays summing to k |
| [medium_top_k_frequent_elements.py](practice/lists/hashmap/medium_top_k_frequent_elements.py) | Medium | Top K frequent elements — bucket sort |

#### `prefix_suffix/` — prefix tables and equilibrium queries
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_range_sum_queries.py](practice/lists/prefix_suffix/easy_range_sum_queries.py) | Easy | O(1) range-sum queries |
| [easy_find_pivot_index.py](practice/lists/prefix_suffix/easy_find_pivot_index.py) | Easy | Equilibrium / pivot index |
| [medium_product_except_self.py](practice/lists/prefix_suffix/medium_product_except_self.py) | Medium | Product of array except self |

#### `sliding_window/` — fixed and variable window over a stream
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_first_negative_in_window.py](practice/lists/sliding_window/easy_first_negative_in_window.py) | Easy | First negative integer in every window of size k |
| [easy_max_average_fixed_window.py](practice/lists/sliding_window/easy_max_average_fixed_window.py) | Easy | Maximum average subarray of fixed length k |
| [medium_longest_substring_no_repeat.py](practice/lists/sliding_window/medium_longest_substring_no_repeat.py) | Medium | Longest substring without repeating characters |
| [medium_min_size_subarray_sum.py](practice/lists/sliding_window/medium_min_size_subarray_sum.py) | Medium | Minimum-length subarray with sum ≥ target |
| [medium_max_consecutive_ones_flip_k.py](practice/lists/sliding_window/medium_max_consecutive_ones_flip_k.py) | Medium | Longest run of 1s with at most k flips |

#### `two_pointers/` — converging or advancing left/right pointers
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_merge_two_sorted_lists.py](practice/lists/two_pointers/easy_merge_two_sorted_lists.py) | Easy | Merge two sorted lists |
| [easy_move_zeroes.py](practice/lists/two_pointers/easy_move_zeroes.py) | Easy | Move all zeros to the end |
| [easy_remove_duplicates_sorted.py](practice/lists/two_pointers/easy_remove_duplicates_sorted.py) | Easy | Remove duplicates from sorted list |
| [easy_remove_element_in_place.py](practice/lists/two_pointers/easy_remove_element_in_place.py) | Easy | Remove all instances of a value in-place |
| [easy_squares_of_sorted_array.py](practice/lists/two_pointers/easy_squares_of_sorted_array.py) | Easy | Sorted squares — two pointers O(n) |
| [medium_container_with_most_water.py](practice/lists/two_pointers/medium_container_with_most_water.py) | Medium | Max water container |
| [medium_three_sum.py](practice/lists/two_pointers/medium_three_sum.py) | Medium | All unique triplets summing to zero |
| [medium_trapping_rain_water.py](practice/lists/two_pointers/medium_trapping_rain_water.py) | Medium | Trap rain water — O(n) O(1) |

---

### Strings Practice

> **Folder:** [practice/strings/](practice/strings/)  |  **README:** [practice/strings/README.md](practice/strings/README.md)

#### `hashmap/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_is_anagram.py](practice/strings/hashmap/easy_is_anagram.py) | Easy | Frequency-count anagram check |
| [easy_first_non_repeating_char.py](practice/strings/hashmap/easy_first_non_repeating_char.py) | Easy | First unique character |
| [medium_isomorphic_strings.py](practice/strings/hashmap/medium_isomorphic_strings.py) | Medium | Bijection mapping — char-to-char |
| [medium_word_pattern.py](practice/strings/hashmap/medium_word_pattern.py) | Medium | Bijection mapping — char-to-word |

#### `sliding_window/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_max_vowels_fixed_window.py](practice/strings/sliding_window/easy_max_vowels_fixed_window.py) | Easy | Fixed-size window — max vowel count |
| [medium_character_replacement.py](practice/strings/sliding_window/medium_character_replacement.py) | Medium | Longest uniform substring with k replacements |
| [medium_longest_k_distinct.py](practice/strings/sliding_window/medium_longest_k_distinct.py) | Medium | Longest substring with ≤ k distinct chars |
| [medium_minimum_window_substring.py](practice/strings/sliding_window/medium_minimum_window_substring.py) | Medium | Shortest substring covering all chars of t |

#### `stack/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_valid_parentheses.py](practice/strings/stack/easy_valid_parentheses.py) | Easy | Bracket matching with a stack |
| [medium_simplify_unix_path.py](practice/strings/stack/medium_simplify_unix_path.py) | Medium | Path canonicalisation |

#### `two_pointers/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_valid_palindrome_normalized.py](practice/strings/two_pointers/easy_valid_palindrome_normalized.py) | Easy | Palindrome ignoring non-alnum characters |
| [easy_longest_common_prefix.py](practice/strings/two_pointers/easy_longest_common_prefix.py) | Easy | Longest shared prefix |
| [medium_reverse_words_trim_spaces.py](practice/strings/two_pointers/medium_reverse_words_trim_spaces.py) | Medium | Reverse word order, collapse spaces |

#### `greedy/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_longest_palindrome_buildable.py](practice/strings/greedy/easy_longest_palindrome_buildable.py) | Easy | Longest palindrome constructible from a char set |

#### `pattern_matching/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_strstr_first_occurrence.py](practice/strings/pattern_matching/easy_strstr_first_occurrence.py) | Easy | Naive O(n·m) substring search |
| [medium_kmp_search.py](practice/strings/pattern_matching/medium_kmp_search.py) | Medium | KMP — O(n + m) LPS-table search |

#### `prefix_suffix/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [medium_repeated_substring_pattern.py](practice/strings/prefix_suffix/medium_repeated_substring_pattern.py) | Medium | Is s made by repeating a substring? |
| [medium_encode_decode_strings.py](practice/strings/prefix_suffix/medium_encode_decode_strings.py) | Medium | Length-prefix codec |

#### Top-level (mixed / standalone)
| File | Topic |
|------|-------|
| [string_backspace_compare.py](practice/strings/string_backspace_compare.py) | Stack-simulate backspace typed strings |
| [string_decode_nested_repeats.py](practice/strings/string_decode_nested_repeats.py) | Decode compressed strings like `3[a2[bc]]` |
| [string_find_anagram_indices.py](practice/strings/string_find_anagram_indices.py) | All anagram substring indices |
| [string_group_anagrams.py](practice/strings/string_group_anagrams.py) | Group anagram words |
| [string_is_rotation_of_another.py](practice/strings/string_is_rotation_of_another.py) | Rotation check via doubled string |
| [string_longest_unique_substring.py](practice/strings/string_longest_unique_substring.py) | Longest substring with unique chars |
| [string_min_remove_to_make_parentheses_valid.py](practice/strings/string_min_remove_to_make_parentheses_valid.py) | Min bracket removals for validity |
| [string_rotate_by_k.py](practice/strings/string_rotate_by_k.py) | Rotate string by k positions |
| [string_run_length_encode.py](practice/strings/string_run_length_encode.py) | Run-length encoding / decoding |
| [string_stream_first_unique.py](practice/strings/string_stream_first_unique.py) | First unique char in a stream |
| [string_valid_palindrome_one_deletion.py](practice/strings/string_valid_palindrome_one_deletion.py) | Palindrome with at most one deletion |

---

### Dictionaries Practice

> **Folder:** [practice/dictionary/](practice/dictionary/)  |  **README:** [practice/dictionary/README.md](practice/dictionary/README.md)

#### `counting/` — frequency maps and counting logic
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_word_frequency_map.py](practice/dictionary/counting/easy_word_frequency_map.py) | Easy | Build word frequency map |
| [easy_anagram_check.py](practice/dictionary/counting/easy_anagram_check.py) | Easy | Anagram check via character counts |
| [easy_char_count_map.py](practice/dictionary/counting/easy_char_count_map.py) | Easy | Character frequency map + most-common char |
| [medium_top_k_frequent_words.py](practice/dictionary/counting/medium_top_k_frequent_words.py) | Medium | Top K frequent words |
| [medium_subarray_sum_k.py](practice/dictionary/counting/medium_subarray_sum_k.py) | Medium | Count subarrays summing to k |
| [medium_frequency_of_frequency.py](practice/dictionary/counting/medium_frequency_of_frequency.py) | Medium | Frequency-of-frequency distribution map |
| [medium_continuous_subarray_sum_divisible_k.py](practice/dictionary/counting/medium_continuous_subarray_sum_divisible_k.py) | Medium | Subarrays whose sum is divisible by k |

#### `lookup/` — fast key lookup / index mapping
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_first_unique_character_index.py](practice/dictionary/lookup/easy_first_unique_character_index.py) | Easy | First non-repeating character index |
| [easy_two_sum.py](practice/dictionary/lookup/easy_two_sum.py) | Easy | Two Sum via complement lookup |
| [easy_valid_parentheses.py](practice/dictionary/lookup/easy_valid_parentheses.py) | Easy | Balanced brackets via stack + dict |
| [medium_randomized_set.py](practice/dictionary/lookup/medium_randomized_set.py) | Medium | Insert / Delete / GetRandom O(1) |
| [medium_lru_cache.py](practice/dictionary/lookup/medium_lru_cache.py) | Medium | LRU Cache with OrderedDict |
| [medium_time_based_key_value_store.py](practice/dictionary/lookup/medium_time_based_key_value_store.py) | Medium | Time-stamped key-value store |
| [medium_four_sum_count.py](practice/dictionary/lookup/medium_four_sum_count.py) | Medium | 4Sum II — meet-in-the-middle |

#### `transformations/` — dictionary reshape and nested transformations
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_invert_dictionary_unique_values.py](practice/dictionary/transformations/easy_invert_dictionary_unique_values.py) | Easy | Invert key↔value mapping |
| [medium_flatten_nested_dictionary.py](practice/dictionary/transformations/medium_flatten_nested_dictionary.py) | Medium | Flatten nested dict with dot-path keys |
| [medium_pivot_records.py](practice/dictionary/transformations/medium_pivot_records.py) | Medium | Pivot flat records to nested dict |
| [medium_deep_merge_dicts.py](practice/dictionary/transformations/medium_deep_merge_dicts.py) | Medium | Deep-merge two nested dicts |
| [medium_unflatten_dictionary.py](practice/dictionary/transformations/medium_unflatten_dictionary.py) | Medium | Reconstruct nested dict from dot-path flat map |

#### `grouping/` — group-by and multi-metric aggregation
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_group_records_by_field.py](practice/dictionary/grouping/easy_group_records_by_field.py) | Easy | Group records by a field (GROUP BY) |
| [medium_aggregate_by_group.py](practice/dictionary/grouping/medium_aggregate_by_group.py) | Medium | SUM / COUNT / AVG per group |
| [medium_group_anagrams.py](practice/dictionary/grouping/medium_group_anagrams.py) | Medium | Group anagram strings |
| [medium_running_aggregate_stream.py](practice/dictionary/grouping/medium_running_aggregate_stream.py) | Medium | Streaming group-by with live aggregates |

#### `merging/` — combining and joining dictionaries
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_merge_sum_dictionaries.py](practice/dictionary/merging/easy_merge_sum_dictionaries.py) | Easy | Merge dicts by summing values |
| [easy_dict_diff.py](practice/dictionary/merging/easy_dict_diff.py) | Easy | Diff two flat dicts |
| [easy_left_join_records.py](practice/dictionary/merging/easy_left_join_records.py) | Easy | LEFT OUTER JOIN on a shared key |
| [medium_inner_join_records.py](practice/dictionary/merging/medium_inner_join_records.py) | Medium | Hash join — INNER JOIN |
| [medium_full_outer_join_records.py](practice/dictionary/merging/medium_full_outer_join_records.py) | Medium | FULL OUTER JOIN |

---

### Sets Practice

> **Folder:** [practice/sets/](practice/sets/)  |  **README:** [practice/sets/README.md](practice/sets/README.md)

#### `hashset/` — membership, dedup, cycle detection
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_contains_duplicate.py](practice/sets/hashset/easy_contains_duplicate.py) | Easy | Membership check — detect any duplicate |
| [easy_remove_duplicates_preserve_order.py](practice/sets/hashset/easy_remove_duplicates_preserve_order.py) | Easy | Dedup while preserving insertion order |
| [easy_happy_number.py](practice/sets/hashset/easy_happy_number.py) | Easy | Cycle detection — sum-of-digit-squares loop |
| [easy_two_sum_complement.py](practice/sets/hashset/easy_two_sum_complement.py) | Easy | One-pass complement check |
| [medium_longest_consecutive_sequence.py](practice/sets/hashset/medium_longest_consecutive_sequence.py) | Medium | Longest run of consecutive integers |
| [medium_first_recurring_element.py](practice/sets/hashset/medium_first_recurring_element.py) | Medium | First duplicate in a stream |

#### `set_ops/` — union / intersection / difference / subset
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_intersection_of_two_lists.py](practice/sets/set_ops/easy_intersection_of_two_lists.py) | Easy | Unique intersection of two unsorted lists |
| [easy_is_subset.py](practice/sets/set_ops/easy_is_subset.py) | Easy | Subset check |
| [easy_symmetric_difference.py](practice/sets/set_ops/easy_symmetric_difference.py) | Easy | Symmetric difference (data reconciliation) |
| [medium_missing_elements_in_range.py](practice/sets/set_ops/medium_missing_elements_in_range.py) | Medium | Gap detection — missing IDs in a range |

#### `two_pointers/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_intersection_sorted_two_lists.py](practice/sets/two_pointers/easy_intersection_sorted_two_lists.py) | Easy | Unique intersection (sorted input) |
| [medium_three_sum_unique_triplets.py](practice/sets/two_pointers/medium_three_sum_unique_triplets.py) | Medium | All unique zero-sum triplets |

#### `sliding_window/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [medium_contains_nearby_duplicate.py](practice/sets/sliding_window/medium_contains_nearby_duplicate.py) | Medium | Duplicate within distance k |
| [medium_longest_unique_subarray.py](practice/sets/sliding_window/medium_longest_unique_subarray.py) | Medium | Longest subarray with all distinct values |
| [medium_min_window_k_distinct.py](practice/sets/sliding_window/medium_min_window_k_distinct.py) | Medium | Shortest subarray with ≥ k distinct values |

---

### Tuples Practice

> **Folder:** [practice/tuples/](practice/tuples/)  |  **README:** [practice/tuples/README.md](practice/tuples/README.md)

#### `sorting/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_sort_records_by_score_then_name.py](practice/tuples/sorting/easy_sort_records_by_score_then_name.py) | Easy | Multi-key sort on tuple records |

#### `hashmap/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [medium_equivalent_domino_pairs.py](practice/tuples/hashmap/medium_equivalent_domino_pairs.py) | Medium | Equivalent domino pairs via normalized tuple keys |

#### `unpacking/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [easy_closest_point_to_origin.py](practice/tuples/unpacking/easy_closest_point_to_origin.py) | Easy | Closest point to origin via tuple unpacking |

#### `intervals/`
| File | Difficulty | Topic |
|------|-----------|-------|
| [medium_merge_intervals.py](practice/tuples/intervals/medium_merge_intervals.py) | Medium | Merge overlapping intervals |

---

## How to Run

Run any tutorial or practice file directly:

```bash
# Tutorials
python "python tutorial/lists.py"
python "python tutorial/heaps.py"

# Practice problems
python "python tutorial/practice/lists/two_pointers/easy_move_zeroes.py"
python "python tutorial/practice/dictionary/counting/easy_word_frequency_map.py"
```

---

## Quick Reference — Complexity Cheat Sheet

| Data Structure | Access | Search | Insert | Delete | Space |
|----------------|--------|--------|--------|--------|-------|
| **List** | O(1) | O(n) | O(n)* | O(n) | O(n) |
| **Dictionary** | O(1) | O(1) | O(1) | O(1) | O(n) |
| **Set** | — | O(1) | O(1) | O(1) | O(n) |
| **Tuple** | O(1) | O(n) | — | — | O(n) |
| **Heap** | O(1)† | O(n) | O(log n) | O(log n) | O(n) |
| **Deque** | O(n) | O(n) | O(1)‡ | O(1)‡ | O(n) |

\* O(1) amortized for `append()`  
† O(1) for accessing the minimum element only  
‡ O(1) for operations at both ends
