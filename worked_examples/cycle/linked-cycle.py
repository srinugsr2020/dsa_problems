"""Detect a repeated node in a chain; equal values do not imply a cycle."""


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
