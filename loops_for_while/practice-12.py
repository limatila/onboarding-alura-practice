livros = [
    {
        "nome": "1984",
        "estoque": 5
    },
    {
        "nome": "Dom Casmurro",
        "estoque": 0
    },
    {
        "nome": "O Pequeno Príncipe",
        "estoque": 3
    },
    {
        "nome": "O Hobbit",
        "estoque": 0
    },
    {
        "nome": "Orgulho e Preconceito",
        "estoque": 
    2}
]

for titulo in livros:
    if titulo["estoque"] > 0:
        print(f"Livro disponível: {titulo['nome']}")
    