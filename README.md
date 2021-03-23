# Discord Bot

![Discord Logo](https://droplr.com/wp-content/uploads/2020/06/iconfinder_discord_2308078-512x400.png)

## Architecture

**Discord Guild** < --- > **Bot/Replit.com** < --- > **HTTP API Endpoint**

From Discord we send commands to our bot running on Replit.com. It can make API calls for us and send the answer back to Discord.

## The Setup

This was done ahead of time:

1. Create bot in Discord's Developer Portal, https://discord.com/developers.
![Build-A-Bot](https://files.realpython.com/media/discord-bot-add-bot.4735c88ff16b.png)
1. A secret token will be provide for us to use in our code. This is how the bot knows we are allowed to talk to it.
1. We need to set what permissions we want the bot to have (but not Admin permissions!).
![](https://files.realpython.com/media/discord-bot-scopes.ee333b7a5987.png)
1. We need to add our bot to our guild.

(If you are curious about the specifics, see the reference links at the bottom.)

## Prep for Programing the Bot

### discord.py
A 3rd party library that implements the Discord API in Python and adds helpers for bot creation. (Yay, open source tools making things easier for us!)

```py
import discord
```

* Documentation: https://discordpy.readthedocs.io
* Source Code: https://github.com/Rapptz/discord.py

### discord.py Bot Helper

`discord.py` has an extention to create bot commands, so we do not have to write the code to talk to the Discord API to do this ourselves.

```py
from discord.ext.commands import Bot

bot = Bot("!")
```

## Computer Sciency Stuff

### Coroutine

As far as we are concerned, it will act like an infinate loop, so we can interact with the bot.

☝️🧐 Remeber that loops are a form of "flow control" in a program? Well, so are coroutines.

> multitasking, by allowing execution to be suspended and resumed

-- https://en.wikipedia.org/wiki/Coroutine

> A coroutine is a function that must be invoked with **await** or yield from. When Python encounters an await it stops the function’s execution at that point and works on other things until it comes back to that point and finishes off its work. This allows for your program to be doing multiple things at the same time without using threads or complicated multiprocessing.

-- https://discordpy.readthedocs.io/en/latest/faq.html#coroutines

```py
bot.run(<API TOKEN>)
```

### Python Decorators

TL;DR: A wrapper to put our function inside of another function. This helps to simplify the code we have to write.

(The big brain term is "closure".)

```py
@bot.command()
async def speak(ctx):
  await ctx.send(":robot: Beep boop. Boop beep.")
```

### Wait, what is this `ctx`?

`bot.command()` is making our funcion a "callback". It is how our function can hook into the coroutine. `ctx` provides this ability. In `discord.py` it stands for the `Context`.

The `Context` contains:

> Essentially all the information you need to know how the command was executed.

-- https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#invocation-context

## Other References

Learn how to create a Discord Bot:

* https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
* https://realpython.com/how-to-make-a-discord-bot-python/