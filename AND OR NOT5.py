#Analise se o nome do estado se refere a um dos estados do Paraguai. 
#Os estados do Paraguai são: Alto Paraguay, Alto Paraná, Amambay, Boquerón, Caaguazú,
#Caazapá, Canindeyú, Central,
#Concepción, Guairá, Itapúa, Cordillera, 
#Misiones, Ñeembucú, Paraguarí, Presidente Hayes e San Pedro

texto = "Alto Paraguay, Alto Paraná, Amambay, Boquerón, Caaguazú, Caazapá, Canindeyú, Central, Concepción, Guairá, Itapúa, Cordillera, Misiones, Ñeembucú, Paraguarí, Presidente Hayes, San Pedro"

print(type(texto))

texto_sem_espaco = texto.replace(", " , ",")

print(type(texto_sem_espaco))

lista_estados = texto_sem_espaco.split(",")

print(type(lista_estados))

print(lista_estados)

nome_estado = input("DIgite o nome de um estado Paraguaio: ").title()

if nome_estado in lista_estados:
  print("É um estado paraguaio!")
else:
  print("Não é um estado paraguaio")