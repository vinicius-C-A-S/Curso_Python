dias = int(input("Digite o número de dias: "))
km_percorridos = float(input("Digite o número de quilômetros percorridos: "))
total_a_pagar = (dias * 60) + (km_percorridos * 0.15)
print(f"O total a pagar é: R$ {total_a_pagar:.2f}")