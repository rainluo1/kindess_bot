import discord
import os
from discord.ext import commands
def run_discord_bot():
    TOKEN = 'MTA1NzM5MzM3MTQ1NjQ3NTIzNg.GyUE4y.M8-92RqKcsfSznzZ6hc-jCRwg-p2wBdg6z7TlE'
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel)
        print(f'{username}:{user_message}({channel}))')

        if message.author == client.user:  # preventing the bot from speaking with itself
            return
        msg = user_message.lower()
        if msg == 'hello':
            await message.channel.send(f'Hello {username}')
        if msg == '!help':
            await message.channel.send(f'''Hello {username} 
I am the kindness bot. My duties is to prevent harassment by supervising the chat.''')
        else:
            f = open('curse word.txt', 'r')
            data = f.readline()
            word = data.split()
            for x in word:
                if msg.__contains__(x):  # meaning that the chat message have curse word
                    await message.reply(f'Hey mind your language! Next time you will be kicked')
                    await kick({username})
    client.run(TOKEN)


    @client.command()
    async def kick(ctx, member : discord.Member, *,reason = None):
            await member.kick( reason = reason)

    @client.command()
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)


