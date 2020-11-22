def b_c(c):
	return (1 + (1 + 13 * (c ** 2)) ** (1/2)) / 12

def v_b(b, c, v):
	return (3 * c * v - 2 * b * v) / (2 * b)

def trap_b(b, c, v):
	return ((v + v_b(b, c, v)) * b) / 2

def trap_c(c, v):
	return (3 * c * v) / 2

c = 5
b = b_c(c)
v = 3

print(f'{trap_b(b, c, v)} - {trap_c(c, v)}')