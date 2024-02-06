height=int(input('what is your height? '))
bill = 0
if height>=3:
    print('can ride')
    age=int(input('what is your age? '))
    if age<12:
        bill = 150
        print('ticket price is 150 naira.')
    elif age<=18:
        bill = 250
        print('ticket price is 250 naira. ')
    else:
        bill = 500
        print('ticket price is 500 naira')

    want_photo= input ('do you want to take photosY/N? ')
    if want_photo == 'y' or want_photo == 'Y':
        bill = bill + 50
    print(f'your total bill is {bill} naira')
else:
    print("you can't ride boss")
print('thank you enjoy the ride')