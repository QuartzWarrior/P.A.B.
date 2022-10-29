from aiohttp import ClientSession


class XenoCanto:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://www.xeno-canto.org/api/2/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_recordings(self, query: str):
        return await self.get("recordings", params={"query": query})

    async def get_recordings_by_id(self, id: int):
        return await self.get(f"recordings/{id}")

    async def get_recordings_by_species(self, species: str):
        return await self.get("recordings", params={"query": f"sp:{species}"})

    async def get_recordings_by_location(self, location: str):
        return await self.get("recordings", params={"query": f"loc:{location}"})

    async def get_recordings_by_country(self, country: str):
        return await self.get("recordings", params={"query": f"cnt:{country}"})

    async def get_recordings_by_region(self, region: str):
        return await self.get("recordings", params={"query": f"rgn:{region}"})

    async def get_recordings_by_area(self, area: str):
        return await self.get("recordings", params={"query": f"area:{area}"})

    async def get_recordings_by_type(self, type: str):
        return await self.get("recordings", params={"query": f"type:{type}"})

    async def get_recordings_by_quality(self, quality: str):
        return await self.get("recordings", params={"query": f"q:{quality}"})

    async def get_recordings_by_length(self, length: str):
        return await self.get("recordings", params={"query": f"len:{length}"})

    async def get_recordings_by_date(self, date: str):
        return await self.get("recordings", params={"query": f"date:{date}"})

    async def get_recordings_by_elevation(self, elevation: str):
        return await self.get("recordings", params={"query": f"elev:{elevation}"})

    async def get_recordings_by_number(self, number: str):
        return await self.get("recordings", params={"query": f"nr:{number}"})

    async def get_recordings_by_license(self, license: str):
        return await self.get("recordings", params={"query": f"lic:{license}"})

    async def get_recordings_by_has(self, has: str):
        return await self.get("recordings", params={"query": f"has:{has}"})

    async def get_recordings_by_has_not(self, has_not: str):
        return await self.get("recordings", params={"query": f"has_not:{has_not}"})

    async def get_recordings_by_has_type(self, has_type: str):
        return await self.get("recordings", params={"query": f"has_type:{has_type}"})

    async def get_recordings_by_has_not_type(self, has_not_type: str):
        return await self.get("recordings", params={"query": f"has_not_type:{has_not_type}"})

    async def get_recordings_by_has_tag(self, has_tag: str):
        return await self.get("recordings", params={"query": f"has_tag:{has_tag}"})

    async def get_recordings_by_has_not_tag(self, has_not_tag: str):
        return await self.get("recordings", params={"query": f"has_not_tag:{has_not_tag}"})

    async def get_recordings_by_has_geoloc(self, has_geoloc: str):
        return await self.get("recordings", params={"query": f"has_geoloc:{has_geoloc}"})

    async def get_recordings_by_has_not_geoloc(self, has_not_geoloc: str):
        return await self.get("recordings", params={"query": f"has_not_geoloc:{has_not_geoloc}"})

    async def get_recordings_by_has_comments(self, has_comments: str):
        return await self.get("recordings", params={"query": f"has_comments:{has_comments}"})

    async def get_recordings_by_has_not_comments(self, has_not_comments: str):
        return await self.get("recordings", params={"query": f"has_not_comments:{has_not_comments}"})

    async def get_recordings_by_has_rating(self, has_rating: str):
        return await self.get("recordings", params={"query": f"has_rating:{has_rating}"})

    async def get_recordings_by_has_not_rating(self, has_not_rating: str):
        return await self.get("recordings", params={"query": f"has_not_rating:{has_not_rating}"})

    async def get_recordings_by_has_quality(self, has_quality: str):
        return await self.get("recordings", params={"query": f"has_quality:{has_quality}"})

    async def get_recordings_by_has_not_quality(self, has_not_quality: str):
        return await self.get("recordings", params={"query": f"has_not_quality:{has_not_quality}"})

    async def get_recordings_by_has_length(self, has_length: str):
        return await self.get("recordings", params={"query": f"has_length:{has_length}"})

    async def get_recordings_by_has_not_length(self, has_not_length: str):
        return await self.get("recordings", params={"query": f"has_not_length:{has_not_length}"})
    #
