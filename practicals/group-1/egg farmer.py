# Your task is to write a Python program that will:

# Ask the farmer to enter how many eggs they have picked up this morning.

# Work out how many boxes of 12 eggs will be needed today.

# Work out if the farmer will also need a box of 6.

# Finally let the farmer know how many eggs they will 
# have left to cook for breakfast.



#!/usr/bin/env python3

if __name__ == '__main__':

    collected_eggs = int(input("How many eggs you've been collected: "))

    box_12 = collected_eggs//12
    remaining_eggs = collected_eggs % 12

    print(f"You will need {box_12} boxes of 12 eggs")
    print (f"You have {remaining_eggs} left after making up 12 eggs a box.")

    if remaining_eggs>=6:
        box_6 = 1
        breakfast_eggs = remaining_eggs - 6

    elif remaining_eggs<6:
        box_6 = 0
        breakfast_eggs = remaining_eggs 

    if box_6:
        print ("You will need 1 box of 6 eggs.")
    else:
        print ("You won't need a box of 6 eggs")

    print (f"You will have {breakfast_eggs} eggs left for breakfast.")

