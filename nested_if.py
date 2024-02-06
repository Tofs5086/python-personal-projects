height=int(input('what is your height? '))

if height>=3:
    print('can ride')
    age=int(input('what is your age? '))
    if age<12:
        print('please pay 150 naira.')
    elif age<=18:
        print('please pay 250 naira. ')
    else:
        print('Please pay 500 naira')
else:
    print("you can't ride boss")
print('bye')