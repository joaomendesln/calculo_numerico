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
n = 2 * k
h = ((b - a) / n) / 3


x_0 = a
x_3 = a + ((b - a) / n)
x_1 = x_0 + h
x_2 = x_0 + 2 * h 
result = 0

for i in range(0,n):
	result += ((3 * h) / 8) * (f(x_0) + 3 * f(x_1) + 3 * f(x_2) + f(x_3))
	x_0 = x_3
	x_3 = x_3 + ((b - a) / n)
	x_1 = x_0 + h
	x_2 = x_0 + 2 * h 

print(result)