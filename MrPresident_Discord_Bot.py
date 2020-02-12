"""
It's discord bot which send memes with President of Republic of Poland - Mr Duda
Type "meme!" in Discord.
"""
import random
import requests
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()
MY_KEY_API = os.getenv('MY_KEY_API')
MY_CX = os.getenv("MY_CX")


def get_google_image_query(query_text: str, number_of_results: int, start_index: int) -> dict:
    """Return request from Google Custom API"""
    req = requests.get("https://www.googleapis.com/customsearch/v1",
                       params={"key": MY_KEY_API, "cx": MY_CX, "q": query_text,
                               "searchType": "image", "num": number_of_results, "start": start_index})
    return req.json()


def get_meme_with_google(related: str) -> str:
    """Return link to photo"""
    start_index = random.randint(1, 80)
    return get_google_image_query(related, 6, start_index).get("items")[random.randint(1, 5)].get("link")


@client.event
async def on_ready():
    """Starting message"""
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} has connected to Discord!',
          f'{guild.name}(id: {guild.id})\n')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    print("Mr President is ready!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content == "meme!":
        response = get_meme_with_google("duda memy")
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException


client.run(TOKEN)
