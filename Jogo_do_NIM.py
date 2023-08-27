def campeonato():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    op=int(input("2 - para jogar um campeonato "))
    print()

    if(op==2):
        i=1
        
        print("Voce escolheu um campeonato!")

        while(i<=3):
            print()
            print("**** Rodada ", i, "****")
            print()
            partida()
            i=i+1
        print()
        print("**** Final do campeonato! ****")
        print()
        print("Placar: Você 0 X 3 Computador")

    else:
        partida()


def partida():
    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada? "))
    print()

    if(n%(m+1)==0):
        print("Você começa!")
        while(n!=0):
            print()
            n=n-usuario_escolhe_jogada(m, n)
            if(n==1):
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n, "peças no tabuleiro.")
            print()
            n=n-computador_escolhe_jogada(m, n)
            if(n==0):
                break
            if(n==1):
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n, "peças no tabuleiro.")
    else:
        print("Computador começa!")
        while(n!=0):
            print()
            n=n-computador_escolhe_jogada(m, n)
            if(n==0):
                break
            if(n==1):
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n, "peças no tabuleiro.")
            print()
            n=n-usuario_escolhe_jogada(m, n)
            if(n==1):
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam", n, "peças no tabuleiro.")
    print("Fim do jogo! O computador ganhou!")


def computador_escolhe_jogada(n, m):
    i=0
    while((n-(m-i))%(m+1)!=0):
        i=i+1
    if(m-i==0):
        if(m==1):
            print("O computador tirou uma peça.")
        else:
            print("O computador tirou", m, "peças.")
        return m
    if(m-i==1):
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", m-i, "peças.")
    return m-i
    if(n<=m):
        if(n==1):
            print("O computador tirou uma peça.")
        else:
            print("O computador tirou", n, "peças.")
        return n

def usuario_escolhe_jogada(n, m):
    pecas_retiradas=int(input("Quantas peças você vai tirar? "))
    if(pecas_retiradas<1 or pecas_retiradas>m or pecas_retiradas>n):
        while(pecas_retiradas<1 or pecas_retiradas>m or pecas_retiradas>n):
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
            pecas_retiradas=int(input("Quantas peças você vai tirar? "))
    if(pecas_retiradas==1):
        print("Voce tirou uma peça.")
    else:
        print("Voce tirou", pecas_retiradas, "peças.")
    return pecas_retiradas

campeonato()
