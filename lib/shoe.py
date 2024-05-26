#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.set_size(size)

    def set_size(self, size):
        if not isinstance(size, int):
            raise ValueError("size must be an integer\n")
        else:
            self._size = size

    def get_size(self):
        return self._size

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    size = property(get_size, set_size)