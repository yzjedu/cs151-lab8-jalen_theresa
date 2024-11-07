# Lab Assignment: 8
# Problem Statement:Finding out how mab
#You need to design, write, and test a program that calculates the cost of buying flooring for your friend’s house.
# Your friend may need to test the cost with different designs, so your program should ask your friend if they want to check the cost of another design.
# Data In: Length and width of flooring in each room, and type of flooring being installed
# Data Out:  Total balance of all the rooms combined
# Credits: In Class



import random


import random



sum_list = [0] * 13
amount_of_rolls = int(input("How many rolls would you like to calculate?"))
count = 0

while count < amount_of_rolls:
    total = random.randint(2,12)
    sum_list[total] += 1
    count += 1


for i in (range(2,13)):
        print("Sum of", [i], sum_list[i] * "*")