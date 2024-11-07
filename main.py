# Lab Assignment: 8
# Problem Statement:Finding out how mab
#You need to design, write, and test a program that calculates the cost of buying flooring for your friend’s house.
# Your friend may need to test the cost with different designs, so your program should ask your friend if they want to check the cost of another design.
# Data In: Length and width of flooring in each room, and type of flooring being installed
# Data Out:  Total balance of all the rooms combined
# Credits: In Class





import random

def sum_list_creation():
  return [0] * 13

def sum_of_dice(amount_of_rolls, sum_list):
    count = 0

    while count < amount_of_rolls:
        total = random.randint(2, 12)
        sum_list[total] += 1
        count += 1
def display(sum_list):
    for i in (range(2, 13)):
        print(f"Sum of {i}: {sum_list[i] * '*'}")

def main():
    amount_of_rolls = int(input("How many rolls would you like to calculate?"))
    while amount_of_rolls == str:
        amount_of_rolls = int(input("Invalid input please enter a positive integer for how many rolls would you like to calculate?"))
    sum_list = sum_list_creation()
    sum_list_creation()
    sum_of_dice(amount_of_rolls, sum_list)
    display(sum_list)

main()
