class Dog:
    def make_sound(self):
        print("Dog bark")


class Cat(Dog):
    def make_sound(self):
        print("Cat meows")


animal = Dog()
animal.make_sound()
