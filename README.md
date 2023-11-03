# Discord Lyric Bot

## The Description

This Discord bot is designed to perform the following tasks:

1. Lyrics Management: You can use the bot to manage and retrieve song lyrics. It allows you to add, update, and retrieve lyrics for songs. Users can upload text files containing lyrics, and the bot stores them for later retrieval.

2. Multi-Word Song Names: The bot supports multi-word song names with spaces. Users can enclose song names in double quotes to create or update lyrics files with full names.

3. Usage of Commands:

	- `$lyrics add <song_name>`: Adds lyrics for the specified song. Users must upload a text file containing the lyrics.
	- `$lyrics update <song_name>`: Updates the lyrics for the specified song. Users must upload a text file with updated lyrics.
	- `$lyrics show <song_name>`: Retrieves and displays the lyrics for the specified song.
	
	
## Getting Started

To run this bot, follow these steps:

1. Ensure you have Python installed on your system.

2. Install the required Python packages by running the following command in your bot's directory:

```pip install discord.py```

3. Configure the bot by setting up a Discord bot application on the Discord Developer Portal. 
Create a bot, get the token, and invite it to your server.

4. Run the bot using the following command:

```python bot.py```

Or use the `start.bat` script for Windows, or `start.sh` script for Linux.


## LICENSE
This project is licensed by the GNU General Public License v3.0
