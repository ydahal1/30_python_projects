import random

higher_number, lower_number = 10, 1
number: int = random.randint(lower_number, higher_number)
guess_count: int = 0
max_guess_allowed = 5
guess = None

while True:
    try:
        if (max_guess_allowed == guess_count):
            print("Game over !!!")
            break
        else:
            guess: int = int(input(f"Please enter a number between {lower_number} and {higher_number} : "))
            guess_count +=1
    except ValueError:
        print("Please enter a valid number")
        continue

    if(guess > higher_number or guess < lower_number):
        print("The number you provided is not in range")
    elif(guess > number):
        print("The number is smaller")
    elif(guess < number):
        print("The number is larger")
    else:
        print("Correct !!!")
        break


    
 