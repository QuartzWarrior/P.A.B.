from aiohttp import ClientSession


class RandomFox:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://randomfox.ca/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_random_image(self):
        return await self.get("floof")

    async def get_random_image_by_id(self, id: int):
        return await self.get(f"images/{id}.jpg")
