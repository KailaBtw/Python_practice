# define a dog class
class Dog:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # getter method
    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    # setter
    def set_age(self, age):
        self._age = float(age)

    def set_name(self, name):
        self._name = name

    def age_in_dog_years(self):
        return self._age * 7

