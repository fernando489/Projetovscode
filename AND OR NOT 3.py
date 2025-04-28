#Desafio: Crie uma calculadora onde o usuário insere o valor 
#de renda mensal e o código realiza o cálculo de IR 2023 mensal:
renda_mensal = float(input("Digite o valor da sua renda mensal: "))

if renda_mensal <= 2259.20:
  imposto = 0
  print(f"O valor do importo de renda é: R${imposto}")
elif 2259.21 <= renda_mensal <= 2826.65:
  imposto = round(((renda_mensal * 0.075) - 168.44), 2)
  print(f"O valor do imposto de renda é: R${imposto}")
elif 2826.66 <= renda_mensal <= 3851.05:
  imposto = round(((renda_mensal * 0.15) - 381.44), 2)
  print(f"O valor do imposto de renda é: R${imposto}")
elif 3851.06 <= renda_mensal <= 4664.68:
  imposto = round(((renda_mensal * 0.225) - 662.77), 2)
  print(f"O valor do imposto de renda é: R${imposto}")
else:
  imposto = round(((renda_mensal * 0.275) - 896), 2)
  print(f"O valor do imposto de renda é: R${imposto}")
