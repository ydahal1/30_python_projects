import random

# Roll dice number of specified times
def roll_dice(amount : int = 2) -> list [int]:
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range(amount):
        roll: int = random.randint(1,6)
        rolls.append(roll)
    
    return rolls

# Main method
def main():
    """
    Takes user input, tries to convert to int. if unable to convert throws error and asks for user input, if 
    input is exit - exits the program. if int is more than 0, rolls the dice
    """
    while True:
        user_input: str = input("Enter a number : ")

        try:
            if(user_input.lower() == "exit"):
                print("Goodbye !!")
                break

            else:
                input_int: int = int(user_input)
                result: list[int] = roll_dice(input_int)
                total = 0
                for i in result:
                    total += result[i-1]
                print(*roll_dice(int(user_input)), sep=", ")
                print(f"({total})")
                
        except ValueError:
            print("Invalid input")
            continue

# Run main method
if __name__ == '__main__':
    main()
