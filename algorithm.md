# Algorithm Document

### First function
- Purpose:  picking number of dice rolls
- Name: num_rolls
- Parameters: none
- Return: amount of rolls
- Algorithm: 
1. number_of_rolls = int(input('Enter number of rolls'))
2. While number_of_rolls does not equal int:
    a. number_of_rolls = int(input('Enter number of rolls'))
3. return number_of_dice_rolls 



### Second function
-  Purpose: sum of one dice roll
- Name: dice_roll_sum
- Parameters: none
- Return: sum of the two dice
- Algorithm: 
1. import random
- dice_roll = random.randint(2,12)

### Third function
- Purpose: creates the list for display function
- Name: my_list 
- Parameters: none
- Return: the list 
- Algorithm:
- total_list = [] * 12
- num_rolls = int(input('Please enter number of rolls'))
- 2. While number_of_rolls does not equal int:
    a. number_of_rolls = int(input('Enter a positive whole number for number of rolls'))
3. return number_of_dice_rolls 
- count = 0 
  - while count < num_rolls:
  i. total = random.randint(2,12)
  ii. total_list[total] = total list + 1
  iii. count = count + 1


### Fourth function
- Purpose: Adding a tally to dice_roll_sum to correct sum value
- Name: display
- Parameters: my_list
- Return: an asterisk next to correct sum
- Algorithm:
- For i in range(len(my_list)): 
  - i. if i > 1:
        i. output('sum of i', my_list[i] * '*')



### Main function
- Purpose calling all functions and creating list 
- Name: Main
- Parameters:none
- Return: display of asteriks next to each sum the number of times each occured 
- Algorithm:
1. num_rolls()
2. dice_roll_sum()
3. my_list
4. display
5. Return ('Thank you for using our program')
