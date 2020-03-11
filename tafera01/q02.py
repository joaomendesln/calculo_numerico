import math

# q02 - parte 1
def derivada_f(x):
  return math.cos(x) -  x * math.sin(x)

def f(x):
  if x == 0:
    return 1
  if x > 0:
    return f(x - 1) + derivada_f(x - 1)
  else:
    return f(x + 1) - derivada_f(x + 1)


for x in range(-6,7,1):
  print (round(f(x),2))

  # q02 - parte 2
def fat(x):
  if x <= 1:
    return 1
  return x * fat(x - 1)

def derivada_impar_f(k):
  return (-1)**((k-1)/2) * k * math.cos(0) + (-1)**((k+1)/2) * 0 * math.sin(0)

def funcao_somatorio(x):
  f_soma = 0

  for n in range(0,13,1):
    if n % 2 == 0:
      f_soma += 0
    else:
      f_soma += (derivada_impar_f(n)*(x)** n) / fat(n)

  return f_soma

# COMANDOS GNUPLOT
# derivada_impar_f(k)=(-1) ** ((k-1)/2) * k * cos(0)
# funcao_somatorio(x) = sum[n=0:13] (int(n)%2==0) ? 0 : (derivada_impar_f(int(n)) * (x ** int(n))) / int(n)!
