import os
import time
import discord
import requests
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as "{client.user}" (ID: {client.user.id})')
    await client.tree.sync()

@client.tree.command(name="lookup", description="Look up a Kiseki user by their username or ID")
async def lookup(interaction: discord.Interaction, query: str):
    await interaction.response.defer()

    url = f"{os.getenv('KISEKI_URL')}/periwinkle/user/lookup"
    headers = { "Authorization": os.getenv('API_KEY') }
    params = { "query": query }

    response = requests.post(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        join_date_unix = data.get("created_at")
        join_date = datetime.fromtimestamp(join_date_unix, tz=timezone.utc)
        join_date_human = discord.utils.format_dt(join_date, style='R')

        embed = discord.Embed(
            title=data.get("name"),
            url=f"{os.getenv('KISEKI_URL')}/user/profile",
            color=0x8540ff
        )
        embed.add_field(name="Currency", value=data.get("currency"), inline=False)
        embed.add_field(name="Account age", value=join_date_human, inline=False)

        await interaction.followup.send(embed=embed)

    else:
        await interaction.followup.send(f"failed to lookup user: {response.error}")

client.run(os.getenv('TOKEN'))