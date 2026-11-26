"""Implement put, get and remove without a built-in hash table."""


class Baseline:
    def __init__(self):
        self.entries = []

    def put(self, key, value):
        for i, (existing, _) in enumerate(self.entries):
            if existing == key:
                self.entries[i] = key, value
                return
        self.entries.append((key, value))

    def get(self, key):
        return next((value for existing, value in self.entries if existing == key), -1)

    def remove(self, key):
        for i, (existing, _) in enumerate(self.entries):
            if existing == key:
                self.entries.pop(i)
                return


class Pythonic:
    """Fixed-size separate chaining using ordinary Python lists."""

    def __init__(self, buckets=13):
        self.buckets = [[] for _ in range(buckets)]
        self.size = 0

    def _bucket(self, key):
        return self.buckets[key % len(self.buckets)]

    def put(self, key, value):
        bucket = self._bucket(key)
        for i, (existing, _) in enumerate(bucket):
            if existing == key:
                bucket[i] = key, value
                return
        bucket.append((key, value))
        self.size += 1

    def get(self, key):
        return next((value for existing, value in self._bucket(key) if existing == key), -1)

    def remove(self, key):
        bucket = self._bucket(key)
        for i, (existing, _) in enumerate(bucket):
            if existing == key:
                bucket[i] = bucket[-1]
                bucket.pop()
                self.size -= 1
                return


class Optimized(Pythonic):
    def __init__(self):
        super().__init__(8)

    def _resize(self, count):
        old = self.buckets
        self.buckets = [[] for _ in range(count)]
        for bucket in old:
            for entry in bucket:
                self._bucket(entry[0]).append(entry)

    def put(self, key, value):
        super().put(key, value)
        if self.size > len(self.buckets):
            self._resize(2 * len(self.buckets))

    def remove(self, key):
        super().remove(key)
        count = len(self.buckets)
        if count > 8 and self.size < count // 4:
            self._resize(count // 2)


if __name__ == "__main__":
    for Map in (Baseline, Pythonic, Optimized):
        table = Map()
        assert table.get(1) == -1
        table.put(1, 0)
        table.put(105, 91)
        table.put(209, 99)
        table.put(105, 5)
        table.remove(1)
        table.remove(313)
        assert (table.get(1), table.get(105), table.get(209)) == (-1, 5, 99)
        for key in range(300, 385):
            table.put(key, key + 1)
        for key in range(300, 385):
            assert table.get(key) == key + 1
            table.remove(key)
            assert table.get(key) == -1
        assert (table.get(105), table.get(209)) == (5, 99)
