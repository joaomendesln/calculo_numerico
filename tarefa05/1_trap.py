import math

def f(x):
	return x * math.sin(math.radians(x))

a = -5
b = 5
n = 10
h = (b - a) / n


x_0 = a
x_1 = a + h
result = 0

for i in range(0,n):
	result += (h * (f(x_0) + f(x_1))) / 2
	x_0 = x_1
	x_1 = x_1 + h

print(result)