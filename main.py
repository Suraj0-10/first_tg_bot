import asyncio
from pyrogram import Client

api_id = 5168062
api_hash = "04c049aa96d1cc87920b45b7fb43c0d0"


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from Pyrogram!")


asyncio.run(main())
