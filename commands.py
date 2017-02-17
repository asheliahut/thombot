#command list for thombot

import discord
import asyncio
import random
import requests

#random cat image
async def cat(client, message):
    ran_cat_link = random.choice(['http://thecatapi.com/api/images/get','http://random.cat/meow'])
    if ran_cat_link == 'http://random.cat/meow':
        ran_cat = requests.get(ran_cat_link).json()["file"]
    else:
        ran_cat = requests.get(ran_cat_link).url
    await client.send_message(message.channel, ran_cat)

#random nickelback song when someone posts @nickelback
async def nickelback(client, message):
    songs = ('https://www.youtube.com/watch?v=BB0DU4DoPP4','https://www.youtube.com/watch?v=4OjiOn5s8s8','https://www.youtube.com/watch?v=_1hgVcNzvzY','https://www.youtube.com/watch?v=PvxVNGdwVwk','https://www.youtube.com/watch?v=JtxpcQaSR0k','https://www.youtube.com/watch?v=76RbWuFll0Y','https://www.youtube.com/watch?v=1cQh1ccqu8M','https://www.youtube.com/watch?v=wQzn4a5qHT4','https://www.youtube.com/watch?v=-qcZ9M-QoOc','https://www.youtube.com/watch?v=5RtTFP2TNcM','https://www.youtube.com/watch?v=GP7zpdwo3Xo','https://www.youtube.com/watch?v=FIjRo-gMlKE','https://www.youtube.com/watch?v=vt-UtzP1u1g');
    rand_song = random.choice(songs)
    await client.send_message(message.channel, rand_song)

#lets users get help!
async def bothelp(client, message):
    help_file = open('/home/pi/thombot/helpinfo.txt','r')
    help_info = help_file.read()
    await client.send_message(message.author, help_info)
    help_file.close()

#random harambe picture
async def harambe(client, message):
    harambe_pics = ('Harambe.jpg','Harambe2.jpg','Harambe3.jpg','Harambe4.jpg','Harambe5.jpg','Harambe6.jpg','Harambe7.jpg','Harambe8.jpg')
    await client.send_file(message.channel, '/home/pi/thombot/pictures/harambe/' + random.choice(harambe_pics))

#post a persons mastersoverwatch page using their battletag
async def ostats(client, message):
     tag_check = r'(\w+)-(\d+)'
     match_check = re.search(tag_check, message.content)
     if match_check:
        await client.send_message(message.channel, 'http://masteroverwatch.com/profile/pc/us/' + match_check.group())
     else:
        await client.send_message(message.channel, 'Incorrect battletag format.\nPlease use the format \' !ostats battletag-1234\'')

#change the currently playing game. Must have bot friend role to use
async def gameset(client,message):
    role_test = 1
    for role in message.author.roles:
        if role.name == 'bot friend':
            game_name = message.content[9:]
            await client.change_presence(game=discord.Game(name=game_name))
            role_test = 0
            break
    if role_test == 1:
        await client.send_message(message.channel, 'you\'re not a bot friend!')

#post sombra shit
async def sombra(client, message):
    await client.send_file(message.channel, '/home/pi/thombot/pictures/sombra.jpg')

#post aliens guy
async def aliens(client,message):
    await client.send_file(message.channel, '/home/pi/thombot/pictures/aliens.png')

#return the slab, maybe do soemthing better later. Not sure what else i could do though.
async def slab(client,message):
    await client.send_message(message.channel, 'RETURN THE SLAAAAB')

#can't wake up
async def wakemeup(client,message):
    await client.send_message(message.channel, 'no')


async def setavatar(client,message):
    role_test = 1
    for role in message.author.roles:
        if role.name == 'bot friend':
            avatar = open('/home/pi/thombot/pictures/avatar.jpg', 'rb')
            await client.edit_profile(avatar=avatar.read())
            role_test = 0
            break
    if role_test == 1:
        await client.send_message(message.channel, 'You\'re not a bot friend!')

async def tillISeeYou(client,message):
    url = 'http://iwillseeyousoon.com/countdown.php'
    days = requests.get(url).text
    await client.send_message(message.channel, 'Ashley gets to see Trevor in '+ days + ' days!')

async def dva(client, message):
    await client.send_file(message.channel, '/home/pi/thombot/pictures/dva.png')

async def stfu(client, message):
    await client.send_message(message.channel, 'https://youtu.be/OLpeX4RRo28')

async def doomfist(client, message):
    await client.send_file(message.channel, '/home/pi/thombot/pictures/doomfist.jpg')

async def ban(client, message):
    await client.send_message(message.channel, 'you\'ve been banned, {}!'.format(message.mentions[0].mention))

async def melonfic(client, message):
    await client.send_message(message.channel, 'Melon fanfic by ttariel')
    await client.send_message(message.channel, 'IT WAS A WARM DAY IN MELON LAND HEN SUDDENLY WITH SHOCK MNELON DAD WOKE UP AND FOUND A GUN UNDER HIS BED; HE STOOD UP AND WENDT OUTSIDE AND WFOUND IT WAS WAR OUTSIDE AND ALSO HIS SON WAS GOEN SO HE WENT TO OUTSIDE AND LOOKED FOR HIS SUN WHEN SUDDENLY WITH SHOCK HIS BAD EVIL ATTACKED HIM AND HE KILLED')
    await client.send_message(message.channel, 'SO HE KEEPT GOING TO FIND CHILD BUT CHILD STILL GONE SO SEARCH WILL GO ON')
    await client.send_message(message.channel, 'HE MEETS OTHER BAD GUY BUT HE IS EXTAR EVIL SO HE SHOOTS HIS GUN BUT GUN IS EMPTY SO HE HAS TO FIGHT LIEK THE OLD WORLDF DID WITH FIST ROCKS AND FIITS')
    await client.send_message(message.channel, 'HE KICKD AND PUNCHD AND WAS ALL IN HIS MIDN WHEN SUDDENLY YOU WANT TO TEST HIM IM SURE OYU FIND THE THINGS I TEACH YA ARE ASURE TO BEATCHA YA')
    await client.send_message(message.channel, 'SO HE KILLS AND KEEPS GOING')
    await client.send_message(message.channel, 'WHEN SUDDENLY HE FINS CHILD BEING SLAVE BY BAD SO HE KILLS PEOPLE AND FIND S SONE ANDS SAID CHILD YOU ARE BACK NOW')
    await client.send_message(message.channel, 'AND CHIDL SAID')
    await client.send_message(message.channel, 'YES PAPA')
    await client.send_message(message.channel, 'AND TEHY WNTES HOME WHEN SUDDENLY WITH SHOCK')
    await client.send_message(message.channel, 'EVIL ATATCKS AGAIN')
    await client.send_message(message.channel, 'SO FATHER MELOMN TAKES HCILD MELON ANDS YELSS')
    await client.send_message(message.channel, 'I WILL BEAT YOU WITH POWER OF PARENT')
    await client.send_message(message.channel, 'AND HE KILLED EVIÖL')
    await client.send_message(message.channel, 'THEY WNET HOME AND GOT HAIRCUT THE END')
    await client.send_message(message.channel, 'done')

#async def test(client, message):
    #for channel in message.server.channels:
        #if channel.id == '85228383054594048':
            #cream = discord.Channel(id = '85228383054594048')
            #await client.send_message(channel, 'please work')
