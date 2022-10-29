from aiohttp import ClientSession


class DogApi:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://dog.ceo/api/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_breeds(self):
        return await self.get("breeds/list/all")

    async def get_random_image(self):
        return await self.get("breeds/image/random")

    async def get_random_image_by_breed(self, breed: str):
        return await self.get(f"breed/{breed}/images/random")

    async def get_random_image_by_sub_breed(self, breed: str, sub_breed: str):
        return await self.get(f"breed/{breed}/{sub_breed}/images/random")
