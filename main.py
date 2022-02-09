from keep_alive import keep_alive

import os
import discord
import os

client = discord.Client()
penis_triggers=["penis", "shaft", "member","weenie","cock","dick","phallus","prick","willy","wood","schlong","dong","wiener","wang","sausage","pee-pee"]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
 
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if any(word in msg for word in penis_triggers):
      await message.channel.send('HAHA PENIS')
keep_alive()
client.run(os.getenv('TOKEN'))

my_secret = os.environ['TOKEN']
