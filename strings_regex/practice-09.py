import re


description = input("Digite a descrição da receita\t->")

pattern_digits = r'\d+'

print("O número da receita é:", re.search(pattern_digits, description).group())
