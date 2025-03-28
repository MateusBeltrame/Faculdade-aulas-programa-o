#Pergunte o valor de um produto e a porcentagem de desconto e calcule o novo preço.

valorproduto = float(input("Qual o valor do produto: "))
desconto = int(input("Qual o valor do desconto: "))

calculo = desconto / 100
calculo2 = valorproduto * calculo
calculo3 = valorproduto - calculo2

mensagem = f"O valor do produto com o desconto será de {calculo3}"
print(mensagem)