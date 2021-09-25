import random
import math

#taking range from user

lower = int(input('Ente the Lower bound: '))
upper = int(input('Enter the Upper bond: '))

x  = random.randint(lower,upper)
print("\n You have only",round(math.log(upper - lower +1,2)),"chances to guess the number\n")

count = 0

while count < math.log(upper - lower+1,2):
    count+= 1
    guess = int(input('Guess a Number: '))
    if x == guess:
        print('Congratulation you did it in',count,"try")
        break
    elif x > guess:
        print('Hint:- You Entered too Small')
    elif x < guess:
        print('Hint:- You Entered too high!')
if count > math.log(upper-lower+1,2):
    print('\nThe Number was',x)
    print('Better luck next time')