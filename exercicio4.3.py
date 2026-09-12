primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
terceiro_numero = int(input("Digite o terceiro número: "))
if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    print("O maior número é:", primeiro_numero)
elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    print("O maior número é:", segundo_numero)
else:
    print("O maior número é:", terceiro_numero)
     