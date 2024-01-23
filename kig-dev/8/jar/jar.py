class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        if self._size + n > self.capacity:
            raise ValueError("Too many cookie in the Jar")
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookie in the Jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("not a non-negative int")
        self._capacity = value

    @property
    def size(self):
        return self._size
