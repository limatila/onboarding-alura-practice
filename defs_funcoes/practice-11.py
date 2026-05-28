
class CalculadoraSimples:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.last_result = None

    @property
    def method_dispatcher(self):
        return {
            '+': self.somar,
            '-': self.subtrair,
            '*': self.multiplicar,
            '/': self.dividir
        }

    def calcular(self, operation: str) -> float | str:
        if operation in self.method_dispatcher.keys():
            self.last_result = self.method_dispatcher[operation]()
            return self.last_result
            
        else:
            return "[ERRO] Operação inválida. Por favor, escolha entre +, -, *, /."

    def somar(self):
        return self.num1 + self.num2

    def subtrair(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "[ERRO] Divisão por zero não é permitida."


try:
    first_number = float(input("Digite o primeiro número\t->").strip())
    second_number = float(input("Digite o segundo número\t->").strip())
    calc_operation = input("Escolha a operação matemática (| + | - | * | / |)\t->").strip()

except ValueError:
    print("[ERRO] Por favor, digite um número válido ao inserir os valores.")


calculator = CalculadoraSimples(first_number, second_number)
result = calculator.calcular(calc_operation)

print(f"\nO resultado é {result}")
