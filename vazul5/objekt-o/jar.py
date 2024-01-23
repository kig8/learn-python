class Jar:
    def __init__(self, capacity=12, deposit , withdraw):
        self._capacity = capacity
        self._deposit = deposit
        self._withdraw = withdraw
        self._size = 0
    def __str__(self):
        return  f'{"🍪" * self.size}'

    def deposit(self, n):
        self._deposit = n
        if self._size + self._deposit > self._capacity:
           raise ValueError
        self._size += self._deposit
        return self._size
    
    def withdraw(self, n):
        self._withdraw = n
        if self._withdraw > self._size:
            raise ValueError
        self._size -= self._withdraw
        return self._size

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("no - ")

        elif capacity > 12:
            raise ValueError("no more than 12")
        
        self._capacity = capacity

    @property
    def size(self):
      return self._size
    @size.setter
    def size(self, size):
        if size > self._capacity:
            raise ValueError
        self._size = size

