import random

def jogo():
    novamente = 'sim'
    pontuacao = 0
    while novamente in 'sim, Sim, SIM, s, ss':
        nivel = int(input('-------------------------------------------------- \n              Níveis de Dificuldade: \n-------------------------------------------------- \n                  (1) - Fácil \n                  (2) - Médio \n                  (3) - Difícil \n-------------------------------------------------- \n     Digite o Número de acordo com o Nível: '))
        print('--------------------------------------------------')
        while nivel != 1 and nivel != 2 and nivel != 3:
            nivel = int(input('-------------------------------------------------- \n       Valor Inválido. Digite Novamente: '))
        if nivel == 1:
            tentativas = 20
        elif nivel == 2:
            tentativas = 10
        else:
            tentativas = 5
        numero_secreto = int(random.randrange(101))
        chute = 101
        rodada = 0
        tentativa = 1
        while tentativa != 0:
            chute = int(input('     Digite o seu Palpite: '))
            rodada += 1
            tentativa = tentativas - rodada
            if chute == numero_secreto:
                break
            if chute > numero_secreto:
                print(f'-------------------------------------------------- \n Você está na rodada {rodada}. Possui mais {tentativa} tentativas. \n \n          O número deve ser Menor... \n--------------------------------------------------')
            elif chute < numero_secreto:
                print(f'-------------------------------------------------- \n Você está na rodada {rodada}. Possui mais {tentativa} tentativas. \n \n          O número deve ser Maior... \n--------------------------------------------------')
        if chute == numero_secreto:
            pontuacao += 1
            print(f'     Você Ganhou, Parabéns!     Pontuação Atual: {pontuacao} \n--------------------------------------------------')
        if tentativa == 0:
            #pontuacao -= 1
            if pontuacao > 1:
                pontuacao -= 1
            print(f'     Você perdeu :(     Pontuação Atual: {pontuacao} \n--------------------------------------------------')
            print(f'            O número secreto era {numero_secreto}')
        novamente = input('Deseja Jogar Novamente (Sim ou Não)? ')
        while novamente not in 'sim, Sim, SIM, s, ss, Não, não, nao, Nao, n':
            novamente = input('-------------------------------------------------- \n               Resposta Inválida. \nDeseja Jogar Novamente (Sim ou Não)? ')
    print('-------------------------------------------------- \n               Te vejo na Próxima! \n--------------------------------------------------')
jogo()


