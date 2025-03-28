#Jogo de Pedra, Papel, Tesoura

mensagementrada = 'Seja bem-vindo ao jogo de pedra, papel tesoura. Boa sorte e divirta-se'
mensagemregras = 'Vamos as regras \n [1] Para pedra \n [2] Para papel \n [3] Para tesoura \n Cada jogador escolhe um dos objetos: pedra, papel ou tesoura. \n Os jogadores mostram os objetos ao mesmo tempo. \n Pedra vence tesoura, papel vence pedra e tesoura vence papel. \n Se os dois jogadores escolherem o mesmo objeto, é empate e nenhum ganha ponto.'

print(mensagementrada)
print(mensagemregras)

jogador1nome= input('Jogador um qual o seu nome: ')
jogador2nome= input('Jogador dois qual o seu nome: ')

jogador1 = int(input(f'{jogador1nome} faça sua jogada: '))
jogador2 = int(input(f'{jogador2nome} faça sua jogada: '))

if jogador1 < 1 or jogador1 > 3 or jogador2 < 1 or jogador2 > 3:
    print("Escolha invalida! Apenas numeros entre 1 e 3 sao permitidos.\n Por favor reinicie o jogo.")

if (jogador1 == 1 and jogador2 == 3 or
    jogador1 == 2 and jogador2 == 1 or
    jogador1 == 3 and jogador2 == 1):
    print(f'O Jogador {jogador1nome} VENCEU!!!!!!!!!')
elif jogador1 == jogador2:
    print('EMPATE!!!!!!!!!')
else:
    print(f'O Jogador {jogador2nome} VENCEU!!!!!!!!!')