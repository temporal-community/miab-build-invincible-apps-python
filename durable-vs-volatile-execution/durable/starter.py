import asyncio
import logging

from counter import CountingWorkflow
from temporalio.client import Client


async def main():

    # Customize the logger output to match the print statement
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
    )

    client = await Client.connect("localhost:7233")

    await client.start_workflow(
        CountingWorkflow.run,
        id="counting-workflow-id",
        task_queue="durable",
    )


if __name__ == "__main__":
    asyncio.run(main())
