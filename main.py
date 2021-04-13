from discord.ext import commands
from discord.ext.commands import Bot

client: Bot = commands.Bot(command_prefix="&")

@client.event
async def on_ready():
    print("bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("HI")

client.run("ODMwMzMxMDMyODA4MzI1MTYw.YHFICQ.KKslb8D3r4bvtYWOSNI01RiHctk")

