from aiohttp import ClientSession


class ZooAnimals:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://zoo-animal-api.herokuapp.com/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_animal(self):
        return await self.get(f"animals/rand")

    async def get_animals(self, amount: int = 1):
        return await self.get(f"animals/rand/{amount}")
