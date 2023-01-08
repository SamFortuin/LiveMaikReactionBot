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

f = open('TOKEN.txt','r') #grabs token from local file
TOKEN = f.read()
f.close()

bot = commands.Bot(command_prefix='//', intents=intents) #discord.ext way of creating user

@bot.event
async def on_ready():
    print(f'{bot.user} is ready')

@bot.event
async def on_voice_state_update(member,before,after):
    if str(member) == "Sammie#0901": #[ ]change to lothym#5083
        a = str(after).split(sep=" ") # grabs after object and turns it into a list for reading
        for x in a: #I forgor how to do it with *a and sep so this is how we're doing it for now
            print(x)
        print("\n\n")


bot.run(TOKEN)
