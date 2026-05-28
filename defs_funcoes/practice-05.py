
word_to_measure = input("Digite uma palavra\t->")

def measure_word(word: str) -> int:
    return len(word.strip())

print(f"Essa palavra tem {measure_word(word_to_measure)} letras.")
