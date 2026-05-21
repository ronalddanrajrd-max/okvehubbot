import os
import discord
import aiohttp
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
API_URL = "https://perfect-upliftment-production-c953.up.railway.app"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté : {bot.user}")
    await bot.tree.sync()

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.tree.command(name="stats", description="Voir les stats whitelist")
async def stats(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}/stats") as response:
            data = await response.json()

    embed = discord.Embed(title="📊 Premium Stats", color=0x8A2BE2)
    embed.add_field(name="Total Keys", value=data["total_keys"], inline=True)
    embed.add_field(name="Redeemed", value=data["redeemed"], inline=True)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="redeem", description="Activer une clé premium")
async def redeem(interaction: discord.Interaction, key: str, hwid: str):
    payload = {
        "key": key,
        "discord_id": str(interaction.user.id),
        "hwid": hwid
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(f"{API_URL}/redeem", json=payload) as response:
            data = await response.json()

    if data["success"]:
        await interaction.response.send_message("✅ Key activée avec succès.", ephemeral=True)
    else:
        await interaction.response.send_message(f"❌ {data['message']}", ephemeral=True)

@bot.tree.command(name="getscript", description="Recevoir le script premium")
async def getscript(interaction: discord.Interaction):
    script = "```lua\nprint('Premium script loaded')\n```"
    await interaction.response.send_message(script, ephemeral=True)

@bot.tree.command(name="resethwid", description="Reset HWID")
async def resethwid(interaction: discord.Interaction, key: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{API_URL}/reset-hwid?key={key}") as response:
            data = await response.json()

    if data["success"]:
        await interaction.response.send_message("✅ HWID reset.", ephemeral=True)
    else:
        await interaction.response.send_message("❌ Key introuvable.", ephemeral=True)

bot.run(TOKEN)
