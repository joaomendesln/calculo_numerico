def f(x):
	return x ** 3 - 1.7 * x ** 2 - 12.78 * x - 10.08
 
i_max, cont = 15, 0

p = 0.1 # critério de parada
a, b = -5, 5 # intervalo
m = (a+b)/2 

for i in range (0, i_max):
	cont += 1
	print("a: ", a, "  b: ", b, " ponto médio: ", m, " f(a): ", f(a), " f(b): ", f(b), " f(m): ", f(m))
	
	if f(m) < p and f(m) > -1 * p: 
		print("Raiz aproximada:", m, "->", f(m))
		break
	
	if f(a)*f(m) < 0:
		b = m
		m = (a+b)/2
	elif f(m)*f(b) < 0:
		a = m
		m = (a+b)/2

print("Iterações:", cont)