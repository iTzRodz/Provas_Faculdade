#Exercício 2 – Crie um algoritmo em Python que peça o valor de um produto e a porcentagem de desconto que ele receberá. Exiba o preço final do produto e o valor do desconto que foi dado.
i = 0
produto = float(input("Valor do produto: "))
while (i < 1):
    if produto <= 50.00:
        produto = produto - (produto * 0.20) 
        print(f"O produto recebeu 20% de desconto e agora custa: R${produto:.2f} reais")
    elif produto > 50.00 and produto <= 1000:
        produto = produto - (produto * 0.15) 
        print(f"O produto recebeu 15% de desconto e agora custa: R${produto:.2f} reais")
    else:
        produto =  produto - (produto * 0.05)
        print(f"O produto recebeu 5% de desconto e agora custa: R${produto:.2f} reais")
    i = i + 1
