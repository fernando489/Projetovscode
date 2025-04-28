#Faça uma calculadora que converta graus Celsius para Kelvin e Vice versa
#de acordo com o valor que o usuário
#inseriu no input e a letra para qual ele quer transformar (C ou K)
temperatura = float(input("Digite a temperatura: "))
unidade_origem = input("A temperatura está em (C)elsius ou (K)elvin? ").upper()
conversao = input("Deseja converter para (C)elsius ou (K)elvin? ").upper()

if unidade_origem == "K" and conversao == "C":
    celsius = temperatura - 273.15
    print(f"A temperatura em Celsius é: {celsius:.2f}°C")

elif unidade_origem == "C" and conversao == "K":
    kelvin = temperatura + 273.15
    print(f"A temperatura em Kelvin é: {kelvin:.2f}°K")

elif unidade_origem == conversao:
    print("A temperatura já está na unidade desejada.")

else:
    print("Opção inválida. Use 'C' para Celsius ou 'K' para Kelvin.")
