# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from defs import *

invalid_selection = False
while not invalid_selection:
    print('Please select which application you would like to run:')
    print('1. Diamond Pattern')
    print('2. Average of 3 numbers')
    print('3. Convert Miles to Kilometers')
    print('4. Convert Time to Seconds')
    print('5. Convert Triangle side length to Area')
    print('6. Kennel Script')
    print('7. Box Script')
    print('8. Other')

    print('Exit. Exit Application')
    selection = input('Selection: ')
    if selection == '1':
        print_diamond()
        input(print('Press enter to continue'))
    elif selection == '2':
        average_three()
        input(print('Press enter to continue'))
    elif selection == '3':
        convert_miles()
        input(print('Press enter to continue'))
    elif selection == '4':
        convert_seconds()
        input(print('Press enter to continue'))
    elif selection == '5':
        convert_triangle()
        input(print('Press enter to continue'))
    elif selection == '6':
        select_kennel()
        input(print('Press enter to continue'))
    elif selection == '7':
        box_selection()
        input(print('Press enter to continue'))
    elif selection == 'Exit':
        print('Exiting Application.')
        invalid_selection = True
    else:
        print('Invalid Selection, Exiting Application.')
        invalid_selection = True
# print_hi('PyCharm')
# print_diamond()
# average_three()
# convert_miles()
# convert_seconds()
# convert_triangle()
# Kennel.make_dog()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
