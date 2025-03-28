#Solicite ao usuário três notas e exiba a média aritmética delas.

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

mensagem = f"A sua média aritimetica é: {media}"
print(mensagem)