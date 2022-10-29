from aiohttp import ClientSession


class PlaceBear:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://placebear.com/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_image(self, width: int = 200, height: int = 200):
        return await self.get(f"{width}/{height}")

    async def get_gray_image(self, width: int = 200, height: int = 200):
        return await self.get(f"g/{width}/{height}")

    async def get_random_image(self):
        return await self.get("")

    async def get_random_gray_image(self):
        return await self.get("g")

    async def get_random_image_by_id(self, id: int):
        return await self.get(f"{id}")

    async def get_random_gray_image_by_id(self, id: int):
        return await self.get(f"g/{id}")

    async def get_random_image_by_id_and_text(self, id: int, text: str):
        return await self.get(f"{id}/{text}")

    async def get_random_gray_image_by_id_and_text(self, id: int, text: str):
        return await self.get(f"g/{id}/{text}")

    async def get_random_image_by_text(self, text: str):
        return await self.get(f"{text}")

    async def get_random_gray_image_by_text(self, text: str):
        return await self.get(f"g/{text}")

    async def get_random_image_by_id_and_text_and_color(self, id: int, text: str, color: str):
        return await self.get(f"{id}/{text}/{color}")

    async def get_random_gray_image_by_id_and_text_and_color(self, id: int, text: str, color: str):
        return await self.get(f"g/{id}/{text}/{color}")

    async def get_random_image_by_text_and_color(self, text: str, color: str):
        return await self.get(f"{text}/{color}")

    async def get_random_gray_image_by_text_and_color(self, text: str, color: str):
        return await self.get(f"g/{text}/{color}")

    async def get_random_image_by_color(self, color: str):
        return await self.get(f"{color}")

    async def get_random_gray_image_by_color(self, color: str):
        return await self.get(f"g/{color}")

    async def get_random_image_by_id_and_color(self, id: int, color: str):
        return await self.get(f"{id}/{color}")

    async def get_random_gray_image_by_id_and_color(self, id: int, color: str):
        return await self.get(f"g/{id}/{color}")

    async def get_random_image_by_id_and_text_and_color_and_size(self, id: int, text: str, color: str, width: int = 200,
                                                                 height: int = 200):
        return await self.get(f"{id}/{text}/{color}/{width}/{height}")

    async def get_random_gray_image_by_id_and_text_and_color_and_size(self, id: int, text: str, color: str,
                                                                      width: int = 200, height: int = 200):
        return await self.get(f"g/{id}/{text}/{color}/{width}/{height}")

    async def get_random_image_by_text_and_color_and_size(self, text: str, color: str, width: int = 200,
                                                          height: int = 200):
        return await self.get(f"{text}/{color}/{width}/{height}")

    async def get_random_gray_image_by_text_and_color_and_size(self, text: str, color: str, width: int = 200,
                                                               height: int = 200):
        return await self.get(f"g/{text}/{color}/{width}/{height}")

    async def get_random_image_by_color_and_size(self, color: str, width: int = 200, height: int = 200):
        return await self.get(f"{color}/{width}/{height}")

    async def get_random_gray_image_by_color_and_size(self, color: str, width: int = 200, height: int = 200):
        return await self.get(f"g/{color}/{width}/{height}")

    async def get_random_image_by_id_and_color_and_size(self, id: int, color: str, width: int = 200, height: int = 200):
        return await self.get(f"{id}/{color}/{width}/{height}")

    async def get_random_gray_image_by_id_and_color_and_size(self, id: int, color: str, width: int = 200,
                                                             height: int = 200):
        return await self.get(f"g/{id}/{color}/{width}/{height}")

    async def get_random_image_by_id_and_text_and_size(self, id: int, text: str, width: int = 200, height: int = 200):
        return await self.get(f"{id}/{text}/{width}/{height}")

    async def get_random_gray_image_by_id_and_text_and_size(self, id: int, text: str, width: int = 200,
                                                            height: int = 200):
        return await self.get(f"g/{id}/{text}/{width}/{height}")

    async def get_random_image_by_text_and_size(self, text: str, width: int = 200, height: int = 200):
        return await self.get(f"{text}/{width}/{height}")

    async def get_random_gray_image_by_text_and_size(self, text: str, width: int = 200, height: int = 200):
        return await self.get(f"g/{text}/{width}/{height}")

    async def get_random_image_by_id_and_size(self, id: int, width: int = 200, height: int = 200):
        return await self.get(f"{id}/{width}/{height}")

    async def get_random_gray_image_by_id_and_size(self, id: int, width: int = 200, height: int = 200):
        return await self.get(f"g/{id}/{width}/{height}")

    async def get_random_image_by_size(self, width: int = 200, height: int = 200):
        return await self.get(f"{width}/{height}")

    async def get_random_gray_image_by_size(self, width: int = 200, height: int = 200):
        return await self.get(f"g/{width}/{height}")

    async def get_random_image_by_id_and_text_and_color_and_size_and_background(self, id: int, text: str, color: str,
                                                                                width: int = 200, height: int = 200,
                                                                                background: str = "000000"):
        return await self.get(f"{id}/{text}/{color}/{width}/{height}/{background}")

    async def get_random_gray_image_by_id_and_text_and_color_and_size_and_background(self, id: int, text: str,
                                                                                     color: str, width: int = 200,
                                                                                     height: int = 200,
                                                                                     background: str = "000000"):
        return await self.get(f"g/{id}/{text}/{color}/{width}/{height}/{background}")

    async def get_random_image_by_text_and_color_and_size_and_background(self, text: str, color: str, width: int = 200,
                                                                         height: int = 200, background: str = "000000"):
        return await self.get(f"{text}/{color}/{width}/{height}/{background}")

    async def get_random_gray_image_by_text_and_color_and_size_and_background(self, text: str, color: str,
                                                                              width: int = 200, height: int = 200,
                                                                              background: str = "000000"):
        return await self.get(f"g/{text}/{color}/{width}/{height}/{background}")

    async def get_random_image_by_color_and_size_and_background(self, color: str, width: int = 200, height: int = 200,
                                                                background: str = "000000"):
        return await self.get(f"{color}/{width}/{height}/{background}")

    async def get_random_gray_image_by_color_and_size_and_background(self, color: str, width: int = 200,
                                                                     height: int = 200, background: str = "000000"):
        return await self.get(f"g/{color}/{width}/{height}/{background}")
