from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('ぽんぽんぽんっ')
    
@bot.command()
async def mogukun(ctx):
    await ctx.send('呼んだ？')


bot.run(token)
