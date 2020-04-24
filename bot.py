import praw
import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix="?")
client.remove_command("help")

bot_version = "v1.1"
# RedditScraperBot v1.1
# Written by Navin Pemarathne (Storm)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("?help general for help."))
    print(f"{client.user} has connected to Discord!")


@client.command()
async def setsub(ctx, extension):
    subreddit_name = extension
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
async def scrape(ctx, extension):
    image_formats = [".jpeg", ".png", ".jpg", ".gif", "img", "reddituploads", "gfycat", "imgur"]
    submission_count = int(extension)

    if "sort_method" in globals():
        pass
    else:
        global sort_method
        sort_method = "top"

    for submission in sort_methods[sort_method](limit=submission_count):
        if any(ext in submission.url for ext in image_formats):
            print("Posting link...")
            await ctx.send(submission.url)  # Output: the URL the submission points to.
            print("Done!\n")
        else:
            submission_count += 1
    print("Task completed.")
    await ctx.send("Task completed.")


@scrape.error
async def scrape_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Please set a valid subreddit name.")


@client.command()
async def settime(ctx, extension):
    global time_mode # Can be all, day, hour, month, week, year (default: all).
    time_mode = extension
    await ctx.send(f"Time sort set to {time_mode}")


# @client.command()
# async def keyword(ctx, extension):
#     global keyword
#     keyword = extension
#     await ctx.send(f"Keyword is {keyword}")


@client.command()
async def search(ctx, extension, extension2):
    image_formats = [".jpeg", ".png", ".jpg", ".gif", "img", "reddituploads", "gfycat", "imgur"]
    submission_count = int(extension2)
    count = submission_count
    keyword = extension

    if "time_mode" in globals():
        pass
    else:
        global time_mode
        time_mode = "all"

    if "sort_method" in globals():
        pass
    else:
        global sort_method
        sort_method = "top"

    for submission in reddit.subreddit(subreddit_name).search(keyword, sort_method, "lucene", time_mode):
        if submission_count > 0:
            if any(ext in submission.url for ext in image_formats):
                print("Posting link...")
                await ctx.send(submission.url)  # Output: the URL the submission points to.
                print("Done!\n")
                submission_count -= 1
    print("Task completed.")
    await ctx.send("Task completed.")


@search.error
async def search_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Please set a valid subreddit name.")


@client.command()
async def help(ctx, extension):
    author = ctx.message.author

    embed = discord.Embed(
        color=discord.Color.orange()
    )

    if extension == "general":
        embed.set_author(name="General Help")
        embed.add_field(name="?setsub <subreddit_name>", value="Sets the current subreddit. (Default - /r/all)",
                        inline=False)
        embed.add_field(name="?sort <sort_method>", value="Sets the current sort method. (Default - top)", inline=False)
        embed.add_field(name="?settime <time_sort_method>", value="Sets the timeframe. (Default - all)", inline=False)
        embed.add_field(name="?scrape <number_of_pics>", value="Scrapes the subreddit and posts the number of pics want"
                                                               "ed.", inline=False)
        embed.add_field(name="?search <keyword> <number_of_pics>", value="Search the subreddit using the set parameters"
                                                                         " and posts the number of pics wanted.",
                        inline=False)
        embed.add_field(name="?help <command_name>", value="Shows more info about the required command", inline=False)

    if extension == "sort":
        embed.set_author(name="sort <sort_method>")
        embed.add_field(name="Available reddit sort methods.", value="top\nrising\nhot\nnew\ngilded\ncontroversial",
                        inline=False)

    if extension == "settime":
        embed.set_author(name="settime <time_sort_method>")
        embed.add_field(name="Available time sort methods.", value="all\nday\nhour\nmonth\nweek\nyear\n\nDefault - all",
                        inline=False)

    await ctx.send(embed=embed)


# @client.command()
#     async def debug(ctx, extension):

# Getting credentials from the .env file or the cloud config.
reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"),
                     password=os.getenv("PASSWORD"),
                     user_agent=os.getenv("USER_AGENT"),
                     username=os.getenv("REDDIT_USERNAME"))

print(f"""Welcome to RedditScraperBot {bot_version}.\n""")

subreddit_name = "all"
subreddit = reddit.subreddit(subreddit_name)

client.run(TOKEN)

