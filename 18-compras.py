#18.Fazer um sistema de compras (Deve mostrar um 
# dicionário com os objetos (Nome, Preço e Cor), 
# pedir o nome do usuário e fazer com o que o 
# usuário selecione um objeto e imprimir a compra 
# na tela)

#Solicita o nome do usuário
nome = input("Bem-vinde a nossa loja! Digite seu nome para começarmos: \n")
#dicionario com as opções de compra
dicionario_compras = {"Nome": "Blusa P","Preço": "R$29,90","Cor":"Azul"}, {"Nome": "Camiseta M","Preço": "R$39,90","Cor": "Florida"}, {"Nome": "Short M","Preço": "R$59,90","Cor": "Verde"}
#loop infinito
while True:
        contador = 0    #índice
        for lista in dicionario_compras:        #lista as opções comppras
                print(f"{contador} - {lista}")  #Imprime as opções comppras
                contador += 1   #incremento
        #imprime desistência de compra, fim do loop
        print(f"\nSe desistiu da compra, digite {contador} para sair!\n")       
        #solicita opção de compra
        compra = int(input(f"{nome} digite o número da sua opção de compra: \n"))
        if compra == 0:         #condição produto 1
                print(f"{nome} parabéns! Você acaba de adquirir uma Blusa P\n")
        elif compra == 1:       #condição produto 2
                print(f"{nome} parabéns! Você acaba de adquirir uma Camiseta M\n")
        elif compra == 2:       #condição produto 3
                print(f"{nome} parabéns! Você acaba de adquirir uma Camiseta M\n")
        elif compra == 3:       #condição sair da compra
                print(f"{nome} volte sempre!")
                break   #fim do loop
        elif compra >= 4:       ##condição opção de compra errada
                print(f"{nome} a opção não existe")