import discord
from discord.ext import commands
import numpy as np
from PIL import Image

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True
intents.message_content = True
intents.voice_states = True
intents.emojis = True
intents.emojis_and_stickers = True

#grabs token from local file
with open('TOKEN.txt','r') as f:
    TOKEN = f.read()

bot = commands.Bot(command_prefix='//', intents=intents) #discord.ext way of creating user

@bot.event
async def on_ready():
    print(f'{bot.user} is ready')

@bot.event
async def on_voice_state_update(member,before,after):
    if str(member) == "Sammie#0901": #[ ]change to lothym#5083
        a = str(after).split(sep=" ") # grabs after object and turns it into a list for reading
        for x in a: #I forgor how to do it with *a and sep so this is how we're doing it for now, we won't need this shit in the future anyway
            print(x)
        print("\n\n")

@bot.command() #manually triggered for now
async def memeify(ctx):
    list_im = [r'images\Header.jpg',r'images\testMeme.jpg']
    imgs = [Image.open(i) for i in list_im]
    imgs_comb = np.vstack([i for i in imgs])

    #save & send
    imgs_comb = Image.fromarray(imgs_comb)
    imgs_comb.save(r'images\finalMeme.png')
    await ctx.send(file=discord.File(r'D:\Users\Sammi\Desktop\LiveMaikReactionBot\images\finalMeme.png'))

"""
[ ] figure out the getting of the screenshot
[ ] write code for updating the emote
[ ] use datetime to make a yearly recap on Maik's birthday
[ ] archive all the created maiks on a website
"""

bot.run(TOKEN)