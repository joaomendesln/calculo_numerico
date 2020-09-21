def f(x):
	return x ** 3 - 1.7 * x ** 2 - 12.78 * x - 10.08

def derivada_f(x):
	return 3 * x ** 2 - 3.4 * x - 12.78


i_max, cont = 15, 0

p = 0.1 # critério de parada
x = -0.5 # chutes iniciais: (-2, -1.5, 4)

for i in range(0, i_max):
	cont += 1
	print("x: ", x, " f(x): " , f(x))
	if f(x) < p and f(x) > -1 * p :
		print("Raiz aproximada:", x, "->", f(x))
		break
	
	x = x - (f(x) / derivada_f(x))

print("Iterações:", cont)
