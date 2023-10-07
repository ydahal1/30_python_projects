
import typing
import string
import itertools
import time

# check if pw is in common password list
def is_common_pw(pw : str) -> typing.Union[str,None]:
    with open("/Users/yadhapdahal/Desktop/python/30_python_projects.py/passwords.txt", "r") as file:
        common_pw = file.read().splitlines()
    for index, item in enumerate(common_pw):
        if item == pw:
            return f"Match found in commonly used passwords index - {index}"


def brute_force(pw: str, length: int, upper_case: bool= False, digits: bool = False, symbols:bool = False) -> typing.Union[str, None]:
    chars = string.ascii_lowercase

    if digits:
        chars += string.digits
    
    if symbols:
        chars += string.punctuation
    
    if upper_case:
        chars += string.ascii_uppercase
    
    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        word = ''.join(guess)

        if word == pw:
            return f"Cracked password '{word}' with length {length} in {attempts} attempts"

    

if __name__ == "__main__":
   start_time : float = time.perf_counter()
   common =  is_common_pw("Apple1254")
   if(common == None):
    for i in range(3,12):
        bf = brute_force("Apple1254", length=i, upper_case= True, digits = True, symbols = False)
        if bf != None:
            print(bf)
            break
   else:
    print(common)
   end_time : float = time.perf_counter()
   print(f"{round(end_time - start_time)} seconds")

