from aiohttp import ClientSession


class Cataas:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        async with self.session.get(f"https://cataas.com{path}", **kwargs) as resp:
            return await resp.read()

    async def get_cat(self, tag: str = None, type: str = None, width: int = None, height: int = None):
        params = {}
        if tag:
            params["tag"] = tag
        if type:
            params["type"] = type
        if width:
            params["width"] = width
        if height:
            params["height"] = height
        return await self.get("/cat", params=params)

    async def get_tags(self):
        return await self.get("/tags")

    async def get_random_tag(self):
        return await self.get("/tag/random")

    async def get_random_cat(self):
        return await self.get("/cat/random")

    async def get_cat_by_id(self, id: int):
        return await self.get(f"/cat/{id}")

    async def get_cat_by_text(self, text: str, color: str = None, size: int = None):
        params = {}
        if color:
            params["color"] = color
        if size:
            params["size"] = size
        return await self.get(f"/cat/says/{text}", params=params)

    async def get_cat_by_text_and_id(self, id: int, text: str, color: str = None, size: int = None):
        params = {}
        if color:
            params["color"] = color
        if size:
            params["size"] = size
        return await self.get(f"/cat/{id}/says/{text}", params=params)

    async def get_cat_by_text_and_tag(self, tag: str, text: str, color: str = None, size: int = None):
        params = {}
        if color:
            params["color"] = color
        if size:
            params["size"] = size
        return await self.get(f"/cat/{tag}/says/{text}", params=params)

    async def get_cat_by_text_and_type(self, type: str, text: str, color: str = None, size: int = None):
        params = {}
        if color:
            params["color"] = color
        if size:
            params["size"] = size
        return await self.get(f"/cat/{type}/says/{text}", params=params)

    async def get_cat_by_text_and_width(self, width: int, text: str, color: str = None, size: int = None):
        params = {}
        if color:
            params["color"] = color
        if size:
            params["size"] = size
        return await self.get(f"/cat/{width}/says/{text}", params=params)

    async def get_cat_by_text_and_height(self, height: int, text: str, color: str = None, size: int = None):
        params = {}
        if color:
            params["color"] = color
        if size:
            params["size"] = size
        return await self.get(f"/cat/{height}/says/{text}", params=params)

    async def get_cat_by_text_and_width_and_height(self, width: int, height: int, text: str, color: str = None,
                                                   size: int = None):
        params = {}
        if color:
            params["color"] = color
        if size:
            params["size"] = size
        return await self.get(f"/cat/{width}/{height}/says/{text}", params=params)

    async def get_cat_by_text_and_width_and_height_and_type(self, width: int, height: int, type: str, text: str,
                                                            color: str = None, size: int = None):
        params = {}
        if color:
            params["color"] = color
        if size:
            params["size"] = size
        return await self.get(f"/cat/{width}/{height}/{type}/says/{text}", params=params)

    async def get_cat_by_text_and_width_and_height_and_tag(self, width: int, height: int, tag: str, text: str,
                                                           color: str = None, size: int = None):
        params = {}
        if color:
            params["color"] = color
        if size:
            params["size"] = size
        return await self.get(f"/cat/{width}/{height}/{tag}/says/{text}", params=params)

    async def get_cat_by_text_and_width_and_height_and_tag_and_type(self, width: int, height: int, tag: str, type: str,
                                                                    text: str, color: str = None, size: int = None):
        params = {}
        if color:
            params["color"] = color
        if size:
            params["size"] = size
        return await self.get(f"/cat/{width}/{height}/{tag}/{type}/says/{text}", params=params)

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id(self, width: int, height: int, tag: str,
                                                                           type: str, id: int, text: str,
                                                                           color: str = None, size: int = None):
        params = {}
        if color:
            params["color"] = color
        if size:
            params["size"] = size
        return await self.get(f"/cat/{width}/{height}/{tag}/{type}/{id}/says/{text}", params=params)

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color(self, width: int, height: int,
                                                                                     tag: str, type: str, id: int,
                                                                                     text: str, color: str,
                                                                                     size: int = None):
        params = {}
        if size:
            params["size"] = size
        return await self.get(f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/says/{text}", params=params)

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size(self, width: int,
                                                                                              height: int, tag: str,
                                                                                              type: str, id: int,
                                                                                              text: str, color: str,
                                                                                              size: int):
        return await self.get(f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text(self, width: int,
                                                                                                       height: int,
                                                                                                       tag: str,
                                                                                                       type: str,
                                                                                                       id: int,
                                                                                                       text: str,
                                                                                                       color: str,
                                                                                                       size: int,
                                                                                                       text2: str):
        return await self.get(f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2(self,
                                                                                                                 width: int,
                                                                                                                 height: int,
                                                                                                                 tag: str,
                                                                                                                 type: str,
                                                                                                                 id: int,
                                                                                                                 text: str,
                                                                                                                 color: str,
                                                                                                                 size: int,
                                                                                                                 text2: str,
                                                                                                                 text3: str):
        return await self.get(f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5_and_text6(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str, text7: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}/{text7}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5_and_text6_and_text7(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str, text7: str, text8: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}/{text7}/{text8}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5_and_text6_and_text7_and_text8(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str, text7: str, text8: str, text9: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}/{text7}/{text8}/{text9}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5_and_text6_and_text7_and_text8_and_text9(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str, text7: str, text8: str, text9: str, text10: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}/{text7}/{text8}/{text9}/{text10}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5_and_text6_and_text7_and_text8_and_text9_and_text10(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str, text7: str, text8: str, text9: str, text10: str,
            text11: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}/{text7}/{text8}/{text9}/{text10}/{text11}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5_and_text6_and_text7_and_text8_and_text9_and_text10_and_text11(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str, text7: str, text8: str, text9: str, text10: str,
            text11: str, text12: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}/{text7}/{text8}/{text9}/{text10}/{text11}/{text12}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5_and_text6_and_text7_and_text8_and_text9_and_text10_and_text11_and_text12(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str, text7: str, text8: str, text9: str, text10: str,
            text11: str, text12: str, text13: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}/{text7}/{text8}/{text9}/{text10}/{text11}/{text12}/{text13}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5_and_text6_and_text7_and_text8_and_text9_and_text10_and_text11_and_text12_and_text13(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str, text7: str, text8: str, text9: str, text10: str,
            text11: str, text12: str, text13: str, text14: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}/{text7}/{text8}/{text9}/{text10}/{text11}/{text12}/{text13}/{text14}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5_and_text6_and_text7_and_text8_and_text9_and_text10_and_text11_and_text12_and_text13_and_text14(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str, text7: str, text8: str, text9: str, text10: str,
            text11: str, text12: str, text13: str, text14: str, text15: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}/{text7}/{text8}/{text9}/{text10}/{text11}/{text12}/{text13}/{text14}/{text15}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5_and_text6_and_text7_and_text8_and_text9_and_text10_and_text11_and_text12_and_text13_and_text14_and_text15(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str, text7: str, text8: str, text9: str, text10: str,
            text11: str, text12: str, text13: str, text14: str, text15: str, text16: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}/{text7}/{text8}/{text9}/{text10}/{text11}/{text12}/{text13}/{text14}/{text15}/{text16}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5_and_text6_and_text7_and_text8_and_text9_and_text10_and_text11_and_text12_and_text13_and_text14_and_text15_and_text16(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str, text7: str, text8: str, text9: str, text10: str,
            text11: str, text12: str, text13: str, text14: str, text15: str, text16: str, text17: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}/{text7}/{text8}/{text9}/{text10}/{text11}/{text12}/{text13}/{text14}/{text15}/{text16}/{text17}")

    async def get_cat_by_text_and_width_and_height_and_tag_and_type_and_id_and_color_and_size_and_text_and_text2_and_text3_and_text4_and_text5_and_text6_and_text7_and_text8_and_text9_and_text10_and_text11_and_text12_and_text13_and_text14_and_text15_and_text16_and_text17(
            self, width: int, height: int, tag: str, type: str, id: int, text: str, color: str, size: int, text2: str,
            text3: str, text4: str, text5: str, text6: str, text7: str, text8: str, text9: str, text10: str,
            text11: str, text12: str, text13: str, text14: str, text15: str, text16: str, text17: str, text18: str):
        return await self.get(
            f"/cat/{width}/{height}/{tag}/{type}/{id}/{color}/{size}/says/{text}/{text2}/{text3}/{text4}/{text5}/{text6}/{text7}/{text8}/{text9}/{text10}/{text11}/{text12}/{text13}/{text14}/{text15}/{text16}/{text17}/{text18}")
