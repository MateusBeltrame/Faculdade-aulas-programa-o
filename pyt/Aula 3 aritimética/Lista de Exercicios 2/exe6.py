#Peça ao usuário o valor de uma compra e quanto ele pagou. Calcule o troco.

valorcompra = float(input("Qual foi o valor da compra: "))
valorpago = float(input("Qual o valor pago na compra: "))

calculo = valorpago - valorcompra
mensagem = f"O valor do troco será: {calculo}"
print(mensagem)
