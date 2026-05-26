
try_again = False

while True:
    text_for_revision = input(f"Digite{' novamente' if try_again else ''} o texto a ser revisado\t->")
    word_to_replace = input("Qual palavra deseja substituir\t->")
    replacement_word = input("Qual a nova palavra\t->")
    
    for word in [word_to_replace, replacement_word]:
        if len(word.split()) != 1:
            print("Cada palavra deve ser apenas um termo/palavra, sem espaços.\n")
            try_again = True
            break

    if try_again:
        continue

    revised_text = text_for_revision.replace(word_to_replace, replacement_word)
    print(f"Texto revisado:\t\'{revised_text}\'")
    exit()
