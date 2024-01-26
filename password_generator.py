import random
#generate random letters
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("welcome to tofunmi's password generator")
n_letters= int(input('how many letters do you want in your password?\n'))
n_symbols = int(input('how many symbols do you want in your password?\n'))  #this is the code that will ask for the amount of letters, numbers and symbols
n_numbers = int(input('how many numbers do you want in your password?\n'))
password_list = []
for i in range(1,n_letters + 1): # this loop is used to generate a random amount of letters based on the amount the user picks
    char = random.choice(letters) # this is the code that will select the random letters from the letters list
    password_list += char  #this code will now concatenate the random letters with the password_list variable
for i in range(1,n_symbols + 1):
    char=random.choice(symbols)  # this is the code that will select the random symbols from the symbols list
    password_list += char #this code will now concatenate the random symbols with the password_list variable
for i in range(1,n_numbers + 1):
    char=random.choice(numbers)  # this is the code that will select the random numbers from the numbers list
    password_list += char  #this code will now concatenate the random numbers with the password_list variable
random.shuffle(password_list) #This code will now shuffle the elements in the list
password = '' #from here you'll now convert the elements in password_list to a string that will be held inside password variable
for i in password_list:
    password += i
print(password)