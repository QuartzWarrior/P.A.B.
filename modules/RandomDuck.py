from aiohttp import ClientSession


class RandomDuck:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://random-d.uk/api/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_random_image(self):
        return await self.get("")

    async def get_random_image_by_size(self, width: int, height: int):
        return await self.get(f"{width}/{height}")

    async def get_random_image_by_width(self, width: int):
        return await self.get(f"{width}")

    async def get_random_image_by_height(self, height: int):
        return await self.get(f"0/{height}")

    async def get_random_image_by_grayscale(self):
        return await self.get("g")

    async def get_random_image_by_grayscale_by_size(self, width: int, height: int):
        return await self.get(f"g/{width}/{height}")

    async def get_random_image_by_grayscale_by_width(self, width: int):
        return await self.get(f"g/{width}")

    async def get_random_image_by_grayscale_by_height(self, height: int):
        return await self.get(f"g/0/{height}")

    async def get_random_image_by_color(self, color: str):
        return await self.get(f"{color}")

    async def get_random_image_by_color_by_size(self, color: str, width: int, height: int):
        return await self.get(f"{color}/{width}/{height}")

    async def get_random_image_by_color_by_width(self, color: str, width: int):
        return await self.get(f"{color}/{width}")

    async def get_random_image_by_color_by_height(self, color: str, height: int):
        return await self.get(f"{color}/0/{height}")

    async def get_random_image_by_grayscale_and_color(self, color: str):
        return await self.get(f"g/{color}")

    async def get_random_image_by_grayscale_and_color_by_size(self, color: str, width: int, height: int):
        return await self.get(f"g/{color}/{width}/{height}")

    async def get_random_image_by_grayscale_and_color_by_width(self, color: str, width: int):
        return await self.get(f"g/{color}/{width}")

    async def get_random_image_by_grayscale_and_color_by_height(self, color: str, height: int):
        return await self.get(f"g/{color}/0/{height}")

    async def get_random_image_by_grayscale_and_color_by_size_and_color(self, color: str, width: int, height: int,
                                                                        color2: str):
        return await self.get(f"g/{color}/{width}/{height}/{color2}")
