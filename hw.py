# PROBLEM 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15]

for number in numbers:
    if number ** 3 > 1000:
        break
    print(number ** 3)


#PROBLEM 2

for num in range(2,101):
    prime = True
    for i in range(2,num):
        if num % i == 0:
            prime = False
    if prime:
        print(num)


#PROBLEM 3
age = input('enter age as number: ')
real_age = int(age)

if real_age < 18:
    print('kids')
elif real_age >= 18 and real_age < 65:
    print('adults')
else:
    print('seniors')
