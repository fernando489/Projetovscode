#Solicite ao usuário para que digite o estado onde ele mora. Se for igual a um dos estados do Sul, 
#imprima "Você mora no sul do Brasil", 
#senão, imprima "Você não mora no sul do Brasil".
estado = input("Digite o estado que você mora").title()

if estado == "Paraná" or estado == "Santa Catarina" or estado == "Rio Grande Do Sul":
  print("Você mora no sul do Brasil")

else:
  print("Você não mora no sul do Brasil")