"""Stably splice disjoint sorted lists, selecting left nodes first on ties."""

from heapq import merge
from itertools import chain
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


def relink(ordered):
    sentinel = tail = Node(0)
    for node in ordered:
        tail.next = node
        tail = node
    tail.next = None
    return sentinel.next


def merge_by_sorting(left, right):
    ordered = sorted(chain(nodes(left), nodes(right)), key=attrgetter("value"))
    return relink(ordered)


def merge_with_heapq(left, right):
    return relink(merge(nodes(left), nodes(right), key=attrgetter("value")))


def merge_by_splicing(left, right):
    sentinel = tail = Node(0)
    while left is not None and right is not None:
        if right.value < left.value:
            tail.next = right
            right = right.next
        else:
            tail.next = left
            left = left.next
        tail = tail.next
    tail.next = right if left is None else left
    return sentinel.next


if __name__ == "__main__":
    for solve in (merge_by_sorting, merge_with_heapq, merge_by_splicing):
        a3 = Node(5)
        a2 = Node(2, a3)
        a1 = Node(2, a2)
        b3 = Node(7)
        b2 = Node(2, b3)
        b1 = Node(-3, b2)
        result = solve(a1, b1)
        for expected in (b1, a1, a2, b2, a3, b3):
            assert result is expected
            result = result.next
        assert result is None
        assert solve(None, None) is None
        tail = Node(12)
        single_input = Node(1, tail)
        assert solve(None, single_input) is single_input
        assert solve(single_input, None).next is tail
