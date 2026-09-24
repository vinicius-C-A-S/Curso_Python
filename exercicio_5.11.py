deposito_inicial = float(input("Digite o valor do depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros (em %): "))
montante = deposito_inicial
mes = 0
while mes < 24:
    mes += 1
    montante += rendimento
    rendimento = montante * (taxa_juros / 100)
    print(f"Mês {mes}: Montante acumulado: R$ {montante:.2f}, Rendimento: R$ {rendimento:.2f}")
total_rendimento = montante - deposito_inicial
print(f"\nTotal de rendimento após 24 meses: R$ {total_rendimento:.2f}")    
