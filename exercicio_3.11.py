preco = input("Digite o preço do produto: ")
porcentagem_desconto = input("Digite a porcentagem de desconto: ")
novo_preco = float(preco) - (float(preco) * float(porcentagem_desconto) / 100)
print("O novo preço do produto com desconto é: R$", round(novo_preco, 2))