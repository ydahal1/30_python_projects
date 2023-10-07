def check_password() -> None:
    password:str = None

    while True:
        password = input("Enter your password : ")
        if(len(password) > 0):
            break

    with open("/Users/yadhapdahal/Desktop/python/30_python_projects.py/passwords.txt", "r") as file:
        common_passwords: list[str] = file.read().splitlines()

    # print(common_passwords)
    for index, pw in enumerate(common_passwords):
        if(password ==  pw):
            print(f"❌ {password} is in the list of most commonly used passwords in {index + 1} position")
            return
    
    print(f" ✅ {password} is unique ")
    

if __name__ == "__main__":
    check_password()