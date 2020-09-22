def f(L):
	return 1 / ((900 - L ** 2) ** (1 / 2)) + 1 / ((400 - L ** 2) ** (1 / 2)) - 1 / 8

def nova_estimativa(x0, x1):
  return x1 - ((f(x1) * (x1 - x0)) / (f(x1) - f(x0)))


parar = False
cont = 0

p = 0.01 # critério de parada
x0, x1 = 16, 16.4 # chute inicial
x2 = nova_estimativa(x0,x1)

while not parar:
  cont += 1
  print("x: ", x2, " f(x): ", f(x2))
  if f(x2) < p and f(x2) > -1 * p: 
    print("Raiz aproximada:", x2, "->", f(x2))
    break

  x0 = x1
  x1 = x2
  x2 = nova_estimativa(x0,x1)

print("Iterações:", cont)