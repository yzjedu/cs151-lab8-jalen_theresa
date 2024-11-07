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