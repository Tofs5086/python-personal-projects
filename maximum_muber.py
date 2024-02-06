numbers = input('enter a list of numbers separated by a space')
numbers.split()
list_numbers = numbers.split()

amount_of_numbers = len(list_numbers)# this is to find the length of list_numbers using the len() function
for i in range(amount_of_numbers):# this will convert the individual strings to integers
    list_numbers[i]=int(list_numbers[i])

maximum_number = list_numbers[0] #this is to find the maximum number
for i in list_numbers:
    if i > maximum_number:
        maximum_number = i
print(f'the maximum of your numbers is {maximum_number}')

