import os
import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix= "> ", intents= intents)

# .........................[on-ready-code]......................
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# .........................[main-code]..........................
@client.command()
async def status(ctx):
    await ctx.send(f"i'm alive,\nand logged in as '{client.user}'")



# ----------------------[ run ]------------------------
try:
    client.run(os.getenv("TOKEN"))
except nextcord.HTTPException as e:
    if e.status == 429:
        print("The nextcord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-nextcord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e