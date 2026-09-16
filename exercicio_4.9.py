valor_da_casa = float(("Digite o valor da casa:"))
salario = float(("Digite o valor do seu salário:"))
quantidade_de_anos = int(("Digite a quantidade de anos que deseja pagar:"))
valor_da_prestacao = valor_da_casa / (quantidade_de_anos * 12)
if valor_da_prestacao > (salario * 0.3):
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")