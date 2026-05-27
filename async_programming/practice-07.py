import asyncio

def factorial(n: int) -> int:
    if n == 0: return 1
    else: return n * factorial(n - 1)

async def calculate_factorial(n: int):
    await asyncio.sleep(n)
    print(f"Factorial de {n} é {factorial(n)}")

numeros = [5, 3, 7, 4, 6]

async def main():
    tasks = []
    
    for n in numeros:
        task = asyncio.create_task(calculate_factorial(n))
        tasks.append(task)
    
    await asyncio.gather(*tasks)

asyncio.run(main())