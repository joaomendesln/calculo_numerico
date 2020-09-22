def g(x):
  return -1 * x ** 3 + 1.7 * x ** 2 + 13.78 * x + 10.08

def f(x):
  return x - g(x)


parar = False
cont = 0

p = 0.1 # critério de parada
x = -2 # ver as condições para escolher o chute certo

while not parar:
  cont += 1
  print("x: ", x, "  g(x): ", g(x), " f(x): ", f(x))

  if f(x) < p and f(x) > -1 * p:
    print("Raiz aproximada:", x, "->", f(x))
    break
  
  x = g(x)

print("Iterações:", cont)
