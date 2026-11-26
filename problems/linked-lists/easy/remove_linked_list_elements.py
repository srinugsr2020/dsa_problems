"""Remove Linked Values

Problem:
Unlink every node with the target value from an acyclic list, keeping original
survivors in order. Return the new head or None.

Examples:
- Removing 0 from 0 -> 0 -> 4 -> 0 -> 9 -> 0 returns the original 4 -> 9 nodes.
- Removing 2 from 2 -> 2 returns None.

Approaches:
- Baseline: Collect surviving references.
- Python / standard library: Lazily filter and relink.
- Optimized: Use a sentinel to unlink in place.
"""


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


def remove_collected(head, target):
    kept = [node for node in nodes(head) if node.value != target]
    return relink(kept)


def remove_filtered(head, target):
    return relink(filter(lambda node: node.value != target, nodes(head)))


def remove_by_bypassing(head, target):
    sentinel = previous = Node(0, head)
    while previous.next is not None:
        candidate = previous.next
        if candidate.value == target:
            previous.next = candidate.next
        else:
            previous = candidate
    return sentinel.next


if __name__ == "__main__":
    for solve in (remove_collected, remove_filtered, remove_by_bypassing):
        second = Node(3, Node(0))
        first = Node(3, Node(0, Node(0, second)))
        head = Node(0, Node(0, first))
        assert solve(head, 0) is first
        assert first.next is second and second.next is None
        assert solve(Node(0, Node(0)), 0) is None
        assert solve(None, 0) is None
        tail = Node(-1)
        untouched = Node(1, tail)
        assert solve(untouched, 0) is untouched and untouched.next is tail
