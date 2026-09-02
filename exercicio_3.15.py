quantidade_fumada = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumando = int(input("Digite a quantidade de anos fumando: "))
expectativa_vida_perdida = (quantidade_fumada * anos_fumando * 10) / 1440  # 1440 minutos em um dia
print(f"Você perdeu aproximadamente {expectativa_vida_perdida:.2f} dias de vida devido ao tabagismo.")
