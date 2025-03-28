#Peça um número ao usuário e exiba o dobro, o triplo e a raiz quadrada dele.

num = int(input("Digite um número: "))

dobro = num * 2
triplo = num * 3
raiz = float(num ** 0.5)

mensagem = f"O dobro é {dobro} o triplo é {triplo} e a raiz quadrada é {raiz}"
print(mensagem)