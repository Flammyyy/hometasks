class Animal:
    name = ''
    species = ''
    def make_sound():
        print()

class Dog(Animal):
    def make_sound():
        print('Гав')

class Cat(Animal):
    def make_sound():
        print('Мяу')

Dog.make_sound()
Cat.make_sound()