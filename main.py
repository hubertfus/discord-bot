import discord
from discord.ext import commands, tasks
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

token = os.environ.get("TOKEN")
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
targets = os.environ.get("TARGETS").split(";")

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name} ({bot.user.id})')
    for guild in bot.guilds:
        for member in guild.members:
            for target in targets:
                if target == f'{member.id}':
                    dm_channel = await member.create_dm()
                    await dm_channel.send("test")




@bot.event
async def on_message(message):
    if message.author != bot.user and "chuj" in message.content.lower():
        await message.reply('Spierdalaj cwelu!')

@bot.command()
async def reply(ctx, *, reply_content: str):
    await ctx.send(reply_content)

@bot.command()
async def trigger_reply(ctx):
    await bot.dispatch('reply', ctx, reply_content='spierdalaj cwelu')


bot.run(token)