<img width="150" height="150" align="left" style="float: left; margin: 0 10px 0 0;" alt="Vignette" src="https://github.com/dave-kramer/vignette/blob/main/previews/vignetteimg.png?size=1024"> 

# Vignette 

[![](https://img.shields.io/badge/discord.py-v1.7.3-blue.svg?logo=npm)](https://github.com/Rapptz/discord.py)
[![](https://img.shields.io/badge/discord_components-v2.1.2-blue.svg?logo=npm)](https://github.com/kiki7000/discord.py-components)
[![License](https://img.shields.io/github/license/dave-kramer/atlasboy)](https://github.com/dave-kramer/vignette/blob/main/LICENSE)

> Surf MyAnimeList inside Discord with ease.


## Table of Contents

- [About](#About)
- [Features](#features)
- [Installation](#installation)
- [License](#license)
- [Previews](#previews)

## About
Vignette is a bot to surf the MyAnimeList website in Discord with the use of the [Jikan](https://github.com/jikan-me/jikan-rest).  
Get information for anime, manga, users, characters, the industry & more, be able to receive airing schedule or tell Vignette which anime you want to
get notified about when it airs.  
Know instantly which characters are people's most favourite, get a [waifu](https://waifu.pics/), use [trace.moe](https://trace.moe/) to find out what anime your picture is from, get recommendations, trailers, quotes, watchlists and check what other MyAnimeList users are watching.  
Don't forget to play the anime or character guess game, receive points and battle other members.  

## Features
| Command | Arguments | Information | Example |
| ------------- | ------------- | ------------- | ------------- |
| .anime | `none` | Receive information about an anime.  | .anime Gabriel Dropout |
| .manga  | `none` | Receive information about a manga.  | .manga Berserk |
| .character  | `none` | Receive information about a characters.  | .character Levi |
| .person | `none` | Receive information about a person.  | .person Hanazawa Kana |
| .producer  | `none` | Receive information about a producer. | .producer Aniplex |
| .magazine  | `none` | Receive information about a magazine | .magazine Ace Assault |
| .user  | `none` | Receive information about a MyAnimeList user including buttons for about, clubs, favorites, friends, history, recommendations, reviews, statistics, userupdates. | .user davekramer |
| .random  | `anime, manga, characters, people, reviews` | Get something random! | .random characters |
| .top  | `anime, manga, characters, people, reviews` | Get the top straight from MAL. | .top anime |
| .season  | `summer, fall, winter, spring, later` + `year` | Receive the seasonal anime. | .season fall 2022 |
| .notify  | `none` | Add an anime and receive notification when it airs. | .notify Shingeki no Kyojin: The Final Season Part 2 |
| .airlist  | `none` | Get the current airlist you've put together. | .airlist |
| .delete  | `none` | Remove an airing anime from your airlist. | .delete Shingeki no Kyojin: The Final Season Part 2 |
| .waifu  | `neko, shinobu, megumin, bully, cuddle, cry, hug, awoo, kiss, lick, pat, smug, bonk, yeet, blush, smile, wave, highfive, handhold, nom, bite, glomp, slap, kill, kick, happy, wink, poke, dance, cringe` | Get a random waifu. | .waifu |
| .quote  | `none` | Get a random anime/manga quote. | .quote |
| .watch  | `recent, popular` | Receive the recent or popular top 25 to watch. | .watch popular |
| .recommendations  | `anime, manga` | Get a random recommendation from MAL. | .recommendation anime |
| .schedule  | `today, monday, tuesday, wednesday, thursday, friday, saturday, sunday` | Get the schedule for the week. | .schedule today |
| .guess  | `anime, char` | Guess the Character game. | .guess char |
| .leaderboards  | `none` | Get the current leaderboards. | .leaderboards |
| .trace  | `none` | Search for the anime by image. | .trace link |
| .trailer  | `recent, popular` | Receive the recent or popular trailers. | .trailer recent |
| .trivia  | `recent, popular` | Play a small anime trivia game. | .trivia easy 5 |
| .commands  | `none, waifu` | Receive the all the commands or just for waifu | .commands |


## Installation
### Creating Vignette in Discord
1. Go to the [Discord Developer Portal](https://discord.com/developers/docs).
2. Login to your Discord account.
3. Click on New Application.
4. Enter the name of your bot and press create.
5. Click on the Bot tab on the left menu bar.
6. Click on Add Bot & Click to Reveal Token, save this token for a moment somewhere.
7. Press OAuth2 on the left menu bar.
8. Check the checkbox and press Copy.
9. You can paste this link in your browser and add this bot to any discord server you want.

### Local Setup
10. Install [Python](https://www.python.org/).
11. [Download](https://github.com/dave-kramer/vignette/archive/refs/heads/main.zip) or [clone](https://github.com/dave-kramer/vignette.git) the bot.
12. Unpack ZIP & create an .env file including DISCORD_TOKEN="TOKENHERE" and add your BOT TOKEN from step 6 inside the "" & save.
13. Save this .env file
14. Go to your discord server and create or select a channel that you want the guess game in - right click the channel and click Copy ID.
    - If you dont have the Copy ID option, enable Developer Mode in Discord settings -> Advanced -> Developer Mode.
15. Add this Channel ID to guess.py inside the cog folder on line 19 replace CHANNELID with the Channel ID & save.
16. Repeat step 14 for airing anime, this is the spot where u want anime airing notifications, this can be the same channel or another.
17. Add this Channel ID to bot.py inside the main folder on line 84 replace SETCHANNELID with the Channel ID & save.
18. Open cmd, locate the folder through cmd and run the bot by typing python bot.py
    - If you're new on how to run Python scripts use google.
19. Vignette is now running.

## License
[MIT License](https://github.com/dave-kramer/vignette/blob/main/README.md)

## Previews
![animecommandimg](https://github.com/dave-kramer/vignette/blob/main/previews/animecommandimg.png)
![usercommandimg](https://github.com/dave-kramer/vignette/blob/main/previews/usercommandimg.png)
![notifycommandimg](https://github.com/dave-kramer/vignette/blob/main/previews/notifycommandimg.png)
![airingcommandimg](https://github.com/dave-kramer/vignette/blob/main/previews/airingcommandimg.png)
![guesscharcommandimg](https://github.com/dave-kramer/vignette/blob/main/previews/guesscharcommandimg.png)
![guessanimecommandimg](https://github.com/dave-kramer/vignette/blob/main/previews/guessanimecommandimg.png)
![topcommandimg](https://github.com/dave-kramer/vignette/blob/main/previews/topcommandimg.png)
