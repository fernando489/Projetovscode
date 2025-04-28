texto_filmes = '''1950 - "Crepúsculo dos Deuses" 1951 - "Um Lugar ao Sol" 1952 - "O Maior Espetáculo da Terra" 1953 - "A Malvada" 1954 - "Nasce uma Estrela" 1955 - "Ladrão de Casaca" 1956 - "A Volta ao Mundo em 80 Dias" 1957 - "A Ponte do Rio Kwai" 1958 - "Um Corpo que Cai" 1959 - "Ben-Hur" 1960 - "Psicose" 1961 - "Amor, Sublime Amor" 1962 - "Lawrence da Arábia" 1963 - "O Sol É para Todos" 1964 - "Música no Coração" 1965 - "Doutor Jivago" 1966 - "O Bom, o Mau e o Feio" 1967 - "A Primeira Noite de um Homem" 1968 - "2001: Uma Odisseia no Espaço" 1969 - "Butch Cassidy" 1970 - "Patton - Rebelde ou Herói?" 1971 - "Operação França" 1972 - "O Poderoso Chefão" 1973 - "O Exorcista" 1974 - "O Poderoso Chefão - Parte II" 1975 - "Um Estranho no Ninho" 1976 - "Rocky, um Lutador" 1977 - "Star Wars: Episódio IV - Uma Nova Esperança" 1978 - "O Franco Atirador" 1979 - "Kramer vs. Kramer" 1980 - "Touro Indomável" 1981 - "Carro Comando" 1982 - "E.T. - O Extraterrestre" 1983 - "Star Wars: Episódio VI - O Retorno do Jedi" 1984 - "O Exterminador do Futuro" 1985 - "De Volta para o Futuro" 1986 - "Platoon" 1987 - "Os Intocáveis" 1988 - "Rain Man" 1989 - "Nascido em 4 de Julho" 1990 - "Dança com Lobos" 1991 - "O Silêncio dos Inocentes" 1992 - "Os Imperdoáveis" 1993 - "A Lista de Schindler" 1994 - "Forrest Gump - O Contador de Histórias" 1995 - "Coração Valente" 1996 - "O Paciente Inglês" 1997 - "Titanic" 1998 - "Shakespeare Apaixonado" 1999 - "Beleza Americana" 2000 - "Gladiador" 2001 - "O Senhor dos Anéis: A Sociedade do Anel" 2002 - "Chicago" 2003 - "O Senhor dos Anéis: O Retorno do Rei" 2004 - "Menina de Ouro" 2005 - "O Segredo de Brokeback Mountain" 2006 - "Os Infiltrados" 2007 - "No Country for Old Men" 2008 - "Quem Quer Ser um Milionário?" 2009 - "Guerra ao Terror" 2010 - "O Discurso do Rei"'''

print(texto_filmes)
texto_filmes_sem_hifen = texto_filmes.replace(" - ","")

print(texto_filmes_sem_hifen)
texto_filmes_sem_espaco = texto_filmes_sem_hifen.replace('" ', '"')

print(texto_filmes_sem_espaco)
lista_final_filmes = texto_filmes_sem_espaco.split('"')

print(lista_final_filmes)
texto_filmes = '''1950 - "Crepúsculo dos Deuses" 1951 - "Um Lugar ao Sol" 1952 - "O Maior Espetáculo da Terra" 1953 - "A Malvada" 1954 - "Nasce uma Estrela" 1955 - "Ladrão de Casaca" 1956 - "A Volta ao Mundo em 80 Dias" 1957 - "A Ponte do Rio Kwai" 1958 - "Um Corpo que Cai" 1959 - "Ben-Hur" 1960 - "Psicose" 1961 - "Amor, Sublime Amor" 1962 - "Lawrence da Arábia" 1963 - "O Sol É para Todos" 1964 - "Música no Coração" 1965 - "Doutor Jivago" 1966 - "O Bom, o Mau e o Feio" 1967 - "A Primeira Noite de um Homem" 1968 - "2001: Uma Odisseia no Espaço" 1969 - "Butch Cassidy" 1970 - "Patton - Rebelde ou Herói?" 1971 - "Operação França" 1972 - "O Poderoso Chefão" 1973 - "O Exorcista" 1974 - "O Poderoso Chefão - Parte II" 1975 - "Um Estranho no Ninho" 1976 - "Rocky, um Lutador" 1977 - "Star Wars: Episódio IV - Uma Nova Esperança" 1978 - "O Franco Atirador" 1979 - "Kramer vs. Kramer" 1980 - "Touro Indomável" 1981 - "Carro Comando" 1982 - "E.T. - O Extraterrestre" 1983 - "Star Wars: Episódio VI - O Retorno do Jedi" 1984 - "O Exterminador do Futuro" 1985 - "De Volta para o Futuro" 1986 - "Platoon" 1987 - "Os Intocáveis" 1988 - "Rain Man" 1989 - "Nascido em 4 de Julho" 1990 - "Dança com Lobos" 1991 - "O Silêncio dos Inocentes" 1992 - "Os Imperdoáveis" 1993 - "A Lista de Schindler" 1994 - "Forrest Gump - O Contador de Histórias" 1995 - "Coração Valente" 1996 - "O Paciente Inglês" 1997 - "Titanic" 1998 - "Shakespeare Apaixonado" 1999 - "Beleza Americana" 2000 - "Gladiador" 2001 - "O Senhor dos Anéis: A Sociedade do Anel" 2002 - "Chicago" 2003 - "O Senhor dos Anéis: O Retorno do Rei" 2004 - "Menina de Ouro" 2005 - "O Segredo de Brokeback Mountain" 2006 - "Os Infiltrados" 2007 - "No Country for Old Men" 2008 - "Quem Quer Ser um Milionário?" 2009 - "Guerra ao Terror" 2010 - "O Discurso do Rei"'''

# Define texto_filmes_sem_hifen 
texto_filmes_sem_hifen = texto_filmes.replace(" - ","")
# Define texto_filmes_sem_espaco
texto_filmes_sem_espaco = texto_filmes_sem_hifen.replace('" ', '"')

lista_final_filmes = texto_filmes_sem_espaco.split('"')

print(lista_final_filmes)