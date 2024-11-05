import random



sum_list = [] * 12
amount_of_rolls = int(input("How many rolls would you like to calculate?"))
count = 0
while count < amount_of_rolls:
    total = random.randint(2,12)
    sum_list.append(total)
    count += 1


for i in (sum_list):
        print("Sum of", [i], sum_list[i] * "*")
