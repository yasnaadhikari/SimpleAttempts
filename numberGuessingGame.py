import random

random_number = int(random.randint(1,10))

attempts = int(input('Enter your value: '))


counter = 1


while (attempts != random_number):

    if(attempts>random_number):
        print("The actual number is lower than the guessed number")
    
    elif(attempts<random_number):
        print("The actual number is greater than the guessed number")
    
    attempts = int(input('Enter your value: '))
    counter += 1
print("Congratulations! You guessed it right. The correct guessed number is ",random_number)

print("The no of attempts were: ", counter)



