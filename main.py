import os
import discord 
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="info")
async def infoContext(ctx):
    print(ctx)
    await ctx.send("Info Context !")

discordToken = os.getenv('DISCORD_BOT_TOKEN')
bot.run(discordToken)