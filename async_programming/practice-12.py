import asyncio
from random import randint, choice


class ShowNameInReprMixin:
    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()


class Sensor(ShowNameInReprMixin):
    def __init__(
        self, name: str,
        measure_interval: int = randint(1, 5)
    ):
        self.name = name
        self.measure: int | str = None #actual measure, string or integer
        self.measure_interval = measure_interval

    def __post_init__(self):
        self.measure = randint(0, 100)

    async def collect_measurement(self):
        "takes a measurement in the set sensor's interval rate and stores it in the measure attribute"
        while True:
            await asyncio.sleep(self.measure_interval)

            if self.name == "Umidade":
                self.measure = choice(["Boa", "Regular", "Ruim"])
            else:
                self.measure = randint(0, 100)

            print(f"Sensor {self.name} coletou a medida: {self.measure}", flush=True)


sensor1 = Sensor("Temperatura", measure_interval=2)
sensor2 = Sensor("Umidade", measure_interval=3)
sensor3 = Sensor("Qualidade do ar", measure_interval=5)


async def main():
    tasks = [
        asyncio.create_task(sensor1.collect_measurement()),
        asyncio.create_task(sensor2.collect_measurement()),
        asyncio.create_task(sensor3.collect_measurement())
    ]
    
    await asyncio.gather(*tasks)


asyncio.run(main())
