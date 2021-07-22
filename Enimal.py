from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def papa(self):
        print("I am a parent")
class B(Animal):
    def papa(self):
        print("I am a child")

a = Animal()
b = B()

print(b.papa())