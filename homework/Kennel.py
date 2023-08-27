from Dog import *


class Kennel:
    @classmethod
    def make_dog(cls):
        name = input('Set Name: ')
        age = input('Set Age: ')
        dog1 = Dog(name, age)

        dog1.set_age(6)
        oldName = dog1.get_name()
        dog1.set_name(input('Enter new name: '))

        print('\nOld Name:', oldName)
        print('New Name:', dog1.name)
        print('Age:', dog1.age)
        print('Age in Dog Years:', dog1.age_in_dog_years())
        pass
