import urllib.parse

from temporalio import activity


class WhereAmIActivities:
    def __init__(self, session):
        self.session = session

    @activity.defn
    async def get_ip(self) -> str:
        async with self.session.get("https://icanhazip.com") as response:
            response.raise_for_status()
            result = await response.text()
            return result.strip()

    @activity.defn
    async def get_location_info(self, ip: str) -> str:
        async with self.session.get(f"http://ip-api.com/json/{ip}") as response:
            response.raise_for_status()
            result = await response.json()
            return f"{result["city"]}, {result["regionName"]}, {result["country"]}"
