#Pergunte ao usuário o preço de um produto e a quantidade que deseja comprar. Calcule e exiba o valor total.

precoproduto = float(input("Qual o preço do produto: "))
quantproduto = int(input("Qual a quantidade de produtos: "))

calculo = precoproduto * quantproduto
mensagem = f"O valor final da compra será: {calculo}"
print(mensagem)