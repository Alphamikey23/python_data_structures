'''
Step 1 : Generate two single digit integer number1 number2
Step 2 : if number1 < number2, swap number1 with number2
Step 3 : Prompt the student to answer, "What is number1 - number2?
Step 4 : Check the student's answer and display whether the answer is correct.'''

import random

#1. Generate two random single-digit integers

number1 = random.randint(0,9)
number2 = random.randint(0,9)

if number1 < number2:
    number1, number2 = number2, number1

answer = int(input("What is " +str(number1) + " - " + str(number2) + "? "))


if number1 - number2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.")
    print(number1, '-', number2, "is", number1-number2)

