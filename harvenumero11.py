#Crie uma calculadora que converta cm em metros e vice versa de
#acordo com o input que o usuário insere (cm / m).
#Se o calor inserido não for nenhum dos dois, 
#avise o usuário que o tipo inserido está incorreto.
medida = float(input("Digite o valor que quer converter: "))

conversao = input("Digite 'cm' para centimetros ou 'm' para metros").lower()

if conversao =="cm":
  centimetros = medida * 100
  print(f"A medida em centimetros é: {centimetros} cm")
else:
  if conversao == "m":
    metros = medida / 100
    print(f"A medida em metros é: {metros} m")
  else:
    print("Tipo de convesão inválido!")