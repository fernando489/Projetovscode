#Crie uma lista com os valores 11,22,51,86,12,71 e 63.
#Calcule o valor médio da lista e imprima na tela.
valores_media = [11,22,51,86,12,71,63]
total = 0
for item in valores_media:
  total = total + item
media = round(total /len(valores_media), 2)
print(f"A média aritimética é:{media}")