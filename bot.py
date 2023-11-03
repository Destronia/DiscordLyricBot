import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def lyrics(ctx, action, *, song_name):
    # Construct the file path for the requested song
    file_path = f'lyrics/{song_name}.txt'

    # Check if the action is "add"
    if action == "add":
        # Check if the file already exists
        if os.path.isfile(file_path):
            await ctx.send(f"Lyrics for '{song_name}' already exist. To update, use '$lyrics update <song_name>'.")
            return

        # Check if a file is attached to the message
        if not ctx.message.attachments:
            await ctx.send("Please attach a text file with the lyrics to add.")
            return

        # Download and save the attached file
        attachment = ctx.message.attachments[0]
        filename, file_extension = os.path.splitext(attachment.filename)
        valid_extensions = ['.txt', '.text']

        if file_extension in valid_extensions:
            content = await attachment.read()
            with open(file_path, "wb") as file:
                file.write(content)
            await ctx.send(f"Lyrics for '{song_name}' have been added.")
        else:
            await ctx.send("The attached file is not a valid text file.")

    # Check if the action is "update"
    elif action == "update":
        # Check if the file exists
        if not os.path.isfile(file_path):
            await ctx.send(f"Lyrics for '{song_name}' not found. To add, use '$lyrics add <song_name>'.")
            return

        # Check if a file is attached to the message
        if not ctx.message.attachments:
            await ctx.send("Please attach a text file with the updated lyrics.")
            return

        # Download and save the attached file as an update
        attachment = ctx.message.attachments[0]
        filename, file_extension = os.path.splitext(attachment.filename)
        valid_extensions = ['.txt', '.text']

        if file_extension in valid_extensions:
            content = await attachment.read()
            with open(file_path, "wb") as file:
                file.write(content)
            await ctx.send(f"Lyrics for '{song_name}' have been updated.")
        else:
            await ctx.send("The attached file is not a valid text file for updating.")

    # Check if the action is "show"
    elif action == "show":
        # Check if the file exists
        if not os.path.isfile(file_path):
            await ctx.send(f"Lyrics for '{song_name}' not found.")
            return

        # Read and display the contents of the text file
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lyrics = file.read()
            await ctx.send(f"Lyrics for '{song_name}':\n```{lyrics}```")
        except Exception as e:
            print("Error:", e)  # Debugging line
            await ctx.send(f"Error reading lyrics for '{song_name}'.")

# Replace 'YOUR_TOKEN' with your bot's token
bot.run('YOUR_TOKEN')
