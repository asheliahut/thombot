#this contains all of the voice channel commands

import discord
import asyncio


class voice:
    def __init__(self, client):
        self.client = client
        self.channel = ""
        self.v_level = 0.2
        self.playlist = []
        music_channel = "" #set as bot music channel

    async def joinchannel(self, message):
        if hasattr(self, 'voice'):
            if self.voice.is_connected():
                self.channel = message.author.voice_channel
                await self.voice.move_to(self.channel)
            else:
                self.channel = message.author.voice_channel
                self.voice = await self.client.join_voice_channel(self.channel)
        else:
            self.channel = message.author.voice_channel
            self.voice = await self.client.join_voice_channel(self.channel)

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
                self.player = await self.voice.create_ytdl_player(url after=self.aftersong())
                self.player.start()
                self.player.volume = self.v_level
        else:
            try:
                self.player = await self.voice.create_ytdl_player(url, after=self.aftersong())
                self.player.start()
                self.player.volume = self.v_level
            except:
                pass

    async def skip(self):
        if self.player.is_playing():
            if self.playlist == []:
                await self.client.send_message(message.channel, 'the queue is empty!')
            else:
                self.player.stop()
                self.player = await self.voice.create_ytdl_player(self.playlist.pop(), after=self.aftersong())
        else:
            await self.client.send_message(message.channel, 'not playing anything!')

    async def aftersong(self):
        if self.playlist == []:
            await client.send_message(music_channel, "the playlist is empty!")
        else:
            self.player.stop()
            self.player = await self.voice.create_ytdl_player(self.playlist.pop(), after=self.aftersong())
            self.player.start()

    def pause(self):
        self.player.pause()

    def resume(self):
        self.player.resume()

    def volume(self, v_input):
        self.v_level = v_input / 100
        self.player.volume = self.v_level
