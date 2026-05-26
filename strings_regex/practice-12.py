import re


user_CPF = input("Digite o CPF no formato XXX.XXX.XXX-XX\t->")

cpf_pattern = r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$'

if re.match(cpf_pattern, user_CPF):
    print("O CPF está no formato correto.")
else:
    print("CPF inválido.")
