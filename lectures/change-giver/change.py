#!/usr/bin/env python3


def coin_string(count_amount):
    return f'{count_amount}p' if count_amount < 100 else f'£{count_amount // 100}'


def give_change(coin, change_left):
    if change_left >= coin:
        print(f'{coin_string(coin):3}: {change_left // coin}')
        change_left %= coin

    return change_left


if __name__ == '__main__':
    price = int(input('Enter the price to be paid: '))
    paid = int(input('Enter the amount paid:      '))

    change = paid - price
    print()
    print('Change Required: ')

    coins = [200, 100, 50, 20, 10, 5, 2, 1]

    for coin in coins:
        change = give_change(coin, change)
