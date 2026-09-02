salario = int(input("Digite o salário do funcionário: "))
porcentagem_aumento = int(input("Digite a porcentagem de aumento: "))
aumento = salario * (porcentagem_aumento / 100)
novo_salario = salario + aumento
print("O novo salário do funcionário é: R$", novo_salario)
