#this contains all of the voice channel commands

import discord
import asyncio


class voice:
    def init(self, client, message):
        self.client = client
        self.message = message

<<<<<<< HEAD
    def joinchannel(self,client,message):
        self.voice = client.join_voice_channel(message.author.voice_channel)

    def leave( self):
        self.voice.disconnect()

    def playsong(self,url):
        self.player = voice.create_ytdl_player(url)
        self.player.start()
=======
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
>>>>>>> acfd77d169b122452346958ef05fad10890842e3
