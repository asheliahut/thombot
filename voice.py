#this contains all of the voice channel commands

import discord
import asyncio


class voice:
    def __init__(self, client):
        self.client = client
        self.v_level = 0.2
        self.playlist = []

    async def joinchannel(self, message):
        try:
            self.voice = await self.client.join_voice_channel(message.author.voice_channel)
        except:
            pass

    async def leave(self):
        try:
            await self.voice.disconnect()
        except:
            pass

    async def playsong(self, url, message):
        if hasattr(self, 'player'):
            if self.player.is_playing():
                self.playlist.append(url)
                await self.client.send_message(message.channel, 'Added song to queue!')
            else:
                self.player.stop()
                self.player = await self.voice.create_ytdl_player(url)
                self.player.start()
                self.player.volume = self.v_level
        else:
            try:
                self.player = await self.voice.create_ytdl_player(url)
                self.player.start()
                self.player.volume = self.v_level
            except:
                pass

    async def skip(self):
        if self.player.is_playing():
            if not self.playlist == []:
                await self.client.send_message(message.channel, 'the queue is empty!')
            else:
                self.player.stop()
                self.player = await self.voice.create_ytdl_player(self.playlist.pop())
        else:
            await self.client.send_message(message.channel, 'not playing anything!')

    def pause(self):
        self.player.pause()

    def resume(self):
        self.player.resume()

    def volume(self, v_input):
        self.v_level = v_input / 100
        self.player.volume = self.v_level
