#Permita ao usuário inserir o ano em um input e retorne a idade histórica conforme a imagem:

#image.png
ano = int(input("Digite o ano que deseja descobrir: "))

sigla = input("Digite 'a.c' para antes de Cristo e 'd.c' para depois de Cristo: ").lower()

if sigla == 'a.c':
    ano_aj = -ano
else:
    if sigla == 'd.c':
        ano_aj = ano
    else:
        ano_aj = None
        print("Valor incorreto. Digite 'a.c' para antes de Cristo e 'd.c' para depois de Cristo")

if ano_aj is None:
    era = "Valor incorreto"
    print(f"{era}")
else:
    if ano_aj <= -4000:
        era = "Pré-história"
        print(f"O ano {ano} {sigla} pertence ao período: {era}")
    else:
        if -4000 < ano_aj <= 476:
            era = "Antiguidade"
            print(f"O ano {ano} {sigla} pertence ao período: {era}")
        else:
            if 476 < ano_aj <= 1453:
                era = "Idade Média"
                print(f"O ano {ano} {sigla} pertence ao período: {era}")
            else:
                if 1453 < ano_aj <= 1789:
                    era = "Idade Moderna"
                    print(f"O ano {ano} {sigla} pertence ao período: {era}")
                else:
                    if ano_aj > 1789:
                        era = "Idade Contemporânea"
                        print(f"O ano {ano} {sigla} pertence ao período: {era}")
                    else:
                        era = "Ano inválido"
                        print(f"{era}")
