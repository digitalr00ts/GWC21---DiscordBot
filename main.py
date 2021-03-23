"""Discord Bot for SMHS GWC 2021!!!"""
import os

from utils import logger

import requests
from discord.ext.commands import Bot

bot = Bot("$")


# Debug info so we know when our bot is ready to party.
@bot.listen("on_ready")
async def log_on_ready():
    logger.info(f"{bot.user} has connected to Discord!")


# Example 0
@bot.command()
async def speak(ctx):
    """Robot says hello."""
    await ctx.send(":robot: Beep boop. Boop beep.")


# Example 1
@bot.command()
async def echo(ctx, *args):
    """Repeat message."""
    # Hint: `args` is a tuple.
    await ctx.send(args)
    # await ctx.send(" ".join(args))


# Example 2
@bot.command()
async def add(ctx, *args):
    """Add numbers cuz math is hard."""
    # Hint: `args` are strings, they must be converted to integers to be summed.
    # What happens if we pass something that is not representative of a number?
    await ctx.send(f"{' + '.join(args)} = {sum(map(int, args))}")


# Example 3
@bot.command()
async def fizzbuzz(ctx, num):
    """Thowback to the FizzBuzz activity."""
    num = int(num)
    rtn = f"{'' if num % 3 else 'Fizz'}{'' if num % 5 else 'Buzz'}"
    await ctx.send(rtn if rtn else num)



# Example 4
@bot.command()
async def inspiration(ctx):
    """Inspirational quotes provided by https://zenquotes.io/."""
    response = requests.get("https://zenquotes.io/api/random")
    data = response.json()[0]
    await ctx.send(f"{data['q']} - {data['a']}")


# The bot's coroutine
bot.run(os.getenv("API_TOKEN"))
