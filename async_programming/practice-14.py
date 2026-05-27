import asyncio
from random import randint, choice


jogos = [
    {"id": 1, "times": ["Flamengo", "Palmeiras"]},
    {"id": 2, "times": ["São Paulo", "Corinthians"]},
    {"id": 3, "times": ["Grêmio", "Internacional"]},
]


class Game:    
    def __init__(self, id_number: int, teams: list[str]):
        self.id = id_number
        self.times = teams
        self.resultado = asyncio.Future() #* Guarda o resultado de forma assíncrona, permitindo que seja definido posteriormente
        self.game_time = randint(2, 8)

    async def start_game(self):
        print(f"Aposta no jogo {self.id} registrada! Aguardando resultado...", flush=True)
        
        await asyncio.sleep(self.game_time) # Simula o tempo do jogo
        resultado = choice([f"Vitória do {self.times[0]}", f"Vitória do {self.times[1]}", "Empate"])
        self.resultado.set_result(resultado)
        
        print(
            f"Aposta no jogo {self.id} definida: {await self.resultado} (após {self.game_time}s)",
            flush=True
        )


games = [Game(jogo["id"], jogo["times"]) for jogo in jogos]


async def main():
    print('')
    tasks = [
        asyncio.create_task(game.start_game()) for game in games
    ]

    await asyncio.gather(*tasks)

    print('\nTodos os resultados foram revelados!')


asyncio.run(main())
