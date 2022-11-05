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



# .........................[fun cmd]..........................
# -------------------------[to emoji]-------------------------
@client.slash_command(name= "toemoji", description= "convert text to emoji")
async def toemoji(self, interaction: Interaction, msg: str):
    emojis = []     #<- empty array>
    # gets all the letter in the msg
    for s in msg.lower():
        if s.isalpha():
            emojis.append(f":regional_indicator_{s}:")
        else:
            emojis.append(s)
    await interaction.response.send_message(' '.join(emojis))

# -------------------------[coin]-------------------------------
@client.slash_command(name= "flipcoin", description= "coin flip")
async def coin(self, interaction: Interaction):
    coinlist = ["heads", "tails"]   #<- coin list>
    embed = nextcord.Embed(title="coin", description= f"coin => {random.choice(coinlist)}")
    await interaction.response.send_message(embed= embed)

# -------------------------[choose]-----------------------------
@client.slash_command(name= "choose", description="choose a person")
async def choose(self, interaction: Interaction, limit: int):
    chosenPerson = random.randint(1, limit)
    embed = nextcord.Embed(title= "God will choose!!!")
    embed.add_field(name= f"God ", value = f"=> {chosenPerson}")
    await interaction.response.send_message(embed = embed)

# ----------------------[ run ]------------------------
try:
    client.run(os.getenv("TOKEN"))
except nextcord.HTTPException as e:
    if e.status == 429:
        print("The nextcord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-nextcord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e