import re


book_title = input("Digite o título do livro\t->")
inicial_letter = input("Digite a letra inicial para pesquisa\t->")

search_pattern = rf'\b{inicial_letter}[a-zà-ÿ\d]*'

matches = re.findall(search_pattern, book_title, re.IGNORECASE)

print("Padrões encontrados:", matches)
