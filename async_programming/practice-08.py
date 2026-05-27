import asyncio

usuarios = [
    {"nome": "Ana", "vip": True, "notificacoes_ativadas": True},
    {"nome": "João", "vip": False, "notificacoes_ativadas": True},
    {"nome": "Carla", "vip": False, "notificacoes_ativadas": False},
]

async def send_notification(usuario):    
    if not usuario["notificacoes_ativadas"]:
        print(f"{usuario['nome']} desativou as notificações. Nada foi enviado.")
        return
    
    if usuario["vip"]:
        print(f"Notificação VIP enviada para {usuario['nome']}!")
    else:
        print(f"Notificação padrão enviada para {usuario['nome']}.")

async def main():
    print("* Enviando notificações...\n")
    
    tarefas = [send_notification(usuario) for usuario in usuarios]
    await asyncio.gather(*tarefas)
    
    print("\n* Todas as notificações foram processadas.")


asyncio.run(main())
