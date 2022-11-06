class Dog:
    def func_dog(self):
        print("Dog")

class Cat:
    def func_cat(self):
        print("Cat")

class Animal(Dog,Cat):
    def func_animal(self):
        print("Animal")
        super().func_dog()

d = Animal()
d.func_cat()
d.func_animal()
#d.func_dog()