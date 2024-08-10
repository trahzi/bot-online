import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await asyncio.sleep(float('inf'))

bot.run("Your_bot_token") # put your bot token



