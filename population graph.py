import matplotlib.pyplot as plt

x = int(input('No. of rabbits: '))
y = int(input('No. of years: '))
r = float(input("Growth Rate: "))
x_points = []
for i in range(0, y+1):
    population = ((r * i) * (1-i))
    x_points.append(population)
    plt.plot(x_points)
print(x_points)
plt.show()
