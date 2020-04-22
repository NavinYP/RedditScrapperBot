import praw
import os
import urllib
import datetime
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix=".")

# RedditScraperBot v0.1
# Written by Navin Pemarathne (Storm)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.command()
async def ping(ctx):
    await ctx.send("pong")


bot_version = "v0.1"

# Getting credentials from the .env file or the cloud config.
reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"),
                     password=os.getenv("PASSWORD"),
                     user_agent=os.getenv("USER_AGENT"),
                     username=os.getenv("REDDIT_USERNAME"))

print(f"""Welcome to TempestBot {bot_version}.\n""")
client.run(TOKEN)
image_formats = [".jpeg", ".png", ".jpg", ".gif", "img",]













