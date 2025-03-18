#!/usr/bin/env python3

if __name__ == '__main__':

    price = int(input('Enter the price to be paid: '))
    paid = int(input('Enter the amount paid: '))

    change = paid - price
    print()
    print('Change Required: ')

    if change >= 200:
        print(f'£2: {change // 200}')
        change %= 200

    if change >= 100:
        print(f'£1: {change // 100}')
        change %= 100

    if change >= 50:
        print(f'50p: {change // 50}')
        change %= 50

    if change >= 20:
        print(f'20p: {change // 20}')
        change %= 20

    if change >= 10:
        print(f'10p: {change // 10}')
        change %= 10

    if change >= 5:
        print(f'5p: {change // 5}')
        change %= 5

    if change >= 2:
        print(f'2p: {change // 2}')
        change %= 2

    if change >= 1:
        print(f'1p: {change}')
