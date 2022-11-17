class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Must be greater than zero")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Greater than capacity")
        if self.size + n > self.capacity:
            raise ValueError("Greater than capacity")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not Enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
