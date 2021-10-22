import random
import pyautogui
# import string

# chars = 'abcdefghijklmnopqrstuvxyz0123456789'
chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
chars_list = list(chars)
password  = pyautogui.password("Enter a password :")
guess_password = ""
while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))
    print("<==========="+ str(guess_password)+ "===========>")
    if(guess_password == list(password)):
        print("Your password is :"+ "".join(guess_password))
        break