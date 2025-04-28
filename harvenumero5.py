#Crie um código que permita inserir a quantidade de lâmpadas, consumo médio em kw/h, 
#quantidade de horas por dia e dias 
#por mês e retorne o valor da conta (considerando R$ 0,57).
qtde_lampadas = int(input("Digite a quantidade de lampadas usadas: "))
consumo_medio = int(input("Digite o consumo médio: "))
tempo_medio = int(input("Digite o tempo médio do equipamento ligado: "))
dias_de_consumo = int(input("Digite a qtde. de dias que o equip. passou ligado: "))
preco_kwh = float(input("Digite o custo por kw/h: "))

gasto_mensal = round((qtde_lampadas * consumo_medio * tempo_medio * dias_de_consumo *preco_kwh), 2)

print("O gasto mensal é de R$"+ str(gasto_mensal))

print("O gasto mensal é de R$", gasto_mensal)