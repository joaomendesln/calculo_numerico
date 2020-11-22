import math

def f(x):
	return x * math.sin(math.radians(x))

# def f(x):
# 	return x * math.sin(2 * x)

k = int(input())

a = -5
b = 5
# a = 0
# b = 9
n = 3 * k
h = ((b - a) / n) / 2


x_0 = a
x_2 = a + ((b - a) / n)
x_1 = x_0 + h

result = 0

for i in range(0,n):
	result += h * ((f(x_0) + 4 * f(x_1) + f(x_2)) / 3)
	x_0 = x_2
	x_2 = x_2 + ((b - a) / n)
	x_1 = x_0 + h

print(result)