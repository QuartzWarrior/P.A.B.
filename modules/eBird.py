from aiohttp import ClientSession


class eBird:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://api.ebird.org/v2/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_recent_observations(self, region: str, days: int = 7, max_results: int = 100):
        return await self.get(f"product/obs/{region}/recent", params={"back": days, "maxResults": max_results})

    async def get_recent_observations_by_species(self, region: str, species: str, days: int = 7,
                                                 max_results: int = 100):
        return await self.get(f"product/obs/{region}/recent/{species}",
                              params={"back": days, "maxResults": max_results})

    async def get_recent_observations_by_species_and_region(self, region: str, species: str, days: int = 7,
                                                            max_results: int = 100):
        return await self.get(f"product/obs/{region}/recent/{species}",
                              params={"back": days, "maxResults": max_results})

    async def get_recent_observations_by_species_and_subregion(self, region: str, subregion: str, species: str,
                                                               days: int = 7, max_results: int = 100):
        return await self.get(f"product/obs/{region}/{subregion}/recent/{species}",
                              params={"back": days, "maxResults": max_results})

    async def get_recent_observations_by_subregion(self, region: str, subregion: str, days: int = 7,
                                                   max_results: int = 100):
        return await self.get(f"product/obs/{region}/{subregion}/recent",
                              params={"back": days, "maxResults": max_results})
