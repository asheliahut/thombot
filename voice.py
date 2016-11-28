#this contains all of the voice channel commands

import discord
import asyncio
import random

#maybe this should be a class? ask ashley for advice on how I should create this thing.

async def joinchannel(client,message):
    try:
        voice = await client.join_voice_channel(message.content[15:])
        return voice
    except:
        if message.author.voice.voice_channel != None:
            voice = await client.join_voice_channel(message.author.voice.voice_channel)
            return voice
        else:
            await client.send_message(message.channel, 'PLease either join a chnanel or specify a channel for me to join!')

async def leavechannel(client,message,voice):
    await voice.disconnect()

async def playsong(client,message,voice,):
    song_to_play = message.content[13:]
    try:
        player = await voice.create_ytdl_player(song_to_play)
        player.start()
    except:
        await client.send_message(message.channel, 'something went wrong!\nMake sure you gave me a valid youtube video to play!')




#voice client business stuff!
#@client.event
#async def on_message(message):
    #if message.content.startswith('!playsong'):
        #discord.opus.load_opus('/usr/lib/libopus.so')
        #print(message.author.voice.voice_channel)
        #if message.author.voice.voice_channel != None:
            #voice = await client.join_voice_channel(message.author.voice.voice_channel)
            #player = await voice.create_ytdl_player('http://www.youtube.com/watch?v=HgQEuPw942c')
#            player.start()

#    if message.content.startswith('!leave'):
#        await voice.disconnect()
