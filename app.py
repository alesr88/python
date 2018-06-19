# -*- coding: UTF-8 -*-

def listar(nomes):
    print 'Listando Nomes'
    for nome in nomes:
        print nome

def cadastrar(nomes):
    print 'Digite o nome: '
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
    print 'Qual nome você deseja remover'
    nome = raw_input()
    nomes.remove(nome)

def alterar(nomes):
    print 'Qual nome você deseja alterar'
    nome = raw_input()
    
    if(nome in nomes):
        print 'Digite o novo nome'
        novo_nome = raw_input()
        posicao = nomes.index(nome)
        nomes[posicao] = novo_nome
    else:
        print 'Este nome não está na lista'

def procurar_nome(nomes):
    print 'Qual nome você deseja procurar?'
    nome = raw_input()
    if(nome in nomes):
        print '%s foi encontrado na lista!' %(nome)
    else:
        print '%s Não está na lista!' %(nome)

def procurar_regex(nomes):
    print('Digite a expressão regular')
    regex = raw_input()
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(regex, nomes_concatenados)
    print(resultados)


def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print 'Digite 1 para cadastrar, 2 para listar, 3 para excluir, 4 para alterar, 5 para pesquisar, 6 para busca regex ou 0 para terminar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)
        if(escolha == '2'):
            listar(nomes)
        if(escolha == '3'):
            remover(nomes)
        if(escolha == '4'):
            alterar(nomes)
        if(escolha == '5'):
            procurar_nome(nomes)
        if(escolha == '6')
            procurar_regex(nomes)
menu()