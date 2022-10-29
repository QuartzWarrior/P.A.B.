from aiohttp import ClientSession


class MeowFacts:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://meowfacts.herokuapp.com/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_meow_fact(self):
        return await self.get("")

    async def get_meow_facts(self, amount: int = 1):
        return await self.get("", params={"amount": amount})

    async def get_meow_fact_by_id(self, id: int):
        return await self.get("", params={"id": id})
