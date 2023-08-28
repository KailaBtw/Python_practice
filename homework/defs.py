from decimal import Decimal, getcontext
import math
import datetime
from Kennel import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_diamond():
    print('\n\t\t\t    *')
    print('\t\t\t   ***')
    print('\t\t\t  *****')
    print('\t\t\t   ***')
    print('\t\t\t    *\n')


def average_three():
    first = int(input('\nInput first integer: '))
    second = int(input('Input second integer: '))
    third = int(input('Input third integer: '))
    print('\nThe Average of ', first, ', ', second, ', and ', third, ' is ', first + second + third, "\n", sep='')


def convert_miles():
    miles = float(input('\nInput distance in Miles: '))
    kilometers = miles * 1.60935
    print('\n', miles, 'miles converts to', round(kilometers, 2), 'kilometers\n')
    # print(miles, 'miles converts to integer', math.trunc(kilometers), 'kilometers\n')


def convert_seconds():
    time = input('\nInput time in HH:MM:SS format\n')
    hours, minutes, seconds = time.split(':')
    print(hours, 'hours', minutes, 'minutes and', seconds, 'seconds is',
          int(datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds)).total_seconds()),
          'seconds.\n')


def convert_triangle():
    print('\nGiven the three lengths of a triangle\'s sides, calculate the Area using Herrod\'s formula\n')
    side_a = float(input('Input length of first side: '))
    side_b = float(input('Input length of second side: '))
    side_c = float(input('Input length of third side: '))
    side_s = (side_a + side_b + side_c) / 2
    area = math.sqrt(side_s * (side_s - side_a) * (side_s - side_b) * (side_s - side_c))
    print('\nThe Area of a triangle with sides of length', side_a, ",", side_b, ", and", side_c,
          "is", round(area, 2), 'square units.\n')


def select_kennel():
    kennel_time = True
    while kennel_time:
        print('Please select which Kennel Application you would like to run:\n')
        print('1. Add Dog')
        print('2. Rename Dog')
        print('3. Change Age')
        print('4. Check Age')
        print('5. Print Dog Info')
        print('Exit. Return to main menu\n')
        choice = input('Selection: ')
        if choice == '1':
            Kennel.make_dog()
        elif choice == '2':
            Kennel.rename_dog()
        elif choice == '3':
            Kennel.change_age()
        elif choice == '4':
            Kennel.check_age()
        elif choice == '5':
            Kennel.__str__()
        elif choice == 'Exit':
            kennel_time = False
        else:
            print('Invalid Selection')


def countdown(__time):
    while __time > 0:
        mins, secs = divmod(__time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        __time -= 1
