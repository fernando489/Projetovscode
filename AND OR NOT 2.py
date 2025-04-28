#Crie um código onde inserimos se o vegetal possui semente, flores, reprodução,
#frutos e vasos condutores e retornamos o grupo ao qual ela pertence.
sementes = input("O vegetal possui sementes?: (sim/não) ").lower()
flores = input("O vegetal possui flores?: (sim/não) ").lower()
reproducao = input("A reprodução do vegetal depende de água?: (sim/não) ").lower()
frutos = input("O vegetal possui frutos?: (sim/não) ").lower()
vaso_condutores = input("O vegetal possui vaso condutor?: (sim/não) ").lower()

if sementes == "não" and flores == "não" and reproducao == "sim" and frutos == "não" and vaso_condutores == "não":
  grupo = "O vegetal é uma Briófita do grupo das Criptógramas"
elif sementes == "não" and flores == "não" and reproducao == "sim" and frutos == "não" and vaso_condutores == "sim":
  grupo = "O vegetal é uma Pteridófita do grupo das Criptógramas"
elif sementes == "sim" and flores == "sim" and reproducao == "não" and frutos == "não" and vaso_condutores == "sim":
  grupo = "O vegetal é uma Gimnosperma do grupo das fanerógramas"
elif sementes == "sim" and flores == "sim" and reproducao == "não" and frutos == "sim" and vaso_condutores == "sim":
  grupo = "O vegetal é uma Angiosperma do grupo das fanerógramas"
else:
  grupo = "Vegetal desconhecido!"
print(grupo)
