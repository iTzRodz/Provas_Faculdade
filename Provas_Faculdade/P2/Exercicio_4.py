#A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programaem Python que gere a série até que o valor seja maior que 500.

primeiro_termo = 0
segundo_termo = 1
sequencia = 0

print("Sequência de Fibonacci")
print("_" * 40)

while sequencia < 501:
    sequencia = primeiro_termo + segundo_termo
    primeiro_termo = segundo_termo                
    segundo_termo = sequencia
    print(f"{sequencia}", end=' ') 


