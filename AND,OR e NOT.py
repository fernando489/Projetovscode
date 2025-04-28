#A mega sena com maior prêmio da história foi o concurso 2237 que pagou 105 milhões. 
#Analise se o número inserido pelo 
#usuário através do input está entre os números sorteados 11 - 20 - 27 - 28 - 53 – 60,
#caso sim imprima "acertou", 
#caso contrário, imprima "não acertou". Sem usar listas.
numero_aposta = int(input("Digite o número apostado: "))

if numero_aposta == 11 or numero_aposta == 20 or numero_aposta == 27 or numero_aposta == 28 or numero_aposta == 53 or numero_aposta == 60:
  print("Acertou!")
else:
  print("Não acertou, tente novamente!")