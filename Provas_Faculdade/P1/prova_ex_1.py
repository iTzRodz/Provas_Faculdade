#– Crie um algoritmo em Python que peça a quantidade de dias, horas, minutos e segundos para o usuário, no final mostre o total em segundos. Dica de ouro: dias, horas, minutos e segundos são valores inteiros. Cada minuto tem 60 segundos, cada hora tem 3600 segundos.

i = 0

while (i < 1):
    dias = int(input("Quantidade em dias: "))
    horas = int(input("Quantidade em horas: "))
    minutos = int(input("Quantidade em minutos: "))
    segundos = int(input("Quantidades em segundos: "))
    i += 1

somaDia = (dias * 86400)
somaHora = (horas * 3600)
somaMinuto = (minutos * 60)
somaTot = somaDia + somaHora + somaMinuto + segundos
print("_" * 30)
print(f"Quantidade total em segundos:\n{somaTot} segundos")
