import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connected: {bot.user}")
    await bot.tree.sync()

@bot.tree.command(name="stats", description="Stats")
async def stats(interaction: discord.Interaction):
    embed = discord.Embed(title="Premium Stats", color=0x8A2BE2)
    embed.add_field(name="Users", value="152")
    embed.add_field(name="Status", value="Online")
    await interaction.response.send_message(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)
