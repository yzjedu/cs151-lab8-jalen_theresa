# Programmers:  Jalen and Theresa
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/6/24
# Lab Assignment: 8
# Problem Statement: Find out how many times a sum of two dice occur and output it using asteriks
# Data In: number of rolls
# Data Out: list of possible sum of rolls with asteriks next to each counting the amount of times each sum occurs
# Credits:In class



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
