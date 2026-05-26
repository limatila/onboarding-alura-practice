clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print('Cliente: ' + cliente)

#* Porque usar for: lista é imediatamente iterável, mais fácil e previsível de usar, out-of-the-box.
#* Porque não while: não é necessário controle de indíces, nem de condição de parada.
#* Porque não usar list comprehension: não é uma transformação (no momento), e esse caso pode escalar no futuro, por eu já estar usando print.