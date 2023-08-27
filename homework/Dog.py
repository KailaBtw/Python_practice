# define a dog class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # getter method
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    # setter
    def set_age(self, age):
        self.age = float(age)

    def set_name(self, name):
        self.name = name

    def age_in_dog_years(self):
        return self.age * 7

