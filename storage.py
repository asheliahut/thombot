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



if message.content.startswith('!v '):
    voice_channel_service = None
    if message.content.startswith('!v joinchannel'):
        voice_channel_service = await voice.joinchannel(client,message)
    else:
        await getattr(voice, input_command.group(0)[2:])(client, message_channel_service, voice_channel_service)
    if message.content.startswith('!v leavechannel'):
        voice_channel_service = None
