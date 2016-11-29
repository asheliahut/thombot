#this contains all of the voice channel commands

import discord
import asyncio


class voice:
    def init(self, client, message):
        self.client = client
        self.message = message

    async def joinchannel(self):
        try:
            self.voice = await self.client.join_voice_channel(message.author.voice_channel)
        except:
            pass

    async def leave(self):
        try:
            await self.voice.disconnect()
        except:
            pass

    async def playsong(url):
        await self.player = self.voice.create_ytdl_player(url)
        await self.player.start()
