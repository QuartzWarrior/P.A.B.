from aiohttp import ClientSession


# live_oQxlCVcGsl3KBfVTLdTrj5WT9Jtv0nf8aEbOjwxGK0l4tJwzqZMxLaWc779aexvX
# 538e943b-b25a-4e8c-8cdf-55e360c630c5
# a56959a4-3749-4be6-8f5e-c53202a436b4
# 2101677a-a5a1-4a78-a4b4-303aab1aa075
# live_37fHdgA0fShUu6KOYXr2SYAt38uuBEMuVlEHJk7H8m1HwfGlDbKQzmFHt1oYngqU
# live_7cy9oXwBEJPzB3t6OPqNcCFX16rvO3f8PvbMo5kxBGkqqmuOhkGaywhFbpF2JCMK
# 6a109865-cc33-4e06-882a-d3cced0b56f5
# 7afdb08a-1a4c-4f5a-b4dd-aa4f8a134896
# b84255e5-0788-4258-aa10-f659ceb6b3c5
# 294cc84a-c8ed-435e-b124-6a0a415f043c
# efaf6552-f07a-4e9d-b1e8-9c615dfa9a4f
# e111a8ad-e09e-4917-899a-2035d2653e51
# cb90513c-1d7b-420d-b14d-df1d7a6cfeca
# 3f41d873-8446-47b3-80c0-45c2f98ff2ff
# a7ed07bb-660b-4184-8084-4163dfd5bc14
# 5fc49858-b719-4ebc-a8e2-9e741777b95e
# 2aeb2c44-30b8-46bd-9ac0-e2a8028aa921
# 6dea088e-c561-4050-aa4d-09be4c639bf0

class TheCatApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = ClientSession()

    async def get_random_cat(self):
        url = f"https://api.thecatapi.com/v1/images/search?api_key={self.api_key}"
        async with self.session.get(url) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

# Path: main.py
# Compare this snippet from TheCatApi.py:
# from aiohttp import ClientSession
#
# class TheCatApi:
#     def __init__(self, api_key):
#         self.api_key = api_key
#         self.session = ClientSession()
#
#     async def get_random_cat(self):
#         url = f"https://api.thecatapi.com/v1/images/search?api_key={self.api_key}"
#         async with self.session.get(url) as response:
#             return await response.json()
#
#     async def close(self):
#         await self.session.close()
