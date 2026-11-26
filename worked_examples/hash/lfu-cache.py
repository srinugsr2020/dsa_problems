"""Evict by frequency, then by oldest access within that frequency."""

from collections import OrderedDict, defaultdict


class Baseline:
    def __init__(self, capacity):
        self.capacity = capacity
        self.entries = {}
        self.clock = 0

    def _record(self, key, value, frequency):
        self.clock += 1
        self.entries[key] = value, frequency, self.clock

    def get(self, key):
        if key not in self.entries:
            return -1
        value, frequency, _ = self.entries[key]
        self._record(key, value, frequency + 1)
        return value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.entries:
            self._record(key, value, self.entries[key][1] + 1)
            return
        if len(self.entries) == self.capacity:
            oldest = min(self.entries, key=lambda k: self.entries[k][1:])
            del self.entries[oldest]
        self._record(key, value, 1)


class Pythonic:
    def __init__(self, capacity):
        self.capacity = capacity
        self.entries = {}
        self.buckets = defaultdict(OrderedDict)
        self.lowest = 0

    def _promote(self, key, value, frequency):
        bucket = self.buckets[frequency]
        del bucket[key]
        if not bucket:
            del self.buckets[frequency]
            if self.lowest == frequency:
                self.lowest += 1
        self.entries[key] = value, frequency + 1
        self.buckets[frequency + 1][key] = None

    def get(self, key):
        if key not in self.entries:
            return -1
        value, frequency = self.entries[key]
        self._promote(key, value, frequency)
        return value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.entries:
            self._promote(key, value, self.entries[key][1])
            return
        if len(self.entries) == self.capacity:
            bucket = self.buckets[self.lowest]
            old_key, _ = bucket.popitem(last=False)
            del self.entries[old_key]
            if not bucket:
                del self.buckets[self.lowest]
        self.entries[key] = value, 1
        self.buckets[1][key] = None
        self.lowest = 1


class _Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.frequency = 1
        self.prev = self.next = self

    def unlink(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = self.next = None

    def append(self, node):
        """Insert at the most recent end of this sentinel's ring."""
        node.prev, node.next = self.prev, self
        self.prev.next = node
        self.prev = node


class Optimized:
    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = {}
        self.rings = defaultdict(_Node)
        self.lowest = 0

    def _promote(self, node):
        frequency = node.frequency
        ring = self.rings[frequency]
        node.unlink()
        if ring.next is ring:
            del self.rings[frequency]
            ring.prev = ring.next = None
            if self.lowest == frequency:
                self.lowest += 1
        node.frequency += 1
        self.rings[node.frequency].append(node)

    def get(self, key):
        node = self.nodes.get(key)
        if node is None:
            return -1
        self._promote(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._promote(node)
            return
        if len(self.nodes) == self.capacity:
            ring = self.rings[self.lowest]
            victim = ring.next
            victim.unlink()
            del self.nodes[victim.key]
            if ring.next is ring:
                del self.rings[self.lowest]
                ring.prev = ring.next = None
        node = _Node(key, value)
        self.nodes[key] = node
        self.rings[1].append(node)
        self.lowest = 1


if __name__ == "__main__":
    for Cache in (Baseline, Pythonic, Optimized):
        disabled = Cache(0)
        disabled.put(1, 10)
        disabled.put(1, 20)
        assert disabled.get(1) == -1

        cache = Cache(2)
        cache.put(2, 20)
        cache.put(1, 10)
        assert cache.get(1) == 10     # 1 is older at frequency two.
        cache.put(2, 22)             # Overwrite promotes 2 to frequency two.
        cache.put(3, 30)
        assert cache.get(1) == -1 and cache.get(2) == 22
        cache.put(4, 40)             # Newer 3 loses on frequency to 2.
        assert cache.get(3) == -1 and cache.get(4) == 40
