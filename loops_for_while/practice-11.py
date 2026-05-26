
current_count = 10

while current_count >= 0:
    if current_count == 0:
        print('Aproveite a promoção agora!')
        exit(0)

    if current_count % 2 == 0:
        print(f'Faltam apenas {current_count} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continue: {current_count} segundos restantes.')
    
    current_count -= 1
        