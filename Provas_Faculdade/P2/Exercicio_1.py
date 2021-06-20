#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programaem Python que leia as um conjunto indeterminado de temperaturas, e  informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

i = 0
contador = 0
litas_temperatura = []
while contador < 5:
    temperatura = float(input("Digite a temperatura atual: "))
    i += temperatura
    contador += 1
    litas_temperatura.append(temperatura)
litas_temperatura.sort()

media = i / 5 
print("_"*40)
print(f"Menor temperatura informada: {litas_temperatura[0]}°C\nTemperatura Maxima: {litas_temperatura[-1]}°C")
print("_"*40)
print(f"Media das temperaturas informadas: {media:.1f}°C")
