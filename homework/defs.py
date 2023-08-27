from decimal import Decimal, getcontext
import math
import datetime


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_diamond():
    print('\t\t\t    *')
    print('\t\t\t   ***')
    print('\t\t\t  *****')
    print('\t\t\t   ***')
    print('\t\t\t    *')


def average_three():
    first = int(input('Input first integer: '))
    second = int(input('Input second integer: '))
    third = int(input('Input third integer: '))
    print('The Average of ', first, ', ', second, ', and ', third, ' is ', first+second+third, sep='')


def convert_miles():
    miles = float(input('Input distance in Miles: '))
    kilometers = miles * 1.60935
    print(miles, 'miles converts to', round(kilometers, 2), 'kilometers')
    print(miles, 'miles converts to integer', math.trunc(kilometers), 'kilometers')


def convert_seconds():
    time = input('Input time in HH:MM:SS format\n')
    hours, minutes, seconds = time.split(':')
    print(hours, 'hours', minutes, 'minutes and', seconds, 'seconds is',
          int(datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds)).total_seconds()),
          'seconds.')


def convert_triangle():
    print('Given the three lengths of a triangle\'s sides, calculate the Area using Herrod\'s formula\n')
    side_a = float(input('Input length of first side: '))
    side_b = float(input('Input length of second side: '))
    side_c = float(input('Input length of third side: '))
    side_s = (side_a + side_b + side_c) / 2
    area = math.sqrt(side_s * (side_s - side_a) * (side_s - side_b) * (side_s - side_c))
    print('The Area of a triangle with sides of length', side_a, ",", side_b, ", and", side_c,
          "is", round(area, 2), 'square units.')






















