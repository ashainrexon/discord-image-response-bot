# Discord Message Trigger Bot 🤖
A discord bot made in Python that responds to pre-defined keywords messaged in server chat by sending images with a small phrase.

## Overview 🚀
This mini-project was built to learn more about the uses of Discord API and explore event-driven programming. This bot monitors messages sent in the server chat it has permissions to access and triggers an image response when the specific word is detected; if there is more than one image that corresponds to that keyword, a random image is selected meaning multiple images can correspond to one word.

This is a demonstration of developing a Discord bot, message handling, automation using discord.py library and file management.

## Built With 🛠️
- Python
- Discord API

## How it Works ⚙️
1. Bot is on standby and waits till a pre-defined keyword is mentioned.
2. When it is triggered, bot searches for the corresponding text and image.
   - If there is more than one image assigned to that keyword, the bot picks a random image in that array.
3. The image and text is automatically posted in the channel.

## Installation 📦
Clone the repository:
- git clone https://github.com/ashainrexon/discord-image-response-bot.git
- cd discord-image-response-bot

Install the dependencies:
- pip install -r requirements.txt

Replace DISCORD_TOKEN with your actual token from the Discord Developer API at the very last line

Run the bot:
- python bot.py

### Customisation 🧩
The top section of the code is the keyword library, replace the "hello" with a word of your choice and replace the IMAGE_URL1 etc with your image URL and the text. You can add multiple URLs but ensure they are seperated by a comma and within the square brackets. 

Copy and paste the segment within the library and repeat above steps to add more keywords.

## Future Improvements 🔧
- Supporting symbols like slash
- Admin configuration commands
- Deployment to a cloud hosting platform
- External Database-backed storage

## What I Learned 🧠
This project helped me learn more about:
- Event-driven Programming
- Working with APIs
- Project Documentation

### License
This project is available under the MIT License.
