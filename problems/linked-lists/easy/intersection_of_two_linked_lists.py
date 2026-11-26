"""Intersection of Two Linked Lists

Problem:
Given two acyclic linked lists, return their first shared node object or None.
Do not modify either list.

Examples:
- 7 -> X -> 4 and 8 -> 9 -> X -> 4 share the same node X; return X.
- Two separately allocated chains both containing 1 -> 2 have no intersection.

Approaches:
- Baseline: Compare node pairs.
- Python / standard library: Set of left identities.
- Optimized: Switch heads at the end.
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def nodes(head):
    while head is not None:
        yield head
        head = head.next


def intersection_nested(left, right):
    if left is None or right is None:
        return None
    for candidate in nodes(left):
        for node in nodes(right):
            if candidate is node:
                return candidate
    return None


def intersection_set(left, right):
    identities = {id(node) for node in nodes(left)}
    return next((node for node in nodes(right) if id(node) in identities), None)


def intersection_switch(left, right):
    a, b = left, right
    while a is not b:
        a = right if a is None else a.next
        b = left if b is None else b.next
    return a


if __name__ == "__main__":
    shared = Node(0, Node(4))
    left = Node(7, shared)
    right = Node(7, Node(8, shared))
    for solve in (intersection_nested, intersection_set, intersection_switch):
        assert solve(left, right) is shared
        assert solve(shared, right) is shared
        assert solve(right, right) is right
        assert solve(Node(7, Node(0, Node(4))), left) is None
        assert solve(None, left) is None
        assert solve(left, None) is None
        assert solve(None, None) is None
        assert left.next is shared and right.next.next is shared
        assert shared.next.value == 4 and shared.next.next is None
