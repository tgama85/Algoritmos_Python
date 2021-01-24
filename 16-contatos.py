#16.Fazer um sistema de Agenda de contatos 
# (Deve criar um dicionário com Nome, 
# Telefone e Endereço, Imprimir os dados do 
# dicionário, ser capaz de inserir e excluir 
# um contato)

#Solucão orientada pelo professor

# usuario = input("Bem-vinde! Digite seu nome:\n")
# lista_agenda = []
# opcoes = ["1 - Adicionar contato","2 - excluir contato","3 - Imprimir agenda", "4 - Sair"]

# #executa as instruções da agenda
# Loop infinito
# while True:
#     print(f"Olá {usuario}, digite o número da opção desejada: ")
#     for opcao in opcoes:
#         print(opcao)
#         instrucao = int(input(""))
#     if instrucao == 1: 
#         nome = input("Nome: \n").strip()
#         telefone = input("Telefone: \n").strip()
#         endereco = input("Endereço: \n").strip()
#     ##Criando um dicionário com os dados da agenda
#         agenda = {
#             "nome": nome,
#             "telefone": telefone,
#             "endereco": endereco
#         }
#         lista_agenda.append(agenda) #Inserindo o dicionário na lista (Escopo Global)
#         print("Contato inserido")
    
#     #exclui dados da agenda, mas mantém agenda
#     elif instrucao == 2:
#         while True:
#             indice = 0
#             for item in lista_agenda:
#                 print(f"{indice} - {item}")
#                 indice += 1 
#                 print(f"Selecione {indice} para sair...")
#                 indice_selecionado = input("Digite o número do item da agenda que deseja excluir?\n") 
#                 if indice_selecionado.isnumeric(): #Verifica se é numérico
#                     indice_selecionado_convertido = int(indice_selecionado) #converte para inteiro
#                     if indice_selecionado_convertido in range(0, indice): #Verifica o número convertido no range da lista
#                         print("Quase lá...") #Avise que está apagando
#                         item_selecionado = lista_agenda.pop(indice_selecionado_convertido) #Apaga o item
#                         print(f"Seu item {item_selecionado} foi excluído!") #Item foi excluído
#                         break #Sai do loop
#                     elif indice_selecionado_convertido == indice: 
#                         break 
#                     else: 
#                         print("Essa opção não existe !") 
#                 else: 
#                     print("Opção incorreta ou inexistente!") 
#     #adiciona contatos sem espaços desnecessários

#     #imprime a agenda
#     elif instrucao == 3:
#         print(lista_agenda)
    
#     #sai da agenda
#     elif instrucao == 4:
#         print(f'\n<< Saiu da agenda! >>')
#         break
#     elif instrucao not in (1,2,3,4): 
#         print("Opção errada ou inexistente!") 

#Solução alternativa

lista_agenda = [] #dicionário inicial que receberá valores
instrucao = "seguir"  #Define a continuação do código

#executa as instruções da agenda
while instrucao != 4:
    instrucao = int(input("Digite o número da opção: 1 - adicionar, 2 - excluir, 3 - imprimir ou 4 - sair: \n"))
    
    #adiciona contatos sem espaços desnecessários
    if instrucao == 1: 
        nome = input("Nome: \n").strip()
        telefone = input("Telefone: \n").strip()
        endereco = input("Endereço: \n").strip()
        agenda = {"nome": nome, "telefone": telefone,"endereco": endereco}  #dicionario da agenda
        lista_agenda.append(agenda) #transforma em lista de dicionários
        print("\nSeu contato foi inserido \n")
    
    #exclui dados da agenda, mas mantém agenda
    elif instrucao == 2:
        while True:
            contador = 0
            for lista in lista_agenda:
                print(f"{contador} - {lista}")
                contador += 1
            print(f"\nSe desistiu, digite {contador} para sair!\n")
            contador_selecionado = input("\n Qual o número da informação deseja excluir?\n")
            if contador_selecionado.isnumeric():
                contador_novo = int(contador_selecionado)
                if contador_novo in range(0, contador):
                    print("\nEstamos excluindo... quase lá...\n")
                    lista_selecionada = lista_agenda.pop(contador_novo) #Apaga o item
                    print(f"\nO dado da agenda {lista_selecionada} foi excluído!\n") #Item foi excluído
                    break #Sai do loop
                elif contador_novo == contador:
                    break   #Sai do loop
                else:
                    print("Informação não existe.")
            else:
                print("Informação incorreta.")
    
    #imprime a agenda
    elif instrucao == 3:
        print(f"\nContatos da agenda: {lista_agenda}\n")
    
    #sai da agenda
    elif instrucao == 4:
        print(f'\n<< Fechamos sua agenda! >>')
        break
    #caso usuário digite opção inexistente
    elif instrucao >=5: 
        print("Essa opção não existe!")