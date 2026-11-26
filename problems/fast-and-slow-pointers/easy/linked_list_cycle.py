"""Linked List Cycle

Problem:
Return whether following next links from the head ever reaches the same node
object twice. Leave all links unchanged.

Examples:
- A -> B -> C, with C.next equal to B, returns True.
- Two distinct nodes both storing 7, followed by None, return False.

Approaches:
- Baseline: Scan the visit log.
- Python / standard library: Set of node identities.
- Optimized: Floyd cycle detection.
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def has_cycle_history(head):
    visited = []
    current = head
    while current is not None:
        if any(previous is current for previous in visited):
            return True
        visited.append(current)
        current = current.next
    return False


def has_cycle_set(head):
    visited = set()
    current = head
    while current is not None:
        identity = id(current)
        if identity in visited:
            return True
        visited.add(identity)
        current = current.next
    return False


def has_cycle_floyd(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    last = Node(4)
    entry = Node(4, last)
    front = Node(4, entry)
    loop = Node(7)
    loop.next = loop
    for solve in (has_cycle_history, has_cycle_set, has_cycle_floyd):
        assert not solve(None)
        assert not solve(Node(7))
        assert not solve(front)
        assert solve(loop) and loop.next is loop
        last.next = entry
        assert solve(front)
        assert front.next is entry and entry.next is last and last.next is entry
        last.next = None
