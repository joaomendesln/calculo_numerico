f = open("pesos.txt", "r")

x_i = []
y_i = []
x_i2 = []
x_iy_i = []
count = 0

for l in f:
	x_i.append(float(l.split()[0]))
	y_i.append(float(l.split()[1]))
	x_i2.append(float(l.split()[0]) ** 2)
	x_iy_i.append(float(l.split()[0]) * float(l.split()[1]))
	count += 1

print('Somatórios:')
print(f'x_i = {sum(x_i)}')
print(f'y_i = {sum(y_i)}')
print(f'x_i ^ 2 = {sum(x_i2)}')
print(f'x_i * y_i = {sum(x_iy_i)}')
print(f'\nn = {count}\n')

print('Mínimos')
print(f'x_i: {min(x_i)}')
print(f'y_i: {min(y_i)}\n')

print('Máximos')
print(f'x_i: {max(x_i)}')
print(f'y_i: {max(y_i)}')

	

