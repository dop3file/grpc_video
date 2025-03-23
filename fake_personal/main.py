import asyncio

from fake_personal.adapters.fake_personal import start_server


async def main() -> None:
    await start_server()


asyncio.run(main())