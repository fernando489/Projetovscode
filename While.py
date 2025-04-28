#Crie uma lista que some os valores de input do usuário até que seja digitado 0. Quando o 0 for digitado, o 
#algoritmo deve finalizar e apresentar o total.
lista_usuario = []

while True:
  valor = int(input("Digite um valor para realizar a soma ou '0' para finalizar: "))
  if valor == 0:
    break
  else:
    lista_usuario.append(valor)

  total = sum(lista_usuario)

  print(f"O total dos valores digitados é: {total}")

