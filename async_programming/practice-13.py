import asyncio
from random import randint


class FileDownload:
    def __init__(self, id_number: int):
        self.name = f"arquivo_{id_number}.txt"
        
        self.download_size = randint(10, 50) # in MB
        self.total_downloaded_size = 0
        
        self.check_interval = 1 # in seconds
        self.download_time = 0

    async def start_download(self):
        while self.total_downloaded_size < self.download_size:
            await asyncio.sleep(self.check_interval)
            self.download_time += self.check_interval
            
            new_packet_size = randint(1, 10) # in MB
            if new_packet_size + self.total_downloaded_size > self.download_size: #limitador teórico
                new_packet_size = self.download_size - self.total_downloaded_size

            self.total_downloaded_size += new_packet_size

            print(f"[{self.download_time}s] {self.name}: {self.total_downloaded_size}", flush=True)
        
        print(f"* {self.name} concluído!\n", flush=True)


file1 = FileDownload(1)
file2 = FileDownload(2)
file3 = FileDownload(3)


async def main():
    tasks = [
        asyncio.create_task(file1.start_download()),
        asyncio.create_task(file2.start_download()),
        asyncio.create_task(file3.start_download())
    ]

    await asyncio.gather(*tasks)


asyncio.run(main())


#* adicional
for file in [file1, file2, file3]:
    print(f"{file.name} - Tamanho: {file.total_downloaded_size}MB/{file.download_size}MB - Tempo de download: {file.download_time}s")