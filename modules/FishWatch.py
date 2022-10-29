from aiohttp import ClientSession


class FishWatch:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://www.fishwatch.gov/api/species/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_fish(self, fish: str):
        fish = fish.lower().replace(" ", "-")
        return await self.get(fish)

    async def get_fish_list(self):
        return await self.get("")

    async def get_fish_list_by_group(self, group: str):
        return await self.get(f"group/{group}")
