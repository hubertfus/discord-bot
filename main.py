import discord
from discord.ext import commands, tasks
import os
from os.path import join, dirname
from dotenv import load_dotenv
import asyncio
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

token = os.environ.get("TOKEN")
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
targets = os.environ.get("TARGETS").split(";")
targets_dm = os.environ.get("TARGETS_DM").split(";")
# game_targets = os.environ.get("GAME_TARGETS").split(";")

online = []
# online_in_game = []
@bot.event
async def on_ready():
    while(True):
        for guild in bot.guilds:
            for target in targets:
                user = guild.get_member(int(target))
                if user.activity:
                    if user.name not in online:
                        online.append(user.name)
                        for dm in targets_dm:
                            user_dm = await guild.get_member(int(dm)).create_dm()
                            await user_dm.send(user.name + " napierdala w " + user.activity.name)
                elif user.name in online:
                    online.remove(user.name)
        # for guild in bot.guilds:
        #     for member in guild.members:
        #         if member.activity:
        #             if member.name not in online_in_game:
        #                 online_in_game.append(member.name)
        #                 for game in game_targets:
        #                     if member.activity.name == game:
        #                         user_dm = guild.get_channel(int(1184204317712973906))
        #                         await user_dm.send(f"{member.mention} pojebabało cię ciapaczku żeby w to grać")
        #         elif member.name in online_in_game:
        #             online_in_game.remove(member.name)
        await asyncio.sleep(3)


@bot.event
async def on_message(message):
    if message.author != bot.user:
        sendmesage = 'Chodź na słówko! :rage:'
        if "tyski" in message.content.lower() or "siost" in message.content.lower() or "fortn" in message.content.lower():
            await message.reply(sendmesage)




bot.run(token)