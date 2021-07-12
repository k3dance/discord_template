import discord
from config.config import PREFIX, TOKEN
from discord.ext import commands

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

# LOAD THE CLASSES
bot.load_extension('classes.main')

# RUN THE BOT
bot.run(TOKEN)