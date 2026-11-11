user_name = input('create user name:- ')
user_password= input('create password:- ')

def sign_in():
    return input('Enter your username:- ')
def get_password():
    return input('Enter your password:- ')
login_username=sign_in()
login_password = get_password()

if login_username == user_name and login_password == user_password:
    print('welcome')
else:
    print('wrong data' )