class LRU:
    def __init__(self, max_capacity=10):
        self._cache = {}
        self._max_capacity = max_capacity
        self._count = 0
        self._lower_bound = 0
        self._upper_bound = -1

    def get(self, key):
        key = self._lower_bound + key
        return self._cache[key] if key in self._cache else -1

    def put(self, value):
        if self._count < self._max_capacity:
            self._cache[self._count] = value
            self._count += 1
            self._upper_bound += 1
        else:
            self._cache[self._upper_bound + 1] = value
            del self._cache[self._lower_bound]
            self._upper_bound += 1
            self._lower_bound += 1

    def size(self):
        return self._count

    def max_capacity(self):
        return self._max_capacity

    def __str__(self):
        return str(self._cache)
