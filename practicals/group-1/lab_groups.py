#!/usr/bin/env python3


GROUP_SIZE = 24

if __name__ == '__main__':

    try:
        number_of_students = int(input("How many students do you have? "))
    except ValueError:
        print("Please enter an integer.")
    else:
        if number_of_students >= 0:
            number_of_groups = number_of_students // GROUP_SIZE
            number_left_over = number_of_students % GROUP_SIZE

            if number_of_groups == 1:
                print(f'There will be {number_of_groups} group ', end='')
            else:
                print(f'There will be {number_of_groups} groups ', end='')

            if number_left_over == 1:
                print(f'and {number_left_over} student left over')
            else:
                print(f'and {number_left_over} students left over')
        else:
            print('Invalid number of students.')
