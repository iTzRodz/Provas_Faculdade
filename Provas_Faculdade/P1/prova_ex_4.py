#Exercício 4 – Uma loja está aplicando um sistema de parcelas diferente, o cliente tem a liberdade de pagar quanto puder por mês enquanto não terminar a dívida. Seu papel é implementar um programa em Python que peça o total da dívida, o valor mínimo a ser pago por mês pelo cliente. E enquanto a dívida existir peça o valor a ser pago, para cada pagamento feito mostre o restante da dívida. No final mostre em quantas vezes a dívida foi paga.

i = 0
totalDivida = float(input("Digite o valor total da sua divida: "))

valorTot = totalDivida
saida = 1
while saida !=0:
    
    valorMin = float(input("Digite o valor minimo da parcela por mês: "))
    pagamentoMes = float(input("Valor da parcela: "))
    while pagamentoMes < valorMin:
        print("Por favor, inserir o valor minimo digitado acima!!")
        pagamentoMes = float(input("Valor da parcela: "))
    if pagamentoMes >=  valorMin:
        i += 1  
    while pagamentoMes > valorTot:
        print(f"Divida atual: R${valorTot}. Por favor insira um valor valido!")
        pagamentoMes = float(input("Valor da parcela: "))
    valorTot = valorTot - pagamentoMes
    if valorTot !=0:
        print(f"Divida atual: R${valorTot}.")
    elif valorTot ==0:
        print("Programa finalizado! ")
        print(f"Sua parcela terminou. Você demorou {i} meses para pagar.")
        saida = 0


