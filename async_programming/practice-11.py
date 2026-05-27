import asyncio

async def job(job_id, duration):
    await asyncio.sleep(duration)
    print(f"Tarefa {job_id} finalizada!")

async def exec_jobs():
    tasks = []
    
    tasks.append(asyncio.create_task(job(1, 3)))
    tasks.append(asyncio.create_task(job(2, 5)))
    tasks.append(asyncio.create_task(job(3, 7)))

    while True:
        if all(task.done() for task in tasks):
            break

        status_tarefas = [
            'Finalizado' if task.done() else 'Em andamento'
            for task in tasks
        ]
        print(f"Status das tarefas: {status_tarefas}")
        await asyncio.sleep(1)

asyncio.run(exec_jobs())

