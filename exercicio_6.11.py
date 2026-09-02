#Estrutura for é parecida com while, mas a cada repetição utiliza um elemento diferente da lista.
#exemplo: L=[8,9,15]
#         for e in L:
#           print(e) 
#geralmente utilizamos for quando queremos processar um a um os elementos de uma lista, tupla ou string.
#while é indicado para repetições nas quais não sabemos ainda quantas vezes vamos repetir ou onde manipulamos os índices de forma não sequencial.
#modificar esse exercício
L= []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)
x = 0
while x < len(L):
    print(L[x])
    x += 1

L = []

while True:
    n = int(input("Digite um número (0 sai):"))

    if n == 0:
        break

    L.append(n)

for e in L:
    print(e)
