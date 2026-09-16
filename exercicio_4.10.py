preco_a_pagar = float(input("Digite os kWh e o tipo de instalação: "))
if tipo_instalacao == "R":
    if faixa_consumo <=500:
        preco_a_pagar = faixa_consumo * 0.40
    elif faixa_consumo > 500 and faixa_consumo <= 1000:
        preco_a_pagar = faixa_consumo * 0.65 
if tipo_instalacao == "C":
    if faixa_consumo <= 1000:
        preco_a_pagar = faixa_consumo * 0.55
    elif faixa_consumo > 1000 and faixa_consumo <= 5000:
        preco_a_pagar = faixa_consumo * 0.60
if tipo_instalacao == "I":
    if faixa_consumo <= 5000:
        preco_a_pagar = faixa_consumo * 0.55
    elif faixa_consumo > 5000 and faixa_consumo <= 10000:
        preco_a_pagar = faixa_consumo * 0.60
    elif faixa_consumo > 10000:
        preco_a_pagar = faixa_consumo * 0.75