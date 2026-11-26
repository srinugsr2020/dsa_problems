"""Return an original middle node, choosing the second middle by default."""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def middle_by_counting(head, *, second=True):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    if not count:
        return None
    index = count // 2 if second else (count - 1) // 2
    for _ in range(index):
        head = head.next
    return head


def nodes(head):
    while head is not None:
        yield head
        head = head.next


def middle_by_indexing(head, *, second=True):
    items = list(nodes(head))
    if not items:
        return None
    index = len(items) // 2 if second else (len(items) - 1) // 2
    return items[index]


def middle_by_speed(head, *, second=True):
    if head is None:
        return None
    slow, fast = head, head if second else head.next
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
    return slow


if __name__ == "__main__":
    fourth = Node(1)
    third = Node(1, fourth)
    second_node = Node(1, third)
    first = Node(1, second_node)
    for solve in (middle_by_counting, middle_by_indexing, middle_by_speed):
        assert solve(first) is third
        assert solve(first, second=False) is second_node
        assert solve(second_node) is third
        assert solve(second_node, second=False) is third
        assert solve(third) is fourth and solve(third, second=False) is third
        assert solve(fourth) is fourth and solve(fourth, second=False) is fourth
        assert solve(None) is None and solve(None, second=False) is None
        assert tuple(nodes(first)) == (first, second_node, third, fourth)
