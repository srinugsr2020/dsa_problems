"""Remove Duplicates from a Sorted Linked List

Problem:
In a sorted acyclic linked list, retain the first original node from each run of
equal values. Return the resulting head.

Examples:
- 1 -> 1 -> 2 -> 3 -> 3 becomes 1 -> 2 -> 3, keeping the first 1 and first 3.
- 7 -> 7 -> 7 becomes the original first 7 with no successor.

Approaches:
- Baseline: Collect nodes and keep run starts.
- Python / standard library: Group consecutive values.
- Optimized: Bypass duplicate successors.
"""

from itertools import groupby
from operator import attrgetter


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def nodes(head):
    while head is not None:
        node = head
        head = head.next
        yield node


def relink(kept):
    sentinel = tail = Node(0)
    for node in kept:
        tail.next = node
        tail = node
    tail.next = None
    return sentinel.next


def dedupe_collected(head):
    original = list(nodes(head))
    kept = [
        node
        for i, node in enumerate(original)
        if i == 0 or node.value != original[i - 1].value
    ]
    return relink(kept)


def dedupe_groups(head):
    groups = groupby(nodes(head), key=attrgetter("value"))
    return relink(next(run) for _, run in groups)


def dedupe_in_place(head):
    kept = head
    while kept is not None and kept.next is not None:
        if kept.value == kept.next.value:
            kept.next = kept.next.next
        else:
            kept = kept.next
    return head


if __name__ == "__main__":
    for solve in (dedupe_collected, dedupe_groups, dedupe_in_place):
        last = Node(10, Node(10))
        middle = Node(0, last)
        first = Node(-2, Node(-2, Node(-2, middle)))
        assert solve(first) is first
        assert first.next is middle and middle.next is last and last.next is None
        only = Node(7, Node(7, Node(7)))
        assert solve(only) is only and only.next is None
        distinct = Node(1, Node(2))
        second = distinct.next
        assert solve(distinct) is distinct and distinct.next is second
        assert solve(None) is None
