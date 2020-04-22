import praw
import dotenv
import os
import urllib
import datetime
import discord


from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
client = discord.Client()

# RedditScraperBot v0.3

bot_version = "v0.3"

# Getting credentials from the .env file.
# todo:Might have to change this later.
reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"),
                     password=os.getenv("PASSWORD"),
                     user_agent=os.getenv("USER_AGENT"),
                     username=os.getenv("REDDIT_USERNAME"))

current_directory = os.getcwd()


def get_subreddit_name():
    user_input = input("Please enter the desired subreddit name: ")
    return user_input


def subreddit_intro():
    print(f"""You are currently in this subreddit:
    {subreddit.display_name}
    {subreddit.title}""")


def get_subreddit():
    user_input = reddit.subreddit(subreddit_name)
    return user_input


def get_submission_count():
    user_input = int(input("How many submission links do you want?: "))
    return user_input


def print_submissions_full():
    for submission in sort_methods[method_number](limit=number_of_submissions):
        print(submission.title)  # Output: the submission's title
        print(submission.score)  # Output: the submission's score
        print(submission.id)  # Output: the submission's ID
        print(submission.url)  # Output: the URL the submission points to


def download_images():
    time_now = datetime.now()
    current_timestamp = time_now.strftime(f"%y_%m_%d_%H_%M_%S")

    if path.exists(f"{current_directory}/downloads"):
        pass
    else:
        os.mkdir(f"{current_directory}/downloads")

    folder_name = f"{subreddit_name}_{current_timestamp}"
    os.mkdir(f"{current_directory}/downloads/{folder_name}")
    for submission in sort_methods[method_number](limit=number_of_submissions):
        if any(ext in submission.url for ext in image_formats):
            filename = submission.url.split('/')[-1]
            print(filename)
            urllib.request.urlretrieve(submission.url, f"{current_directory}/downloads/{folder_name}/{filename}")
            print("Download complete.\n")

        elif "reddituploads" in submission.url:
            filename = submission.url.split("/")[-1].split("?")[0]
            print(filename)
            urllib.request.urlretrieve(submission.url, f"{current_directory}/downloads/{folder_name}/{filename}.jpg")
            print("Download complete.\n")


image_formats = [".jpeg", ".png", ".jpg", ".gif", "img",]

print(f"""Welcome to TempestBot {bot_version}.\n""")

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

client.run(TOKEN)









