from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def inu(ctx):
    await ctx.send('ワンワン')

@bot.command()
async def poll(ctx):
    await ctx.add_reaction(👍)
    await ctx.send('[参加]\n[不参加]\n[未定]\n[未回答]')
   
    
bot.run(token)
