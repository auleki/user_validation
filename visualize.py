import random
import string


def get_user_info():
    print("Welcome to HNG Tech, please input your user details")
    first_name = input(">Type your first name: \n")
    last_name = input(">Type your last name: \n")
    email = input(">Type your email address: \n").lower()    
    user_info = {
        "first_name": first_name, 
        "last_name": last_name,
         "email": email
        }
    return user_info

def generate_password(user_info):
    chars = string.ascii_letters
    random_chars = "".join(random.choice(chars) for z in range(5))
    password = str(user_info["first_name"][0:2].lower() + user_info["last_name"][-2:] + random_chars)
    return password


    


begin_process = True
container = []


while begin_process:
    user_info = get_user_info()
    pswrd = generate_password(user_info)
    print(f"Your password is {pswrd}")
    accept_pswrd = input("Are you satisfied with your password. Enter Yes or No \n").lower()
    password_loop = True
    
    while password_loop:        
        if accept_pswrd == 'yes':
            user_info["password"] = pswrd
            password_loop = False
            begin_process = False            
            print(user_info)
            
        elif accept_pswrd == "no": 
            username = user_info["first_name"]
            print(f"{username}now you get to choose a password")
            choosen_password = input("Your password must be more than 7 characters \n")
            pass_len = True
            
            while pass_len:
                if len(choosen_password) > 7:
                    user_info["password"] = choosen_password
                    container.append(user_info)
                    pass_len = False
                    password_loop = False
                    begin_process = False
                    
                else:
                    print("Your password is not more than 7 characters")
                    choosen_password = input("Choose a password more than 7 characters \n")
        else:
            print("Na Yes or No we say make you type")
            pass_len = False
            password_loop = False
            begin_process = False
                    
    new_user = input("Would you like to enter a new user? Yes or No \n").lower()

    if new_user == 'no':
        begin_process = False
        print(f"Here are your user details: \n {user_info}")                    

    elif new_user == 'yes':
        begin_process = True
    else:
        print("Na kuku yes or no we ask")

