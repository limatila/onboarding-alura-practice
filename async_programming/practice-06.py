import asyncio

async def download_job():
    print("Iniciando download...")
    await asyncio.sleep(1)
    print("Download concluído!")

async def analysis_job():
    print("Iniciando análise de dados...")
    await asyncio.sleep(2)
    print("Análise de dados concluída!")

async def exec_jobs():
    download_task = asyncio.create_task(download_job())
    analysis_task = asyncio.create_task(analysis_job())
    
    await download_task
    await analysis_task

print("* Hello!\n")

asyncio.run(exec_jobs())

print("\n* Finished, Bye!")