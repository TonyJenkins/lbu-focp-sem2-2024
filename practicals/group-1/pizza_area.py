#!/usr/bin/env python3


def pizza_area(diameter):
    from math import pi

    return pi * (diameter / 2) ** 2


if __name__ == '__main__':

    SMALL_PRICE = 15.99
    SMALL_DIAMETER = 9.5

    print(f'Small Pizza is {pizza_area(SMALL_DIAMETER - 0.5):.2f}"')
    print(f'Small Pizza is {SMALL_PRICE / pizza_area(SMALL_DIAMETER):.2f} per square inch.')

    MEDIUM_PRICE = 19.99
    MEDIUM_DIAMETER = 11.5

    print(f'Medium Pizza is {pizza_area(MEDIUM_DIAMETER - 0.5):.2f}"')
    print(f'Medium Pizza is {MEDIUM_PRICE / pizza_area(MEDIUM_DIAMETER):.2f} per square inch.')

    for diameter in [7, 9.5, 11.5, 13.5]:
        print(f'{diameter:2}\" pizza is {pizza_area(diameter):.2f} pizza area.')

    for diameter, price in [(7, 9.99), (9.5, 15.99), (11.5, 19.99), (13.5, 21.99)]:
        print(f'{diameter}" pizza is {price / pizza_area(diameter):.2f} per square inch.')

