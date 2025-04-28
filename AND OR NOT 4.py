#Analise se o número inserido pelo usuário através do input está 
#entre os valores 11 - 20 - 27 - 28 - 53 – 60 do exercício da Mega Sena. 
#Caso sim imprima "acertou", 
#caso contrário, imprima "não acertou" usando listas.
lista_mega = [11, 20, 27, 28, 53, 60]

numero_usuario = int(input("Digite o número da sua aposta: "))

if numero_usuario in lista_mega:
  print("Você acertou!")
else:
  print("Você não acertou")
