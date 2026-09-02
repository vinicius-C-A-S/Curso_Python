ultimo = 10
fila = list(range(1, ultimo + 1))

sair = False

while not sair:
    print("\nExistem %d clientes na fila." % len(fila))
    print("Fila atual:", fila)

    operação = input("Operações (F, A ou S): ")

    x = 0

    while x < len(operação):

        if operação[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print("Cliente %d atendido." % atendido)
            else:
                print("Fila vazia! Ninguém para atender.")

        elif operação[x] == "F":
            ultimo += 1
            fila.append(ultimo)

        elif operação[x] == "S":
            sair = True
            break

        else:
            print("Operação inválida:", operação[x])

        x += 1
        #aqui entra o conceito de pilha LIFO(Last In First Out) que é o conceito de pilha, ou seja, o último elemento a entrar é o primeiro a sair.