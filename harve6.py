# 5Operadores matemáticos - Descoberta guiada
# 6)Considerando que uma lâmpada gasta em média 6 kw/h, ficando ligada em média 2hrs por dia por 20 dias. 
#E o valor pago por cada kw/h é de R$ 0,57 centavos. 
#Quanto estamos gastando por mês com as lâmpadas da sala?
qtde_lampadas = 12
tempo_medio = 2
dias_de_consumo = 20
preco_kwh = 0.57
potencia_lampada = 6
gasto_mensal_6kwh = round((qtde_lampadas * tempo_medio * dias_de_consumo * preco_kwh * potencia_lampada),2)
print(gasto_mensal_6kwh)