#Faça uma calculadora que converta graus Celsius para Fahrenheit
valor_celsius = float(input("Digite a temperatura em graus Celsius: "))

valor_fahrenheit = str(round((valor_celsius * 1.8) + 32, 2))

print("A temperatura em Fahrenheit é:"  + valor_fahrenheit)