import asyncio

import aiohttp
from temporalio.client import Client
from temporalio.worker import Worker

from activities import WhereAmIActivities
from workflow import GetAddressFromIP


async def main():
    client = await Client.connect("localhost:7233", namespace="default")

    # Run the worker
    async with aiohttp.ClientSession() as session:
        activities = WhereAmIActivities(session)

        worker = Worker(
            client,
            task_queue="greeting-tasks",
            workflows=[GetAddressFromIP],
            activities=[activities.get_ip, activities.get_location_info],
        )
        print("Starting the worker....")
        await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
