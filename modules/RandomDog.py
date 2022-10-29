from aiohttp import ClientSession


class RandomDog:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://random.dog/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_random_image(self):
        return await self.get("woof.json")

    async def get_random_image_by_type(self, type: str):
        return await self.get(f"{type}.json")

    async def get_random_image_by_breed(self, breed: str):
        return await self.get(f"breed/{breed}/images/random")

    async def get_random_image_by_sub_breed(self, breed: str, sub_breed: str):
        return await self.get(f"breed/{breed}/{sub_breed}/images/random")
