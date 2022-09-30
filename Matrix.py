import random
import string
import time

print("Matrix Generator")
end = int(input("How Long?  ")) * 10000
x = 0
while x != end:
    print(random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace), sep = '\n', end ='')
    x += 1


def message(string):
    for i in string:
        # printing each character of the message
        print(i, end="")

        # adding time delay of half second
        time.sleep(0.5)


msg = '\n' + 'THE END...' + '\n'
message(msg)

time.sleep(3.0)