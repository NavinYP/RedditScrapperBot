import praw
import os
import urllib
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix=".")

# RedditScraperBot v1.0
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

    global sort_methods
    sort_methods = {"controversial": subreddit.controversial, "gilded": subreddit.gilded, "hot": subreddit.hot,
                    "new": subreddit.new, "rising": subreddit.rising, "top": subreddit.top}


@client.command()
async def sort(ctx, extension):
    global sort_method
    sort_method = extension
    await ctx.send(f"Sort method set to {sort_method}")


@client.command()
async def pics(ctx, extension):
    image_formats = [".jpeg", ".png", ".jpg", ".gif", "img", "reddituploads", "gfycat", "imgur"]
    submission_count = int(extension)
    for submission in sort_methods[sort_method](limit=submission_count):
        if any(ext in submission.url for ext in image_formats):
            print("Posting link...")
            await ctx.send(submission.url)  # Output: the URL the submission points to.
            print("Done!\n")
        else:
            submission_count += 1
    print("Task completed.")


@client.command()
async def settime(ctx, extension):
    global time_mode # Can be all, day, hour, month, week, year (default: all).
    time_mode = extension
    await ctx.send(f"Time sort set to {time_mode}")


@client.command()
async def keyword(ctx, extension):
    global keyword
    keyword = extension
    await ctx.send(f"Keyword is {keyword}")


@client.command()
async def search(ctx, extension):
    image_formats = [".jpeg", ".png", ".jpg", ".gif", "img", "reddituploads"]
    submission_count = int(extension)
    count = submission_count
    for submission in reddit.subreddit(subreddit_name).search(keyword, sort_method, "lucene", time_mode):
        if submission_count > 0:
            if any(ext in submission.url for ext in image_formats):
                print("Posting link...")
                await ctx.send(submission.url)  # Output: the URL the submission points to.
                print("Done!\n")
                submission_count -= 1
    print("Task completed.")


bot_version = "v1.0"

# Getting credentials from the .env file or the cloud config.
reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"),
                     password=os.getenv("PASSWORD"),
                     user_agent=os.getenv("USER_AGENT"),
                     username=os.getenv("REDDIT_USERNAME"))

print(f"""Welcome to RedditScraperBot {bot_version}.\n""")
client.run(TOKEN)

