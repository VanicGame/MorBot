import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

# Сообщение о готовности
@bot.event 
async def on_ready():
    print('yes')



bot.run(os.environ['MorTok'])
