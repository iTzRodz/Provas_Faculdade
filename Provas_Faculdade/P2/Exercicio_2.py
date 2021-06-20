#utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a."Telefonou para a vítima?"
# b."Esteve no local do crime?"
# c."Mora perto da vítima?"
# d."Devia para a vítima?"
# e."Játrabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no  crime.  Se  a  pessoa  responder  positivamente  a  2 questões  ela  deve  ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como"Assassino". Caso contrário, ele será classificado como "Inocente"

coleta_dados = []
positivo = 0
print("Olá, vou fazer algumas perguntas. Me responda apenas com sim ou nao")

for i in range(1):
    pergunta_1 = str(input("Telefonou para a vítima? "))
    pergunta_2 = str(input("Esteve no local do crime? "))
    pergunta_3 = str(input("Mora perto da vítima? " ))
    pergunta_4 = str(input("Devia para a vítima? "))
    pergunta_5 = str(input("Já trabalhou com a vítima? "))
    coleta_dados.append(pergunta_1)
    coleta_dados.append(pergunta_2)
    coleta_dados.append(pergunta_3)
    coleta_dados.append(pergunta_4)
    coleta_dados.append(pergunta_5)

print("_" * 60)
c = 0
for contador in range(len(coleta_dados)):
    if coleta_dados[c] == "sim":
        positivo +=1
    c +=1

if positivo == 2:
    print("Você está sendo classificado(a) como suspeito(a)")
elif positivo == 3 or positivo == 4:
    print("Você está sendo classificado como cúmplice")
elif positivo == 5:
    print("Você é o nosso assasino(a)")
else:
    print("Obrigado por responder, você é inocente")
