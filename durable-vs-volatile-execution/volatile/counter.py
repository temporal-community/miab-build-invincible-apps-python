import asyncio
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


async def main():
    for i in range(1, 11):
        logging.info(i)
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
