#!/usr/bin/env python3


if __name__ == '__main__':

    collected_eggs = int(input("Enter the number of eggs you got this morning: "))

    box_12 = collected_eggs // 12
    remaining_eggs = collected_eggs % 12

    print (f"You will need {box_12} boxes of 12 eggs")

    print (f"And you will have {remaining_eggs} numbers of eggs remaining")

    if remaining_eggs >= 6:
        box_6 = 1
        breakfast_eggs = remaining_eggs - 6

    elif remaining_eggs < 6:
        box_6 = 0
        breakfast_eggs = remaining_eggs 

    if box_6:
        print ("You will also need 1 box of 6 eggs.")
    else:
        print ("You will not need a box of 6 eggs.")

    print (f"You will have {breakfast_eggs} eggs left for your breakfast!!")
    