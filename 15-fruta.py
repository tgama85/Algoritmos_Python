#15.Fazer um sistema de Feira Livre(Deve imprimir 
# uma lista com as frutas e pedir para o 
# solicitante colocar o nome e selecionar a fruta 
# e depois deve imprimir o nome do solicitante e a 
# fruta)


print(f"Nossa Feira Livre tem disponível hoje:" #imprime as opções para o usuário
''' [0] laranja , [1] maçã , [2] pera, [3] uva''')  
solicitante = input("Digite seu nome para comprar: ")   #solicita nome do usuário
selecao = int(input("Digite o número da fruta que deseja adquirir? "))   #solicita a seleção do usuáiro
frutas = ["laranja","maçã","pera","uva"]    #lista de frutas
if selecao <= 3:   #verifica a seleção
        print(f"{solicitante} agradecemos por adquirir {frutas[selecao]}.") #resultado
        print("Volte sempre!")   
if selecao >= 4:
    print(f"{solicitante} não temos essa fruta.")   #caso usuário digite opção inválida

#2ª solução (alternativa)

# frutas = ["laranja","maçã","pera","uva"]    #lista de frutas
# print(f"Nossa Feira Livre tem disponível hoje: {frutas}.")  #print da lista
# solicitante = input("Digite seu nome para comprar: ")   #solicita nome do usuário
# selecao = input("Qual fruta deseja adquirir? ") #solicita fruta
# print(f"{solicitante} agradecemos por adquirir {selecao}.") #imprime solicitação do usuário