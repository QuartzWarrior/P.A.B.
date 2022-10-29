from aiohttp import ClientSession


class PlaceKitten:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"http://placekitten.com/{path}"
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

    async def get_random_image_by_grayscale_and_color_by_size_and_text(self, color: str, width: int, height: int,
                                                                       text: str):
        return await self.get(f"g/{color}/{width}/{height}/{text}")

    async def get_random_image_by_grayscale_and_color_by_width_and_text(self, color: str, width: int, text: str):
        return await self.get(f"g/{color}/{width}/{text}")

    async def get_random_image_by_grayscale_and_color_by_height_and_text(self, color: str, height: int, text: str):
        return await self.get(f"g/{color}/0/{height}/{text}")

    async def get_random_image_by_grayscale_and_color_by_size_and_text_and_font(self, color: str, width: int,
                                                                                height: int, text: str, font: str):
        return await self.get(f"g/{color}/{width}/{height}/{text}/{font}")
