#14.Fazer um sistema de biblioteca (Deve imprimir 
# uma lista com 10 livros, pedir o nome do 
# solicitante do empréstimo, pedir para selecionar 
# um livro e imprimir o livro selecionado)

#Orientação do professor: a lista é de strings, vc vai colocar 
# o nome dos livros, e pedir para o usuário selecionar um e 
# imprimir o livro selecionado (Você vai ter que trabalhar com índices).

#lista de livros, bibliotecas usam número de registro para identificar
#cada publicação
    
print("Bem-vinde a Biblioteca Gama! Os livros para empréstimo são:"
'''
        [0] O universo numa casca de noz',
        [1] Uma breve história do tempo',
        [2] O grande projeto',
        [3] A teoria de tudo',
        [4] Buracos Negros: Palestra da BBC Reith Lectures',
        [5] Uma nova história do tempo',
        [6] Breves respostas para grandes questões',
        [7] Infinito em todas as direções',
        [8] O livro que ninguém leu',
        [9] Mundos em Guerra: a luta de mais 2.500 anos entre o Oriente e o Ocidente.''')

usuario = input("Por favor digite seu nome para realizarmos o empréstimo: ") #nome do usuario
emprestimo = int(input("Digite o número do livro desejado: ")) #solicitações do usuário (seleção)

   #lista para seleção
lista_livros = ["O universo numa casca de noz",
        "Uma breve história do tempo",
        "O grande projeto",
        "A teoria de tudo",
        "Buracos Negros: Palestra da BBC Reith Lectures",
        "Uma nova história do tempo",
        "Breves respostas para grandes questões",
        "Infinito em todas as direções",
        "O livro que ninguém leu",
        "Mundos em Guerra: a luta de mais 2.500 anos entre o Oriente e o Ocidente"]    #lista para escolha
if emprestimo >= 10:    #caso usuário não digite a opção correta
    print("Não temos esta opção em nosso acervo.")
if emprestimo <=9:     #verifica a seleção
     print(f"{usuario} o empréstimo do livro {lista_livros[emprestimo]} foi realizado.") #resultado
     print("Volte sempre!")

#2ª solução - alternativa (uso do if, elif, else)

# print("Os livros disponíveis para empréstimo são:"
# '''
# [1] O universo numa casca de noz
# [2] Uma breve história do tempo
# [3] O grande projeto
# [4] A teoria de tudo
# [5] Buracos Negros: Palestra da BBC Reith Lectures
# [6] Uma nova história do tempo
# [7] Breves respostas para grandes questões
# [8] Infinito em todas as direções
# [9] O livro que ninguém leu
# [10] Mundos em Guerra: a luta de mais 2.500 anos entre o Oriente e o Ocidente
# [11] Se desistiu do empréstimo, selecione esta opção''')

# nome = input("Para realizar um empréstimo por favor digite seu nome: ")
# selecao_livro = int(input("Selecione o número do livro que deseja empréstimo: "))

# if selecao_livro == 1:
#     print("O livro selecionado foi O universo numa casca de noz.")
# elif selecao_livro == 2:
#     print("O livro selecionado foi Uma breve história do tempo.")
# elif selecao_livro == 3:
#     print("O livro selecionado foi O grande projeto.")
# elif selecao_livro == 4:
#     print("O livro selecionado foi A teoria de tudo.")
# elif selecao_livro == 5:
#     print("O livro selecionado foi Buracos Negros: Palestra da BBC Reith Lectures.")
# elif selecao_livro == 6:
#     print("O livro selecionado foi Uma nova história do tempo.")
# elif selecao_livro == 7:
#     print("O livro selecionado foi Breves respostas para grandes questões.")
# elif selecao_livro == 8:
#     print("O livro selecionado foi Infinito em todas as direções.")
# elif selecao_livro == 9:
#     print("O livro selecionado foi O livro que ninguém leu.")
# elif selecao_livro == 10:
#     print("O livro selecionado foi Mundos em Guerra: a luta de mais 2.500 anos entre o Oriente e o Ocidente.")
# else:
#     print("Opção inválida.")
# print("Volte sempre!")