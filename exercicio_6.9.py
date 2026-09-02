L = [15, 7, 27, 39]

p = int(input("Digite o valor a procurar: "))
v = int(input("Digite o segundo valor a procurar: "))

x = 0

while x < len(L):
    if L[x] == p or L[x] == v:
        break

    x += 1

if x < len(L):
    if L[x] == p:
        print("%d achado primeiro na posição %d" % (p, x))
    else:
        print("%d achado primeiro na posição %d" % (v, x))
else:
    print("Valores não encontrados")
    