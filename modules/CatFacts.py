from aiohttp import ClientSession


class CatFacts:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://catfact.ninja/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_cat_fact(self):
        return await self.get("fact")

    async def get_cat_facts(self, amount: int = 1):
        return await self.get("facts", params={"limit": amount})

    async def get_cat_fact_by_id(self, id: str):
        return await self.get(f"fact/{id}")

    async def get_cat_facts_by_ids(self, ids: list):
        return await self.get("facts", params={"ids": ids})

    async def get_cat_fact_by_user(self, user: str):
        return await self.get("fact/user", params={"user": user})

    async def get_cat_facts_by_user(self, user: str, amount: int = 1):
        return await self.get("facts/user", params={"user": user, "limit": amount})

    async def get_cat_fact_by_user_id(self, user_id: str):
        return await self.get("fact/user", params={"user_id": user_id})

    async def get_cat_facts_by_user_id(self, user_id: str, amount: int = 1):
        return await self.get("facts/user", params={"user_id": user_id, "limit": amount})

    async def get_cat_fact_by_length(self, length: int):
        return await self.get("fact/length", params={"length": length})

    async def get_cat_facts_by_length(self, length: int, amount: int = 1):
        return await self.get("facts/length", params={"length": length, "limit": amount})

    async def get_cat_fact_by_length_range(self, min_length: int, max_length: int):
        return await self.get("fact/length", params={"min_length": min_length, "max_length": max_length})

    async def get_cat_facts_by_length_range(self, min_length: int, max_length: int, amount: int = 1):
        return await self.get("facts/length",
                              params={"min_length": min_length, "max_length": max_length, "limit": amount})

    async def get_cat_fact_by_search(self, search: str):
        return await self.get("fact/search", params={"search": search})

    async def get_cat_facts_by_search(self, search: str, amount: int = 1):
        return await self.get("facts/search", params={"search": search, "limit": amount})

    async def get_cat_fact_by_search_regex(self, search: str):
        return await self.get("fact/search", params={"search_regex": search})

    async def get_cat_facts_by_search_regex(self, search: str, amount: int = 1):
        return await self.get("facts/search", params={"search_regex": search, "limit": amount})

    async def get_cat_fact_by_search_length(self, search: str, length: int):
        return await self.get("fact/search", params={"search": search, "length": length})

    async def get_cat_facts_by_search_length(self, search: str, length: int, amount: int = 1):
        return await self.get("facts/search", params={"search": search, "length": length, "limit": amount})

    async def get_cat_fact_by_search_length_range(self, search: str, min_length: int, max_length: int):
        return await self.get("fact/search",
                              params={"search": search, "min_length": min_length, "max_length": max_length})

    async def get_cat_facts_by_search_length_range(self, search: str, min_length: int, max_length: int,
                                                   amount: int = 1):
        return await self.get("facts/search",
                              params={"search": search, "min_length": min_length, "max_length": max_length,
                                      "limit": amount})

    async def get_cat_fact_by_search_regex_length(self, search: str, length: int):
        return await self.get("fact/search", params={"search_regex": search, "length": length})

    async def get_cat_facts_by_search_regex_length(self, search: str, length: int, amount: int = 1):
        return await self.get("facts/search", params={"search_regex": search, "length": length, "limit": amount})

    async def get_cat_fact_by_search_regex_length_range(self, search: str, min_length: int, max_length: int):
        return await self.get("fact/search",
                              params={"search_regex": search, "min_length": min_length, "max_length": max_length})

    async def get_cat_facts_by_search_regex_length_range(self, search: str, min_length: int, max_length: int,
                                                         amount: int = 1):
        return await self.get("facts/search",
                              params={"search_regex": search, "min_length": min_length, "max_length": max_length,
                                      "limit": amount})

    async def get_cat_fact_by_random(self):
        return await self.get("fact/random")

    async def get_cat_facts_by_random(self, amount: int = 1):
        return await self.get("facts/random", params={"limit": amount})

    async def get_cat_fact_by_random_length(self, length: int):
        return await self.get("fact/random", params={"length": length})

    async def get_cat_facts_by_random_length(self, length: int, amount: int = 1):
        return await self.get("facts/random", params={"length": length, "limit": amount})

    async def get_cat_fact_by_random_length_range(self, min_length: int, max_length: int):
        return await self.get("fact/random", params={"min_length": min_length, "max_length": max_length})

    async def get_cat_facts_by_random_length_range(self, min_length: int, max_length: int, amount: int = 1):
        return await self.get("facts/random",
                              params={"min_length": min_length, "max_length": max_length, "limit": amount})

    async def get_cat_fact_by_random_search(self, search: str):
        return await self.get("fact/random", params={"search": search})

    async def get_cat_facts_by_random_search(self, search: str, amount: int = 1):
        return await self.get("facts/random", params={"search": search, "limit": amount})

    async def get_cat_fact_by_random_search_regex(self, search: str):
        return await self.get("fact/random", params={"search_regex": search})

    async def get_cat_facts_by_random_search_regex(self, search: str, amount: int = 1):
        return await self.get("facts/random", params={"search_regex": search, "limit": amount})

    async def get_cat_fact_by_random_search_length(self, search: str, length: int):
        return await self.get("fact/random", params={"search": search, "length": length})

    async def get_cat_facts_by_random_search_length(self, search: str, length: int, amount: int = 1):
        return await self.get("facts/random", params={"search": search, "length": length, "limit": amount})

    async def get_cat_fact_by_random_search_length_range(self, search: str, min_length: int, max_length: int):
        return await self.get("fact/random",
                              params={"search": search, "min_length": min_length, "max_length": max_length})

    async def get_cat_facts_by_random_search_length_range(self, search: str, min_length: int, max_length: int,
                                                          amount: int = 1):
        return await self.get("facts/random",
                              params={"search": search, "min_length": min_length, "max_length": max_length,
                                      "limit": amount})

    async def get_cat_fact_by_random_search_regex_length(self, search: str, length: int):
        return await self.get("fact/random", params={"search_regex": search, "length": length})

    async def get_cat_facts_by_random_search_regex_length(self, search: str, length: int, amount: int = 1):
        return await self.get("facts/random", params={"search_regex": search, "length": length, "limit": amount})

    async def get_cat_fact_by_random_search_regex_length_range(self, search: str, min_length: int, max_length: int):
        return await self.get("fact/random",
                              params={"search_regex": search, "min_length": min_length, "max_length": max_length})

    async def get_cat_facts_by_random_search_regex_length_range(self, search: str, min_length: int, max_length: int,
                                                                amount: int = 1):
        return await self.get("facts/random",
                              params={"search_regex": search, "min_length": min_length, "max_length": max_length,
                                      "limit": amount})
