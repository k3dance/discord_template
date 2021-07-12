import discord
from discord.ext import commands
from discord.ext.commands import bot


class Base(commands.Cog):

    def __init__(self, Bot):
        self.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Base commands successfully added to bots functional')

    @commands.command(name='hello', aliases=['hi'])
    async def _hello(self, ctx):
        await ctx.send(f'{ctx.author.mention}, hello!')


def setup(Bot):
    Bot.add_cog(Base(Bot))