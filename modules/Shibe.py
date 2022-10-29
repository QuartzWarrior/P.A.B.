from aiohttp import ClientSession


class Shibe:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"http://shibe.online/api/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_random_image(self):
        return await self.get("shibes")

    async def get_random_image_by_count(self, count: int):
        return await self.get("shibes", params={"count": count})

    async def get_random_image_by_count_and_urls(self, count: int, urls: bool):
        return await self.get("shibes", params={"count": count, "urls": urls})

    async def get_random_image_by_urls(self, urls: bool):
        return await self.get("shibes", params={"urls": urls})

    async def get_random_cat(self):
        return await self.get("cats")

    async def get_random_cat_by_count(self, count: int):
        return await self.get("cats", params={"count": count})

    async def get_random_cat_by_count_and_urls(self, count: int, urls: bool):
        return await self.get("cats", params={"count": count, "urls": urls})

    async def get_random_cat_by_urls(self, urls: bool):
        return await self.get("cats", params={"urls": urls})

    async def get_random_bird(self):
        return await self.get("birds")

    async def get_random_bird_by_count(self, count: int):
        return await self.get("birds", params={"count": count})

    async def get_random_bird_by_count_and_urls(self, count: int, urls: bool):
        return await self.get("birds", params={"count": count, "urls": urls})

    async def get_random_bird_by_urls(self, urls: bool):
        return await self.get("birds", params={"urls": urls})

    async def get_random_image_by_type(self, type: str):
        return await self.get(type)

    async def get_random_image_by_type_and_count(self, type: str, count: int):
        return await self.get(type, params={"count": count})

    async def get_random_image_by_type_and_count_and_urls(self, type: str, count: int, urls: bool):
        return await self.get(type, params={"count": count, "urls": urls})

    async def get_random_image_by_type_and_urls(self, type: str, urls: bool):
        return await self.get(type, params={"urls": urls})
