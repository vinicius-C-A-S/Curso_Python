notas = [0, 0, 0, 0, 0, 0, 0]

soma = 0
x = 0

while x < 7:
    notas[x] = float(input("Nota %d: " % (x + 1)))
    soma += notas[x]
    x += 1

x = 0

while x < 7:
    print("Nota %d: %.2f" % (x + 1, notas[x]))
    x += 1

print("Média: %.2f" % (soma / x))
#A diferença entre append e extend, extend adiciona não
#aceita parâmetros que não sejam listas, se usar append com uma lista como parâmetro, em vez de adicionar os elementos da lista, ele adiciona a lista inteira como um único elemento.
#exemplo: 
# L = [4,5]
# L.append([1, 2, 3]) => [4,5,[1, 2, 3]]