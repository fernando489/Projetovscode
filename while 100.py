soma = [ ]
while True:
  valor = float(input("Digite um valor: "))
  soma.append(valor)
  total = sum(soma)
  if total > 100:
    break
    print(f"A soma dos valores ultrapassou 100. O total é:{total}")