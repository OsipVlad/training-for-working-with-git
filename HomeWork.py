class Up:
    def act(self):
        return self.value.upper()

class Down:
    def act(self):
        return self.value.lower()

class ValClass:
    value = "fghrtj"

class Word(Up, ValClass):
    pass


w = Word()

print(w.act())