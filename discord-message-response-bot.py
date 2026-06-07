import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

# Dictionary, includes arrays but idk why its not working
image_responses = {
    #Each keyword has 2 fields, the image URL and a phrase that it returns as a message on the server
    "$hello": {
        "text": "Welcome 👋",
        "images": ["IMAGE_URL1","IMAGE_URL2","IMAGE_URL3"]
    },
}

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if the message is in the dictionary
    if message.content in image_responses:
        response = image_responses[message.content]
        text_response = response["text"]
        image_url = random.choice(response["images"])  # Select a random image within the array

        embed = discord.Embed(description=text_response, color=discord.Color.blue())
        embed.set_image(url=image_url)

        await message.channel.send(embed=embed)


    await bot.process_commands(message)

bot.run('DISCORD_TOKEN')