import random
import string


def get_user_info():
    print("Welcome to HNG Tech, please input your user details")
    first_name = input(">Type your first name: \n")
    last_name = input(">Type your last name: \n")
    email = input(">Type your email address: \n").lower()    
    user_info = [first_name, last_name, email]
    return user_info

def generate_password(user_info):
    chars = string.ascii_letters
    random_chars = "".join(random.choice(chars) for z in range(5))
    password = str(user_info[0][0:2] + user_info[1][-2:] + random_chars)
    return password



start = True
container = []

while start:
    user_info = get_user_info()
    pswrd = generate_password(user_info)
    print(f"Your password is {pswrd}")
    accept_pswrd = input("Are you satisfied with your password. Enter Yes or No \n").lower()
    
    password_loop = True
    
    while password_loop:        
        if accept_pswrd == 'yes':
            print(user_info)
        else: 
            print("Now you choose a password")
           
    
    