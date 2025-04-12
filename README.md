## A telegram bot that sends videos from [redgifs](redgifs.com)

### Installation:

**1- Install [requirements.txt](requirements.txt).**

**2- Replace the value of "BotToken" on the first line of [main.py](main.py) with your bot token.**

**3- If you want to: replace the value of "tags" on the second line of [main.py](main.py) with your preferences (It's a list of some tags I like by default)**
### The bot works like this:
**If the command "/video" is typed, the bot will send a random video of a random tag from the list of tags selected in the "tags" variable in the second line of [main.py](main.py).**

**If the command "/video something" is typed, the bot will send a random video of the tag "something" instead of a random one from the list of tags.**

### Usage examples:

> **User**: /video
>
> **Bot**: "Sends a video from one of the default tags"
>
> **User**: /video cosplay
>
> **Bot**: "Sends a cosplay video"
