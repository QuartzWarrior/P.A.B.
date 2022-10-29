from aiohttp import ClientSession


class DogFacts:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://dog-api.kinduff.com/api/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_dog_fact(self):
        return await self.get("facts")

    async def get_dog_facts(self, amount: int = 1):
        return await self.get("facts", params={"number": amount})
