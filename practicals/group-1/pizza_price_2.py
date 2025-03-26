#!/usr/bin/env python3


def pizza_area(diameter):
    from math import pi

    return pi * ((diameter / 2) ** 2)

if __name__ == '__main__':
    
    try:
        pizza_size = float(input('Enter the pizza size:  '))
        pizza_cost = float(input('Enter the pizza price: '))
    except ValueError:
        print('Error: Please enter numbers!')
    else:
        if pizza_cost < 0:
            print('Error: Cannot have a negative price!')
        elif pizza_size <= 0:
            print('Error: Cannot have a zero or negative sized pizza!')
        else:
            this_pizza_area = pizza_area(pizza_size)
            square_inch_cost = pizza_cost / this_pizza_area

            print(f'You are getting {this_pizza_area:.2f} square inches of pizza.')
            print(f'That is £{square_inch_cost:.2f} per square inch of pizza.')
