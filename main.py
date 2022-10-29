async def main():
    # dog_api = DogApi()
    # cataas = Cataas()
    # print(await cataas.get_cat_by_text_and_type("gif", "Hello World!"))
    # thecatapi = TheCatApi()
    # print(await thecatapi.get_random_cat())
    # await thecatapi.close()
    # df = DogFacts()
    # print(await df.get_dog_fact())
    # print(await dog_api.get_random_image())
    pass


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
