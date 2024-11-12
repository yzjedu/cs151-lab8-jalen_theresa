# Programmers:  Jalen and Theresa
# Course:  CS151, Dr. Zaleem Jembre Yalew
# Due Date: 11/6/24
# Lab Assignment: 8
# Problem Statement:Displaying the tally of the amount of each sum rolled by two die with asteriks
# Data In: number of rolls
# Data Out: Correct number of asteriks next to sum of the two die
# Credits: In Class





import random

def sum_list_creation():
  return [0] * 13

def sum_of_dice(amount_of_rolls, sum_list):
    count = 0

    while count < amount_of_rolls:
        total = random.randint(1, 6) + random.randint(1, 6)
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
