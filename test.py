class Cat:
    meow_count = 0

    def __init__(self, name, color):
        self.name = name
        self._meow_count = self.meow_count
        self._color = color
        self._change = 3

    def meow(self):
        self._meow_count += 1
        print("Meow")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, dye):
        if self._change > 0:
            self._color = dye
            self._change -= 1
        else:
            raise ValueError("Tökmindegy")

    @classmethod
    def class_meow(cls):
        cls.meow_count += 1


cat1 = Cat("Kofic", "black")
cat1.color = "brown"
print(cat1.color)
cat1.color = "red"
cat1.color = "red"
print(cat1.color)
