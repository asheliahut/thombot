#this contains all of the voice channel commands

import discord
import asyncio


class voice:
    def __init__(self, client, message):
        self.client = client
        self.message = message

    async def joinchannel(self):
        try:
            voice = await self.client.join_voice_channel(self.message.author.voice_channel)
        except:
            pass

    async def leave(self):
        try:
            await self.voice.disconnect()
        except:
            pass

    async def playsong(self, url):
        self.player = await self.voice.create_ytdl_player(url)
        await self.player.start()
