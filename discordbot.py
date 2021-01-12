from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
def __init__(self, bot):
     self.bot = bot


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
async def tem(ctx):
    await ctx.send('ワンワン')

    @commands.command(pass_context=True)
    async def quickpoll(self, ctx, question, *options: str):
        if len(options) <= 1:
            await self.bot.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await self.bot.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description))
        react_message = await self.bot.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await self.bot.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await self.bot.edit_message(react_message, embed=embed)
    
bot.run(token)
