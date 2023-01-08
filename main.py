# bot.py
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.typing = True
intents.message_content = True
intents.guilds = True
intents.voice_states = True

f = open('TOKEN.txt','r')
TOKEN = f.read()
f.close()

bot = commands.Bot(command_prefix='//', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# @bot.command()
# async def hello(ctx):
#     if ctx.author != bot.user:
#         await ctx.send('Heya')

# @bot.command()
# async def repeat(ctx,arg):
#     await ctx.send(arg)
        
# @bot.command()
# async def listMember(ctx, arg: int):
#     a = ctx.guild.members
#     await ctx.send(a[arg])

@bot.event
async def on_voice_state_update(member,before,after):
    if str(member) == "Sammie#0901": #[ ]change to lothym#5083
        # a = str(after).split(sep=" ")
        # for x in a:
        #     print(x)
        # print("\n\n")
        a = discord.VoiceState.self_video()
        print(a)


bot.run(TOKEN)
