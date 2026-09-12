salario = float(int("Digite o salário do funcionário: "))
if salario <= 1.250:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"O novo salário do funcionário é: R${novo_salario:.2f}")
else:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f"O novo salário do funcionário é: R${novo_salario:.2f}")