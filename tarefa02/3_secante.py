def s(t):
	s0 = 300
	m = 0.25
	g = 32.17
	k = 0.1
	e = 2.71828
	return s0 - (((m * g) / k ) * t) + (((m ** 2) * g) /( k ** 2 )) * (1 - e ** ((-k * t) / m))

def nova_estimativa(x0, x1):
  return x1 - ((s(x1) * (x1 - x0)) / (s(x1) - s(x0)))


parar = False
cont = 0

p = 0.00001 # critério de parada
x0, x1 = 5.98, 6.02 # chute inicial
x2 = nova_estimativa(x0,x1)

while not parar:
  cont += 1
  print("x: ", x2, " s(x): ", s(x2))
  if s(x2) < p and s(x2) > -1 * p: 
    print("Raiz aproximada:", x2, "->", s(x2))
    break

  x0 = x1
  x1 = x2
  x2 = nova_estimativa(x0,x1)

print("Iterações:", cont)