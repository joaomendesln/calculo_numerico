def f(x):
  return x ** 3 - 1.7 * x ** 2 - 12.78 * x - 10.08

def nova_estimativa(x0, x1):
  return x1 - ((f(x1) * (x1 - x0)) / (f(x1) - f(x0)))

i_max, cont = 15, 0

p = 0.1 # critério de parada
x0, x1 = 4, 5 # chutes iniciais: (-3,-2), (-1.5,0), (4,5)
x2 = nova_estimativa(x0,x1)

for i in range (0, i_max):
  cont += 1
  print("x: ", x2, " f(x): ", f(x2))
  if f(x2) < p and f(x2) > -1 * p: 
    print("Raiz aproximada:", x2, "->", f(x2))
    break

  x0 = x1
  x1 = x2
  x2 = nova_estimativa(x0,x1)

print("Iterações:", cont)