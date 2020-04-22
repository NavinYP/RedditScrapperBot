import praw
import os
import urllib
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix=".")

# RedditScraperBot v0.4
# Written by Navin Pemarathne (Storm)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.command()
async def ping(ctx):
    await ctx.send("pong")


@client.command()
async def setsub(ctx, extension):
    global subreddit_name
    subreddit_name = extension
    global subreddit
    subreddit = reddit.subreddit(subreddit_name)
    await ctx.send(f"Subreddit set to {subreddit_name}")


@client.command()
async def sortmethod(ctx, extension):
    global sort_method
    sort_method = extension
    await ctx.send(f"Sort method set to {sort_method}")


@client.command()
async def pics(ctx, extension):
    submission_count = int(extension)
    for submission in subreddit.hot(limit=submission_count):
        print("Posting link...")
        await ctx.send(submission.url)  # Output: the URL the submission points to.
        print("Done!\n")

bot_version = "v0.4"

# Getting credentials from the .env file or the cloud config.
reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"),
                     password=os.getenv("PASSWORD"),
                     user_agent=os.getenv("USER_AGENT"),
                     username=os.getenv("REDDIT_USERNAME"))

print(f"""Welcome to RedditScraperBot {bot_version}.\n""")
client.run(TOKEN)
image_formats = [".jpeg", ".png", ".jpg", ".gif", "img",]
