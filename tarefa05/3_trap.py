import math

def f(x):
	return x * math.sin(x)

# def f(x):
# 	return x * math.sin(2*x)

# k = int(input())

a = -5
b = 5
n = 6
h = (b - a) / n


x_0 = a
x_1 = a + h
result = 0

for i in range(0,n):
	print(f'x >= {round(x_0,6)} && x <= {round(x_1,6)} ?')
	print(f'({round(x_0,6)},{round(f(x_0),6)}) - ({round(x_1,6)}, {round(f(x_1),6)})')
	result += (h * (f(x_0) + f(x_1))) / 2
	x_0 = x_1
	x_1 = x_1 + h

print(result)