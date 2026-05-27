import asyncio  

async def job():  
    print("Iniciando temporizador...")  
    await asyncio.sleep(3)  
    print("Tempo finalizado após 3 segundos!")  

asyncio.run(job())