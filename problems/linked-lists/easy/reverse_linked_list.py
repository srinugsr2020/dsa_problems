"""Reverse Linked List

Problem:
Reverse the links of a possibly empty acyclic singly linked list. Return the old
tail without allocating any replacement data nodes.

Examples:
- 4 -> 8 -> 4 returns the old final 4 as head, then 8, then the old first 4.
- None returns None; a singleton returns the same node.

Approaches:
- Baseline: Detach tails one at a time.
- Python / standard library: Traverse collected nodes in reverse.
- Optimized: Flip links while traversing.
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def reverse_by_detaching_tail(head):
    sentinel = tail = Node(0)
    while head is not None:
        previous, last = None, head
        while last.next is not None:
            previous, last = last, last.next
        if previous is None:
            head = None
        else:
            previous.next = None
        tail.next = last
        tail = last
    return sentinel.next


def reverse_with_reversed(head):
    original = []
    while head is not None:
        original.append(head)
        head = head.next
    sentinel = tail = Node(0)
    for node in reversed(original):
        tail.next = node
        tail = node
    tail.next = None
    return sentinel.next


def reverse_links(head):
    previous = None
    while head is not None:
        successor = head.next
        head.next = previous
        previous, head = head, successor
    return previous


if __name__ == "__main__":
    for solve in (reverse_by_detaching_tail, reverse_with_reversed, reverse_links):
        last = Node(8)
        middle = Node(3, last)
        first = Node(8, middle)
        assert solve(first) is last
        assert last.next is middle and middle.next is first and first.next is None
        assert solve(last) is first and first.next is middle and middle.next is last
        assert last.next is None
        assert solve(None) is None
        only = Node(5)
        assert solve(only) is only and only.next is None
