matriz = [
    ['   ','   ','   '],
    ['   ','   ','   '],
    ['   ','   ','   ']
]

cntrl_nome = True

while cntrl_nome:
    jogador_x = input("Nome do jogador X: ")
    jogador_o = input("Nome do jogador O: ")
    if jogador_x != jogador_o:
        cntrl_nome = False
    else:
        print("Os nomes não podem ser iguais")

def posicoes_ganhar():
    vazio = '   '
    if (matriz[0][0] == matriz[0][1]) and (matriz[0][0] == matriz[0][2]) and (matriz[0][0] != vazio):
        return matriz[0][0]
    elif (matriz[1][0] == matriz[1][1]) and (matriz[1][0] == matriz[1][2]) and (matriz[1][0] != vazio):
        return matriz[1][0]
    elif (matriz[2][0] == matriz[2][1]) and (matriz[2][0] == matriz[2][2]) and (matriz[2][0] != vazio):
        return matriz[2][0]
    elif (matriz[0][0] == matriz[1][0]) and (matriz[0][0] == matriz[2][0]) and (matriz[0][0] != vazio):
        return matriz[0][0]
    elif (matriz[0][1] == matriz[1][1]) and (matriz[0][1] == matriz[2][1]) and (matriz[0][1] != vazio):
        return matriz[0][1]
    elif (matriz[0][2] == matriz[1][2]) and (matriz[0][2] == matriz[2][2]) and (matriz[0][2] != vazio):
       return matriz[0][2]
    elif (matriz[0][0] == matriz[1][1]) and (matriz[0][0] == matriz[2][2]) and (matriz[0][0] != vazio):
        return matriz[0][0]
    elif (matriz[0][2] == matriz[1][1]) and (matriz[0][2] == matriz[2][0]) and (matriz[0][2] != vazio):
        return matriz[0][2]
    else:
        return 1

def mostrar_parcial():
    print(matriz[0][0] + '|' + matriz[0][1] + '|' + matriz[0][2])
    print("-----------")
    print(matriz[1][0] + '|' +  matriz[1][1] + '|' + matriz[1][2])
    print("-----------")
    print(matriz[2][0] + '|' +  matriz[2][1] + '|' + matriz[2][2])

def marcar_posicao(z):
    cntrl = True
    print(z)
    while cntrl:
        i = input("Escolha a posição i na matriz: ")
        j = input("Escolha a posição j na matriz: ")
        if j.isnumeric() and i.isnumeric():
            j = int(j)
            i = int(i)
            if i in [0,1,2] and j in [0,1,2]:
                if matriz[i][j] == '   ':
                    if z == jogador_x:
                        matriz[i][j] = ' X '
                    else:
                        matriz[i][j] = ' O '
                    cntrl = False
                else:
                    print("A posição já foi escolhida")
            else:
                print("Por favor, informe uma posição válida")
        else:
            print("Por favor, informe apenas números")

cntrl = 0

while posicoes_ganhar() == 1:
    print("Vez do jogador X")
    marcar_posicao(jogador_x)
    cntrl = cntrl + 1
    mostrar_parcial()
    if posicoes_ganhar() == 1 and cntrl < 9:
        print("Vez do jogador O")
        marcar_posicao(jogador_o)
        jogando = posicoes_ganhar()
        mostrar_parcial()
        cntrl = cntrl + 1
    else:
        break

if posicoes_ganhar() == ' X ':
    print("O jogador X ganhou! Parabéns:" + jogador_x)
elif posicoes_ganhar() == ' O ':
    print("O jogador O ganhou! Parabéns:" + jogador_o)
else:
    print("Deu velha")