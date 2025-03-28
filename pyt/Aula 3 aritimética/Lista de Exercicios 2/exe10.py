#Peça dois números e exiba o quociente e o resto da divisão inteira entre eles.

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

quociente = num1 // num2
restodiv= num1 % num2

mensagem = f"O quociente da divisão é {quociente}, e o resto da divisão é {restodiv}"
print(mensagem)