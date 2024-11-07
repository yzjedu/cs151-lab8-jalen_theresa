# Algorithm Document

### First function
- Purpose:  picking number of dice rolls
- Name: number of dice rolls
- Parameters: none
- Return: amount of rolls
- Algorithm: 
1. number_of_rolls = int(input('Enter number of rolls'))
2. While number_of_rolls does not equal int:
    a. number_of_rolls = int(input('Enter number of rolls'))
3. return number_of_dice_rolls 



### Second function
-  Purpose: sum of one dice roll
- Name: sum of dice roll
- Parameters: none
- Return: sum of the two dice
- Algorithm: 
1. import random
- dice_roll = random.randit(1,6) + random.randit(1,6)

third function
- Name: display
- Parameters: 
- 


### Fourth function
- Purpose: Adding a tally of total_of_dice to correct sum value
- Name: sum_list
- Parameters:  none
- Return: an asterisk next to correct sum
- Algorithm:
- While count does not equal number_of_dice_rolls:
    a. sum_of_two_dice()
    b. sum_list.append(sum_of_two_dice)
    c. count += 1

- Purpose: Adding a tally of total_of_dice to correct sum value
- Name: sum_list
- Parameters:  none
- Return: an asterisk next to correct sum
- Algorithm: 
  a. return(sum_list)





### Main function
- Purpose calling all functions and creating list 
- Name: Main
- Parameters:none
- Return: 
- Algorithm:
1. number_of_dice_rolls()
2. sum_of_dice_roll()
3. total_of_dice()
4. Return ('Thank you for using our program')
