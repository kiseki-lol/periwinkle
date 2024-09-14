import os
import discord
import humanize

from discord import app_commands
from discord.ext import commands
from .api import get

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as "{client.user}" (ID: {client.user.id})')
    await client.tree.sync()

@app_commands.command(name="lookup", description="Look up a Kiseki user by their username or ID")
async def lookup(interaction: discord.Interaction, query: str):
    await interaction.response.defer()

    data = get("user/lookup", {"query": query})

    if not data.get("error"):
        embed = discord.Embed(
            title=data.get("name"),
            url=f"{os.getenv('KISEKI_URL')}/user/profile",
            color=0x8540ff
        )
        embed.add_field(name="Blurb", value=data.get("blurb", "No blurb available"), inline=False)
        embed.add_field(name="Currency", value=humanize.intword(data.get("currency")), inline=True)
        embed.add_field(name="Account age", value=data.get("age"), inline=True)

        await interaction.followup.send(embed=embed)
    else:
        await interaction.followup.send(f"failed to lookup user, status code: {data.get('error')}")

client.tree.add_command(lookup)