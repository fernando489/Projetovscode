#Digite o ano que deseja descobrir: 1522
#Digite 'a.c' para antes de Cristo e 'd.c' para depois de Cristo: d.c
#O ano 1522 d.c pertence ao período: Idade Moderna
ano = int(input("Digite o ano que deseja descobrir: "))

sigla = input("Digite 'a.c' para antes de Cristo e 'd.c' para depois de Cristo").lower()

if sigla == "a.c":
  ano_aj = - ano
else:
  if sigla == "d.c":
    ano_aj = ano
  else:
    ano_aj = None
    print("Valor incorreto. Digite 'a.c' para antes de Cristo e 'd.c' para depois de Cristo")

if ano_aj == None:
  era = "Valor incorreto"
  print(f"{era}")
elif ano_aj <= -4000:
  era = "Pré-história"
  print(f"O ano {ano} {sigla} pretence ao período: {era}")
elif -4000 < ano_aj <= 476:
  era = "Antiguidade"
  print(f"O ano {ano} {sigla} pretence ao período: {era}")
elif 476 < ano_aj <= 1453:
  era = "Idade Média"
  print(f"O ano {ano} {sigla} pretence ao período: {era}")
elif 1453 < ano_aj <= 1789:
  era = "Idade Moderna"
  print(f"O ano {ano} {sigla} pretence ao período: {era}")
elif ano_aj > 1789:
  era = "Idade Comtemporânea"
  print(f"O ano {ano} {sigla} pretence ao período: {era}")
else:
  era = "Ano inválido"