livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

position_hobbit = livros.index("O Hobbit")

if position_hobbit != -1:
    print(f"Livro encontrato: {livros[position_hobbit]}")
else:
    print("Livro não encontrado nos dados do sistema.")