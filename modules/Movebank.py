from aiohttp import ClientSession


class Movebank:
    def __init__(self, session: ClientSession = ClientSession()):
        self.session = session

    async def get(self, path: str, **kwargs):
        url = f"https://www.movebank.org/movebank/service/json-auth/{path}"
        async with self.session.get(url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def get_study(self, study_id: int):
        return await self.get(f"study/{study_id}")

    async def get_study_by_tag(self, tag: str):
        return await self.get(f"study/tag/{tag}")

    async def get_study_by_user(self, user_id: int):
        return await self.get(f"study/user/{user_id}")

    async def get_study_by_user_and_tag(self, user_id: int, tag: str):
        return await self.get(f"study/user/{user_id}/tag/{tag}")

    async def get_study_by_user_and_study(self, user_id: int, study_id: int):
        return await self.get(f"study/user/{user_id}/study/{study_id}")

    async def get_study_by_user_and_study_and_tag(self, user_id: int, study_id: int, tag: str):
        return await self.get(f"study/user/{user_id}/study/{study_id}/tag/{tag}")

    async def get_study_by_user_and_study_and_tag_and_species(self, user_id: int, study_id: int, tag: str,
                                                              species: str):
        return await self.get(f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual(self, user_id: int, study_id: int,
                                                                             tag: str, species: str,
                                                                             individual_id: int):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor(self, user_id: int,
                                                                                        study_id: int, tag: str,
                                                                                        species: str,
                                                                                        individual_id: int,
                                                                                        sensor_id: int):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data(self, user_id: int,
                                                                                                 study_id: int,
                                                                                                 tag: str, species: str,
                                                                                                 individual_id: int,
                                                                                                 sensor_id: int):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data_and_start(self,
                                                                                                           user_id: int,
                                                                                                           study_id: int,
                                                                                                           tag: str,
                                                                                                           species: str,
                                                                                                           individual_id: int,
                                                                                                           sensor_id: int,
                                                                                                           start: int):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data/{start}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data_and_start_and_end(self,
                                                                                                                   user_id: int,
                                                                                                                   study_id: int,
                                                                                                                   tag: str,
                                                                                                                   species: str,
                                                                                                                   individual_id: int,
                                                                                                                   sensor_id: int,
                                                                                                                   start: int,
                                                                                                                   end: int):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data/{start}/{end}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data_and_start_and_end_and_limit(
            self, user_id: int, study_id: int, tag: str, species: str, individual_id: int, sensor_id: int, start: int,
            end: int, limit: int):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data/{start}/{end}/{limit}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data_and_start_and_end_and_limit_and_format(
            self, user_id: int, study_id: int, tag: str, species: str, individual_id: int, sensor_id: int, start: int,
            end: int, limit: int, format: str):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data/{start}/{end}/{limit}/{format}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data_and_start_and_end_and_limit_and_format_and_time_zone(
            self, user_id: int, study_id: int, tag: str, species: str, individual_id: int, sensor_id: int, start: int,
            end: int, limit: int, format: str, time_zone: str):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data/{start}/{end}/{limit}/{format}/{time_zone}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data_and_start_and_end_and_limit_and_format_and_time_zone_and_time_format(
            self, user_id: int, study_id: int, tag: str, species: str, individual_id: int, sensor_id: int, start: int,
            end: int, limit: int, format: str, time_zone: str, time_format: str):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data/{start}/{end}/{limit}/{format}/{time_zone}/{time_format}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data_and_start_and_end_and_limit_and_format_and_time_zone_and_time_format_and_time_unit(
            self, user_id: int, study_id: int, tag: str, species: str, individual_id: int, sensor_id: int, start: int,
            end: int, limit: int, format: str, time_zone: str, time_format: str, time_unit: str):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data/{start}/{end}/{limit}/{format}/{time_zone}/{time_format}/{time_unit}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data_and_start_and_end_and_limit_and_format_and_time_zone_and_time_format_and_time_unit_and_time_interval(
            self, user_id: int, study_id: int, tag: str, species: str, individual_id: int, sensor_id: int, start: int,
            end: int, limit: int, format: str, time_zone: str, time_format: str, time_unit: str, time_interval: int):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data/{start}/{end}/{limit}/{format}/{time_zone}/{time_format}/{time_unit}/{time_interval}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data_and_start_and_end_and_limit_and_format_and_time_zone_and_time_format_and_time_unit_and_time_interval_and_time_offset(
            self, user_id: int, study_id: int, tag: str, species: str, individual_id: int, sensor_id: int, start: int,
            end: int, limit: int, format: str, time_zone: str, time_format: str, time_unit: str, time_interval: int,
            time_offset: int):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data/{start}/{end}/{limit}/{format}/{time_zone}/{time_format}/{time_unit}/{time_interval}/{time_offset}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data_and_start_and_end_and_limit_and_format_and_time_zone_and_time_format_and_time_unit_and_time_interval_and_time_offset_and_time_offset_unit(
            self, user_id: int, study_id: int, tag: str, species: str, individual_id: int, sensor_id: int, start: int,
            end: int, limit: int, format: str, time_zone: str, time_format: str, time_unit: str, time_interval: int,
            time_offset: int, time_offset_unit: str):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data/{start}/{end}/{limit}/{format}/{time_zone}/{time_format}/{time_unit}/{time_interval}/{time_offset}/{time_offset_unit}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data_and_start_and_end_and_limit_and_format_and_time_zone_and_time_format_and_time_unit_and_time_interval_and_time_offset_and_time_offset_unit_and_time_offset_interval(
            self, user_id: int, study_id: int, tag: str, species: str, individual_id: int, sensor_id: int, start: int,
            end: int, limit: int, format: str, time_zone: str, time_format: str, time_unit: str, time_interval: int,
            time_offset: int, time_offset_unit: str, time_offset_interval: int):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data/{start}/{end}/{limit}/{format}/{time_zone}/{time_format}/{time_unit}/{time_interval}/{time_offset}/{time_offset_unit}/{time_offset_interval}")

    async def get_study_by_user_and_study_and_tag_and_species_and_individual_and_sensor_and_data_and_start_and_end_and_limit_and_format_and_time_zone_and_time_format_and_time_unit_and_time_interval_and_time_offset_and_time_offset_unit_and_time_offset_interval_and_time_offset_offset(
            self, user_id: int, study_id: int, tag: str, species: str, individual_id: int, sensor_id: int, start: int,
            end: int, limit: int, format: str, time_zone: str, time_format: str, time_unit: str, time_interval: int,
            time_offset: int, time_offset_unit: str, time_offset_interval: int, time_offset_offset: int):
        return await self.get(
            f"study/user/{user_id}/study/{study_id}/tag/{tag}/species/{species}/individual/{individual_id}/sensor/{sensor_id}/data/{start}/{end}/{limit}/{format}/{time_zone}/{time_format}/{time_unit}/{time_interval}/{time_offset}/{time_offset_unit}/{time_offset_interval}/{time_offset_offset}")
