#Caixa Eletronico

nome = input('Digite seu nome: ')
print('Insira seu cartão!!')

operação = int(input('Qual operção gostaria de realizar \n [1] Extrato \n [2] Depósito \n [3] Saque \n'))

saldo = float(87500)

if (operação < 1) or operação > 3:
    print('Operação invalida!!')
elif operação == 1:
    print(f'Aqui esta seu extrato bancário \n Saldo R${saldo}')
elif operação == 2:
    valordeposito = int(input('Qual o valor do seu depósito: '))
    if valordeposito < 1:
        print('Deposito inválido')
    else:
        calculodep = valordeposito + saldo
        print(f'Depósito realizado com sucesso agora seu saldo é de R${calculodep}')
elif operação == 3:
    valorsaque = int(input('Informe o valor que deseja sacar: '))
    if valorsaque > saldo:
        print('Saldo insuficiente')
    else:
        nota200 = valorsaque // 200
        resto200 = valorsaque % 200
        nota100 = resto200 // 100
        resto100 = resto200 % 100
        nota50 = resto100 // 50
        resto50 = resto100 % 50
        nota20 = resto50 // 20
        resto20 = resto50 % 20
        nota10 = resto20 // 10
        resto10 = resto20 % 10
        nota5 = resto10 // 5
        resto5 = resto10 % 5
        nota2 = resto5 // 2

        quantnotas = f'Quantidade minima de notas a sacar \n Nota R$200: {nota200}, Notas R$100: {nota100}, Notas R$50: {nota50},  Notas R$20: {nota20},  Notas R$10: {nota10},  Notas R$5: {nota5},  Notas R$2: {nota2}'

        print(quantnotas)
        