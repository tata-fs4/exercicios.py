# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random

def craps():
    qt_jogadas = 1
    dados = random.randint(2,12)
    if dados == 7 or dados == 11:
        print("\nnatural\nVocê Ganhou!")
    elif dados == 2 or dados == 3 or dados == 12:
        print("\ncraps\nVocê Perdeu!")
    else:
        print(f"\nponto\nEsse é o seu numero: {dados}\nOs dados serão jogados novamente!")
        qt_jogadas += 1
        while True:
            dados_repeat = random.randint(2,12)
            if dados_repeat == 7:
                print("\nVocê Perdeu!")
                break
            elif dados_repeat == dados:
                print("\nVocê ganhou!")
                break
            else:
                print(f"\nponto\nO numero tirado foi: {dados_repeat} \nOs dados serão jogados novamente!")
                qt_jogadas += 1
        print(f"\nO numero tirado foi: {dados_repeat} \nforam feita(s) {qt_jogadas} jogada(s)")

print("\nPartida de Craps\n")
craps()