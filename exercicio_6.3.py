L= [1,2,3,4,5,6,7]
V=[6,7,8,9,10]
terceira =[]
x = 0
while x < len(L):
    if L[x] not in terceira:
        terceira.append(L[x])
    x += 1
x = 0
while x < len(V):
    if V[x] not in terceira:
        terceira.append(V[x])
    x += 1
print(terceira)
#duas formas de remover elementos da lista
#del L[1] remove o elemento na posição 1
#del L[1:3] remove os elementos da posição 1 até a posição 3
#FIFO(First In First Out) - o primeiro elemento a entrar é o primeiro a sair
#modo .pop(0) remove o primeiro elemento da lista