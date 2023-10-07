import string
import random
import secrets

class Secure_Password():
    def __init__(self) -> None:
        self.pw_length_prompt : str  = "How long do you want your password/s to be : "           
        self.pw_quantity: str = "Number of password you would like to generate: "
        self.pw_requires_digits_prompt : str  = "Do you want digits in your pw [Y/N]: "
        self.pw_requires_punctuation_prompt : str   = "Do you want punctuation in your pw [Y/N]: "
        self.pw_requires_uppercase_prompt: str =   "Do you want uppercase in your pw [Y/N]: "
        self.pw_requires_lowercase_prompt :str  = "Do you want lowercase in your pw [Y/N]: "
    
    # check if generated password  contains digits
    def contains_digits(self, pw : str) -> bool:
        for char in pw:
            if char in string.digits:
                return True
        
        return False
    
    # check if generated password contains punctuation
    def contains_punctuation(self, pw: str) -> bool:
        for char in pw:
            if char in string.punctuation:
                return True
        return False
    
    # check if pw contains upper case letter
    def contains_upper_case(self, pw: str) -> bool:
        for char in pw:
            if char in string.ascii_uppercase:
                return True
        
        return False

    # check if pw has lower case
    def contains_lower_case(self, pw: str) -> bool:
        for char in pw:
            if char in string.ascii_lowercase:
                return True

        return False

    # Get user input numbers
    def get_user_input_numbers(self, prompt:str) -> int:
        while True:
            try:
                user_input: int = int(input(prompt))
                return user_input
            except ValueError:
                print("Invalid number !! try again")
    
    # Get user input string [Y/N]
    def get_user_input_str(self, prompt:str) -> bool:
        while True:
                user_input: str = input(prompt)
                if user_input.lower() == "y":
                    return True
                elif user_input.lower() == "n":
                    return False
                else:
                    print("Invalid input, try again")

    # Generate list of random number that matches the requirement cout and that sums up to password length
    def generate_random_numbers(self, pw_length, requirement_count):
        count: int = 0

        while True:
            rand_numbers: list = []
            count +=1
            for i in range(requirement_count):
                rand_numbers.append(random.randint(1, pw_length))


            if(sum(rand_numbers)) == pw_length:
                break
        
        return rand_numbers

            
    # Generate password
    def generate_password(self) -> None:
        # Get user inputs
        pw_length = self.get_user_input_numbers(self.pw_length_prompt)
        while True:
            if pw_length < 4:
                print("ERRR !!! Password must be atleast 4 chars")
                pw_length = self.get_user_input_numbers(self.pw_length_prompt)
            else:
                break

        pw_quantity: int = self.get_user_input_numbers(self.pw_quantity)
        pw_requires_digits: str = self.get_user_input_str(self.pw_requires_digits_prompt)
        pw_requires_punctuation = self.get_user_input_str(self.pw_requires_punctuation_prompt)
        pw_requires_uppercase = self.get_user_input_str(self.pw_requires_uppercase_prompt)
        pw_requires_lowercase = self.get_user_input_str(self.pw_requires_lowercase_prompt)

        # PW equirements 
        requirements: dict = {"pw_requires_digits" : pw_requires_digits, 
                              "pw_requires_punctuation": pw_requires_punctuation, 
                              "pw_requires_uppercase": pw_requires_uppercase, 
                              "pw_requires_lowercase": pw_requires_lowercase}
        
        requirements:dict = {key:value for key, value in requirements.items() if value == True}
        
        for _ in range(pw_quantity):
            # Random numbers
            random_list: list= self.generate_random_numbers(pw_length,len(requirements))

            password_chars: str = ""

            for key in requirements:
                if(key ==  "pw_requires_digits"):
                    for _ in range(random_list[0]):
                        password_chars = password_chars + str(random.randint(0,9))
                    random_list.pop(0)


                if(key ==  "pw_requires_punctuation"):
                    for _ in range(random_list[0]):
                        password_chars = password_chars + random.choice(list(string.punctuation))
                    random_list.pop(0) 

                if(key ==  "pw_requires_uppercase"):
                    for _ in range(random_list[0]):
                        password_chars = password_chars + random.choice(list(string.ascii_uppercase))
                    random_list.pop(0) 

                if(key ==  "pw_requires_lowercase"):
                    for _ in range(random_list[0]):
                        password_chars = password_chars + random.choice(list(string.ascii_lowercase))
                    random_list.pop(0) 
                
            
            password_chars_list : list = list(password_chars)
            random.shuffle(password_chars_list)
            shuffled_password_chars : str = ''.join(password_chars_list)
       
            print(shuffled_password_chars )


# # check if generated password  contains digits
# def contains_digits( pw : str) -> bool:
#     for char in pw:
#         if char in string.digits:
#             return True
    
#     return False

# # check if generated password contains punctuation
# def contains_punctuation( pw: str) -> bool:
#     for char in pw:
#         if char in string.punctuation:
#             return True
#     return False

# # check if pw contains upper case letter
# def contains_upper_case( pw: str) -> bool:
#     for char in pw:
#         if char in string.ascii_uppercase:
#             return True
    
#     return False

# # check if pw has lower case
# def contains_lower_case( pw: str) -> bool:
#     for char in pw:
#         if char in string.ascii_lowercase:
#             return True

#     return False

# ## Generate password
# def generate_password(length: int, special_chars: bool, upper_case: bool) -> string:
#     combination : string = string.ascii_lowercase + string.digits

#     if special_chars:
#         combination += string.punctuation
    
#     if upper_case:
#         combination += string.ascii_uppercase

#     combination_length = len(combination)
#     new_password : str = ""

#     for _ in range(length):
#         new_password += combination[secrets.randbelow(combination_length)]

#     return new_password

if __name__ == "__main__":
    pg = Secure_Password()
    pg.generate_password()
    # for i in range(1, 50):
    #     new_pw = generate_password(length=50, upper_case=True, special_chars=True)
    #     specs: str = f"(L: {contains_lower_case(pw=new_pw)}, U: {contains_upper_case(new_pw)}, SC: {contains_punctuation(new_pw)}, NUM: {contains_digits(new_pw)})"
    #     print(new_pw, specs)