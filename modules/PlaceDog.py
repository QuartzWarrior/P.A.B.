from aiohttp import ClientSession


class PlaceDog:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://placedog.net/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_image(self, width: int = 300, height: int = 300):
        return await self.get("", params={"width": width, "height": height})

    async def get_image_by_id(self, id: int, width: int = 300, height: int = 300):
        return await self.get(f"{id}", params={"width": width, "height": height})

    async def get_image_by_breed(self, breed: str, width: int = 300, height: int = 300):
        return await self.get(f"{breed}", params={"width": width, "height": height})

    async def get_image_by_sub_breed(self, breed: str, sub_breed: str, width: int = 300, height: int = 300):
        return await self.get(f"{breed}/{sub_breed}", params={"width": width, "height": height})

    async def get_image_by_breed_and_id(self, breed: str, id: int, width: int = 300, height: int = 300):
        return await self.get(f"{breed}/{id}", params={"width": width, "height": height})

    async def get_image_by_sub_breed_and_id(self, breed: str, sub_breed: str, id: int, width: int = 300,
                                            height: int = 300):
        return await self.get(f"{breed}/{sub_breed}/{id}", params={"width": width, "height": height})

    async def get_image_by_sub_breed_and_id(self, breed: str, sub_breed: str, id: int, width: int = 300,
                                            height: int = 300):
        return await self.get(f"{breed}/{sub_breed}/{id}", params={"width": width, "height": height})

    async def get_image_by_breed_and_id_and_color(self, breed: str, id: int, color: str, width: int = 300,
                                                  height: int = 300):
        return await self.get(f"{breed}/{id}/{color}", params={"width": width, "height": height})

    async def get_image_by_sub_breed_and_id_and_color(self, breed: str, sub_breed: str, id: int, color: str,
                                                      width: int = 300, height: int = 300):
        return await self.get(f"{breed}/{sub_breed}/{id}/{color}", params={"width": width, "height": height})

    async def get_image_by_breed_and_color(self, breed: str, color: str, width: int = 300, height: int = 300):
        return await self.get(f"{breed}/{color}", params={"width": width, "height": height})

    async def get_image_by_sub_breed_and_color(self, breed: str, sub_breed: str, color: str, width: int = 300,
                                               height: int = 300):
        return await self.get(f"{breed}/{sub_breed}/{color}", params={"width": width, "height": height})

    async def get_image_by_color(self, color: str, width: int = 300, height: int = 300):
        return await self.get(f"{color}", params={"width": width, "height": height})

    async def get_image_by_id_and_color(self, id: int, color: str, width: int = 300, height: int = 300):
        return await self.get(f"{id}/{color}", params={"width": width, "height": height})
