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
targets_dm = os.environ.get("TARGETS_DM").split(";")

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name} ({bot.user.id})')
    for guild in bot.guilds:
        for target in targets:
            user = guild.get_member(int(target))
            if user.activity:
                print(f"{user.name}: " + user.activity.name)
                print(user.activity.start)
                for dm in targets_dm:
                    user_dm = await guild.get_member(int(dm)).create_dm()
                    await user_dm.send(user.name + " napierdala w " + user.activity.name )






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