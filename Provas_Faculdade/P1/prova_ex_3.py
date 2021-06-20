#– O hortifrúti Frutado está com uma promoção de compras por kg, assim quando qualquer cliente compra mais de 5kg de um fruta recebe um desconto no valor do kg.
#Escreva um algoritmo para ler a quantidade (em Kg) de laranjas e a quantidade (em Kg) de maças adquiridas, se o total passar de 5kg, deve-se considerar o valor com desconto, senão, o valor normal, no final apresente o valor a ser pago pelo cliente.

i = 0
laranja = float(input("Quantidade de laranja em Kg: "))
maca = float(input("Quantidade de maças em Kg: "))

while (i < 1):
    if maca <=5 and laranja <=5:
        maca *= 3.10
        laranja *= 3.80
        print(f"Preço maça: {maca:.2f}. Preço laranja: {laranja:.2f}")
    elif maca > 5 and laranja > 5:
        maca *= 2.50
        laranja *= 3.00
        print(f"Preço laranja: {laranja:.2f}. Preço maça: {maca:.2f}")
    elif maca <= 5 and laranja > 5: 
        maca *= 3.10
        laranja *= 3.00
        print(f"Preço laranja: {laranja:.2f}. Preço maça: {maca:.2f}")
    elif maca > 5 and laranja <=5:
        maca *= 2.50
        laranja *= 3.80  
        print(f"Preço laranja: {laranja:.2f}. Preço maça: {maca:.2f}")
    i += 1
    
