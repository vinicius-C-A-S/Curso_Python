velocidade = input(int("Qual a velocidade do carro? "))
if velocidade > 80:
    print('Você foi multado!')
    valor_multa = (velocidade - 80) * 5
    print(f'O valor da multa é: R${valor_multa:.2f}')
