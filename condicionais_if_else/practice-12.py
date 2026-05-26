
try:
    input_number = int(input("Digite um número inteiro\t->"))
except ValueError:
    print("Por favor, digite um número ao inserir as quantidades.")

remain = input_number % 2

result = ''
if remain == 0:
    result = "O número é par."
else:
    result = "O número é ímpar."

if result:
    print(f"\n{result}")
else: raise Exception("Ocorreu um erro inesperado ao verificar a paridade do número.")