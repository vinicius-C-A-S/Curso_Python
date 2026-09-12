distancia = float(input("Digite a distância em kilometros: "))
if distancia < 0:
    valor = (distancia - 200)* 0.5
    print(f"o valor a ser pago é: R${valor:.2f}")
else:
    valor = (distancia)*0.45
    print(f"o valor a ser pago é: R${valor:.2f}")