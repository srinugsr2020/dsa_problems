"""Compare an acyclic chain's values without leaving changed links."""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def palindrome_half_stack(head):
    pending = []
    slow = fast = head
    while fast is not None and fast.next is not None:
        pending.append(slow.value)
        slow, fast = slow.next, fast.next.next
    if fast is not None:
        slow = slow.next
    while slow is not None:
        if pending.pop() != slow.value:
            return False
        slow = slow.next
    return True


def palindrome_by_slice(head):
    values = []
    while head is not None:
        values.append(head.value)
        head = head.next
    return values == values[::-1]


def reverse(head):
    previous = None
    while head is not None:
        successor = head.next
        head.next = previous
        previous, head = head, successor
    return previous


def palindrome_by_restoring(head):
    """Temporarily mutate the suffix; callers must allow exclusive access."""
    if head is None:
        return True
    seam = fast = head
    while fast.next is not None and fast.next.next is not None:
        seam, fast = seam.next, fast.next.next
    suffix = reverse(seam.next)
    left, right = head, suffix
    try:
        while right is not None:
            if left.value != right.value:
                return False
            left, right = left.next, right.next
        return True
    finally:
        seam.next = reverse(suffix)


if __name__ == "__main__":
    cases = (
        ([], True),
        ([5], True),
        ([2, 4, 4, 2], True),
        ([2, 4, 9, 4, 2], True),
        ([2, 4, 8, 2], False),
        ([2, 4, 9, 4, 0], False),
    )
    for solve in (palindrome_half_stack, palindrome_by_slice, palindrome_by_restoring):
        for values, expected in cases:
            chain = [Node(value) for value in values]
            head = None
            for node in reversed(chain):
                node.next, head = head, node
            before = [node.next for node in chain]
            assert solve(head) is expected
            assert [node.next for node in chain] == before
