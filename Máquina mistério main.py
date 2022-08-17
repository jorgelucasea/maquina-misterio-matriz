from time import sleep

#Função para o menu
def menu():
    print('=~'*35)
    print('Bem-vindo(a) ao POCCOBUS')
    print('=~'*35)
    print()
    print('[1] COMPRAR ASSENTOS.')
    print('')
    print('[2] RELATÓRIO DE VENDAS.')
    print('')
    print('='*35)

#Definindo a matriz genérica
def criar_matriz(linha,coluna):
    cont = 0
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            cont = cont + 1
            linha.append(cont)
        
        matriz.append(linha)
    
    return matriz

#Criando o ônibus
def van():
    alt = 6
    larg = 4
    return criar_matriz(alt,larg)

#Modo de substituir o número por 'X'
def x_cadeira_reservada(van,cadeiras_r):
    x = 'XX'
    for r in range(len(van)):
        van_n = []
        for c in range(len(van[0])):
            if (van[r][c] in cadeiras_r):
                van_n.append(f'{x:^3}')
            else:
                van_n.append(f'{van[r][c]:^3}')
        print(van_n)
        
v = van()

#Reservar a cadeira
def reservar(cadeira, lista_livre, lista_reservado):
    lista_livre.remove(cadeira)
    lista_reservado.append(cadeira)
    
    return lista_reservado

#Tela para reservar
def tela_para_reservar(cadeiras_r, cadeiras_l):
    
    while True:
        print()
        x_cadeira_reservada(v,cadeiras_r)
        print()   
        print('Para voltar ao menu digite [0]')
        x = int(input('Digite qual cadeira deseja escolher: '))

        if x == 0:
            menu()
            break
        if x in cadeiras_r:
            print('Cadeira já reservada. Por favor escolha outra cadeira.')
            sleep(.75)
        elif x not in cadeiras_l:
            print('Por gentiliza escolha outra cadeira.')
            sleep(.75)
        elif x in cadeiras_l:
            reservar(x,cadeiras_l,cadeiras_r)

#Função para relatório
def relatório():
    exibir = open('relatório.txt', 'a')
    exibir.write(
    f'''Assentos livres: {cadeiras_l} \nAssentos reservados: {cadeiras_r}''')

v = van()
cadeiras_r = []
cadeiras_l = [x for xs in v for x in xs]
        

#PROGRAMA PRINCIPAL
menu()
while True:
    xy = int(input('Digite qual opção você deseja: '))
    if xy == 1:
        tela_para_reservar(cadeiras_r,cadeiras_l)
    elif xy == 2:
        relatório()
    else:
        print('Digite um comando válido.')