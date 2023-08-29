from Dog import *
import time
import defs

class Kennel:
    dog1 = None

    @classmethod
    def make_dog(cls):
        name = input('Set Name: ')
        age = input('Set Age: ')
        cls.dog1 = Dog(name, age)
        print('Returning to kennel menu in ')
        defs.countdown(int(3))


    @classmethod
    def rename_dog(cls):
        old_name = cls.dog1.get_name()
        cls.dog1.set_name(input('Enter new name: '))
        print('Old Name:', old_name)
        print('New Name:', cls.dog1.get_name())

    @classmethod
    def change_age(cls):
        old_age = cls.dog1.get_age()
        cls.dog1.set_age(input('Enter new age: '))
        print('Dog Name:', cls.dog1.get_name())
        print('Old Age:', old_age)
        print('New Age:', cls.dog1.get_age())
        defs.countdown(int(3))


    @classmethod
    def check_age(cls):
        print('Dog Name:', cls.dog1.get_name())
        print('Age:', cls.dog1.get_age())
        print('Age in Dog Years:', str(cls.dog1.age_in_dog_years()))

    @classmethod
    def __str__(cls):
        return print('Dog Name:', cls.dog1.get_name(), '\nDog Age:', cls.dog1.get_age())

