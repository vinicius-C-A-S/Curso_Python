primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (soma, subtração, multiplicação, divisão): ")
if operacao == "soma":
    resultado = primeiro_numero + segundo_numero
elif operacao == "subtração":
    resultado = primeiro_numero - segundo_numero
elif operacao == "multiplicação":
    resultado = primeiro_numero * segundo_numero
elif operacao == "divisão":
    if segundo_numero != 0:
        resultado = primeiro_numero / segundo_numero
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."
print("Resultado:", resultado)