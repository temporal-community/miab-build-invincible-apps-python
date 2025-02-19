import asyncio
import logging
import sys

from counter import CountingWorkflow, add_one
from temporalio.client import Client
from temporalio.worker import Worker


async def main():
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    client = await Client.connect("localhost:7233", namespace="default")

    try:
        worker = Worker(
            client,
            task_queue="durable",
            workflows=[CountingWorkflow],
            activities=[add_one],
        )
        logging.info(f"Starting the worker....{client.identity}")
        await worker.run()
    except asyncio.exceptions.CancelledError:
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
