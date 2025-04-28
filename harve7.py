# 7)Se trocassemos as lâmpadas por outras mais econômicas de 4 kw/h, de quanto seria a economia?
# Dados
qtde_lampadas = 12
tempo_medio = 2  # horas por dia
dias_de_consumo = 20
preco_kwh = 0.57

# Consumo atual com lâmpadas de 6 kWh
potencia_lampada_6kwh = 6
gasto_mensal_6kwh = qtde_lampadas * tempo_medio * dias_de_consumo * preco_kwh * potencia_lampada_6kwh

# Consumo com lâmpadas de 4 kWh (mais econômicas)
potencia_lampada_4kwh = 4
gasto_mensal_4kwh = qtde_lampadas * tempo_medio * dias_de_consumo * preco_kwh * potencia_lampada_4kwh

# Economia
economia = round(gasto_mensal_6kwh - gasto_mensal_4kwh, 2)

# Resultados
print("Gasto mensal com lâmpadas de 4 kWh:", gasto_mensal_4kwh)
print("Economia com a troca:", economia)
