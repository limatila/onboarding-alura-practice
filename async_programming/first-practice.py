# prática própria, testando asyncio e await
import asyncio

async def async_job(job_id: int, duration: int):
    print(f"Job {job_id} started, will take {duration} seconds.")
    
    await asyncio.sleep(duration)
    
    print(f"Job {job_id} completed.")
    return f"Result of job {job_id}"

async def exec_job(job_id: int, duration: int):
    job_task = asyncio.create_task(async_job(job_id, duration))
    job_task_second = asyncio.create_task(async_job(job_id + 1, duration - 1.5))
    
    await job_task
    await job_task_second
    
    print(job_task.result())
    print(job_task_second.result())

print("\n* Hello!")

asyncio.run(exec_job(1, 3))

print("\n* Finished, Bye!")
