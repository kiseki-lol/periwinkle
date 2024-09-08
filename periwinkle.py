import os
import time
import discord
import requests
import humanize

from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as "{client.user}" (ID: {client.user.id})')
    await client.tree.sync()

@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)

@client.tree.command(name="lookup", description="Look up a Kiseki user by their username or ID")
async def lookup(interaction: discord.Interaction, query: str):
    await interaction.response.defer()

    url = f"{os.getenv('KISEKI_URL')}/api/periwinkle/user/lookup"
    headers = { "Authorization": os.getenv('API_KEY') }
    params = { "query": query }

    response = requests.post(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        embed = discord.Embed(
            title=data.get("name"),
            url=f"{os.getenv('KISEKI_URL')}/user/profile",
            color=0x8540ff
        )
        embed.add_field(name="Blurb", value=data.get("blurb"), inline=False)
        embed.add_field(name="Currency", value=humanize.intword(data.get("currency")), inline=True)
        embed.add_field(name="Account age", value=data.get("age"), inline=True)

        await interaction.followup.send(embed=embed)
    else:
        await interaction.followup.send(f"failed to lookup user, status code: {response.status_code}")

client.run(os.getenv('TOKEN'))
