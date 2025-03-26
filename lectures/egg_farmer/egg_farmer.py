#!/usr/bin/env python3


def sort_the_eggs_out():

    try:
        eggs = int(input('Enter the number of eggs: '))
    except ValueError:
        print('Please enter a valid number of eggs.')
    else:
        if eggs <= 0:
            print('Please enter a positive number of eggs.')
        else:
            boxes_of_twelve = eggs // 12
            eggs_left = eggs % 12
            boxes_of_six = 1 if eggs_left >= 6 else 0
            eggs_left = eggs_left - 6 if boxes_of_six else eggs_left

            print(f'{eggs} egg{"s" if eggs > 1 else ""} is '
                  f'{boxes_of_twelve} box{"es" if boxes_of_twelve != 1 else ""} of 12 and '
                  f'{boxes_of_six} box{"es" if boxes_of_six != 1 else ""} of 6 '
                  f'and {eggs_left} egg{"s" if eggs_left != 1 else ""} left over for breakfast.')


if __name__ == '__main__':

    sort_the_eggs_out()
