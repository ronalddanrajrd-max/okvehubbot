import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot connecté : {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commandes slash synchronisées")
    except Exception as e:
        print(e)


# ---------------- PREFIX COMMANDS ----------------

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")


@bot.command()
async def key(ctx):
    embed = discord.Embed(
        title="🔑 Key System",
        description="Votre clé premium est active.",
        color=0x8A2BE2
    )
    await ctx.send(embed=embed)


@bot.command()
async def stats(ctx):
    embed = discord.Embed(
        title="📊 Premium Stats",
        color=0x8A2BE2
    )

    embed.add_field(name="Users", value="152", inline=True)
    embed.add_field(name="Keys", value="87", inline=True)
    embed.add_field(name="Status", value="Online", inline=True)

    await ctx.send(embed=embed)


@bot.command()
async def helpme(ctx):
    embed = discord.Embed(
        title="📖 Commands",
        color=0x8A2BE2
    )

    embed.add_field(name="!ping", value="Ping bot", inline=False)
    embed.add_field(name="!stats", value="Show stats", inline=False)
    embed.add_field(name="!key", value="Show key", inline=False)

    await ctx.send(embed=embed)


# ---------------- SLASH COMMANDS ----------------

@bot.tree.command(name="redeem", description="Redeem premium key")
async def redeem(interaction: discord.Interaction, key: str):

    embed = discord.Embed(
        title="✅ Key Redeemed",
        description=f"Key: `{key}`",
        color=0x00ff00
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="getscript", description="Get premium script")
async def getscript(interaction: discord.Interaction):

    embed = discord.Embed(
        title="📜 Premium Script",
        description="```lua\nprint('Premium Script Loaded')\n```",
        color=0x8A2BE2
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="resethwid", description="Reset HWID")
async def resethwid(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🔄 HWID Reset",
        description="Votre HWID a été reset.",
        color=0xff9900
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="userinfo", description="User information")
async def userinfo(interaction: discord.Interaction):

    user = interaction.user

    embed = discord.Embed(
        title="👤 User Info",
        color=0x8A2BE2
    )

    embed.add_field(name="Username", value=user.name)
    embed.add_field(name="ID", value=user.id)

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="help", description="Show commands")
async def helpslash(interaction: discord.Interaction):

    embed = discord.Embed(
        title="📖 Help Menu",
        color=0x8A2BE2
    )

    embed.add_field(name="/redeem", value="Redeem key", inline=False)
    embed.add_field(name="/getscript", value="Get script", inline=False)
    embed.add_field(name="/resethwid", value="Reset HWID", inline=False)
    embed.add_field(name="/userinfo", value="User info", inline=False)

    await interaction.response.send_message(embed=embed)


bot.run(TOKEN)
