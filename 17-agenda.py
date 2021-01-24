#17.Fazer um sistema de Agenda de revisão do Carro 
# (Deve pedir o nome do carro, ano e modelo, nome 
# do proprietário, data e hora da revisão. Depois 
# deve guardar os dados em um dicionário e mostrar 
# a lista de dicionários (agendamentos) na tela)

print("Bem-vinde a Agenda de revisão de Carros!")
agenda_carro = []   #lista inicial que receberá valores

#loop infinito
while True:
    lista = int(input("Escolha o número da opção desejada: 1 - Agendar revisão, 2 - Sair \n"))

    
    if lista == 1:

        #valores do carro sem espaços desnecessários
        carro = input("Digite o nome do carro: \n").strip()
        ano = input("Digite o ano do carro: \n").strip()
        modelo = input("Digite o modelo do carro: \n").strip()
        proprietario = input("Digite o proprietário do carro: \n").strip()
        data = input("Digite a data de revisão do carro: \n").strip()
        hora = input("Digite a hora de revisão do carro: \n").strip()

        #dicionário da agenda que será inserido na lista agenda_carro
        agenda = {
            "carro": carro,
            "ano": ano,
            "modelo": modelo,
            "proprietario": proprietario,
            "data": data,
            "hora": hora
        }  
        agenda_carro.append(agenda) #relaciona a lista com o dicionário
        print(f"Agendamento da revisão do carro: {agenda_carro}\n")   #imprime a agenda
    
    #Sai da angenda 
    elif lista == 2:
        print("Volte sempre!\n")
        break   #para o loop
    
    #Caso o usuário digite opção diferente
    elif lista >= 3:
        print("Opção não existe.\n") 