f = open("barco.txt", "r")

x_i = []
y_i = []

for l in f:
	x_i.append(float(l.split()[0]))
	y_i.append(float(l.split()[1]))

print('Médias:')
print(f'x_i = {sum(x_i)/len(x_i)}')
print(f'y_i = {sum(y_i)/len(y_i)}')