import numpy as np
import matplotlib.pyplot as plt


print("The 3x + 1 Brute force program.")

y = eval(input("Range of value of 'x' in 3x+1: "))
x = 0
for i in range(5,y+1):
    x = x + i
    print(x,end=' to ')
    xpoints = [x]
    while x != 1:
        if x % 2 != 0:
            x = (3*x) + 1
            xpoints.append(x)
        elif x % 2 == 0:
            x = x/2
            xpoints.append(x)
        print(x, end=' → ')
    if x == 1.0:
        print('Loop.')
    plt.plot(xpoints)
    print(xpoints)

plt.show()
