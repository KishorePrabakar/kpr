
# Program to check if a number is prime or not

num = int(input('meh '))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    for i in range(2, num):
        print(i)
        if (num % i) == 0:
            flag = True


# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


'''
box = [0]
x = 0
while x < 10**8:
    x = x + 1
    box.append(x)

for i in box:
    if i%'''

'''
n = infinite_num()
for i in n:
    print(n)
'''