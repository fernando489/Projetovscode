#Crie uma calculadora de massa corporal.
#O cálculo do IMC é realizando da seguinte forma: Peso / Altura * Altura:
#Obs.: Usar a função input() para capturar os dados do usuário
peso = float(input("Digite seu peso (em kg): "))

altura = float(input("Digite a sua altura e(em metros): "))

imc_bruto = round((peso / (altura * altura)), 2)

imc_aj = round((peso / (altura ** 2)), 2)

print("Seu IMC é: " + str(imc_aj,))