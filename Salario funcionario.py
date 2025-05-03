#3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no
#final uma mensagem.
#Ex:Nome do Funcionário: Maria do Carmo
#Salário: 1850,45
#O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.
nome = input("Qual é seu nome: ")
salário = float(input("Seu salário é de: "))
print (f"{nome}, seu é de R${salário:.2f}esse mês.")


