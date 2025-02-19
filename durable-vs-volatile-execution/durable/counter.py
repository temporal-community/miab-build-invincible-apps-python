import asyncio
from datetime import timedelta

from temporalio import activity, workflow


@activity.defn
async def add_one(num: int) -> int:
    return num + 1


@workflow.defn
class CountingWorkflow:
    # Make the logging output look more like that of print()
    workflow.logger.workflow_info_on_message = False

    @workflow.run
    async def run(self) -> None:
        workflow.logger.info("*** Counting to 10")

        number = 0
        while number < 10:
            number = await workflow.execute_activity(
                add_one,
                number,
                start_to_close_timeout=timedelta(seconds=5),
            )
            workflow.logger.info(number)
            await asyncio.sleep(1)

        workflow.logger.info("*** Counted to 10")
