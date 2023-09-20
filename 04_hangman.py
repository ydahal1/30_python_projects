import random

fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
number_of_tries_allowed = 10

choosen_fruit:list = list(random.choice(fruits))
empty_choosen_fruit:list = ["_" for _ in choosen_fruit]

def replace(char : str):
    for i, item in enumerate(choosen_fruit):
        if (item == char):
            empty_choosen_fruit[i] = char


def main():
    tries: int = 0
    while True:
        print(' '.join(empty_choosen_fruit))

        if(tries == number_of_tries_allowed):
            print(f"GAME OVER !!!. The anser is {''.join(choosen_fruit)}" )
            break

        elif(choosen_fruit == empty_choosen_fruit):
            print("GOOD JOB - YOU WON !!")
            break
        
        else:
            print(f"{number_of_tries_allowed - tries} tries left")
            user_input: str = input("Enter an alphabet : ")
            replace(user_input)
            tries += 1

if __name__ == "__main__":
    main()
