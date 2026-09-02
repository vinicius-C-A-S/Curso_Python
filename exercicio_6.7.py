parenteses = input("Digite os parenteses: ")

pilha = []
x = 0
erro = False

while x < len(parenteses):

    if parenteses[x] == "(":
        pilha.append("(")

    elif parenteses[x] == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            erro = True
            break

    x += 1 