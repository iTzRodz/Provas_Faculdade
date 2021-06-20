#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programaem Python utilizando listas,que receba o nome e as  cinco  distâncias  alcançadas  pelo  atleta  em  seus  saltos  e  depois  informe  o nome, os saltos e a média  dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta:
#Rodrigo Curvêllo
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m
#Resultado final:
#Atleta: Rodrigo Curvêllo 
#Saltos: 6.5 -6.1 -6.2 -5.4 -5.3
#Média dos saltos: 5.9 m

saida = 1
while saida != 0:
    continuar = str(input("Dejesa inserir um nome? [s/n] "))
    saltos = 5
    lista_saltos = []    
    if continuar == "s":
        nome = str(input("Digite o nome do atleta: "))   
        while saltos > 0:
            n_saltos = float(input("Quantos metros foi seu salto: "))
            lista_saltos.append(n_saltos)
            saltos -= 1
            if saltos == 0:
                print("_"* 50)
                print(f"Atleta: {nome}")
                print(f"Primeiro Salto: {lista_saltos[0]} m\nSegundo Salto: {lista_saltos[1]} m\nTerceiro Salto: {lista_saltos[2]} m\nQuarto Salto: {lista_saltos[3]} m\nQuinto Salto: {lista_saltos[-1]} m")
                print("_"* 50)
                print(f"Resultado Final\nAtleta: {nome}\nSaltos:{lista_saltos} m")
                media = sum(lista_saltos) / 5          
                print(f"Média dos saltos: {media:.1f} m")
                print("_"* 50)
    else:
        saida = 0
        print("Programa finalizada.")
        
    