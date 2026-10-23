# Bot Pokemon

### About This Bot

Hello! This is my Pokemon Discord bot.

This bot was made during the Python Level 3 class at **Kodland**. In this class, we learned about OOP (Object-Oriented Programming) and tried to use it in our bot.

With this bot, you can get a Pokemon, fight other players, and feed your Pokemon!

![Pikachu](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png)

### How to Try

1. Install the required libraries:

   ```bash
   pip install discord.py aiohttp
   ```

2. Create a `config.py` file and put your Discord bot token inside it.

   ```python
   token = "YOUR_BOT_TOKEN"
   ```

3. Run the bot:

   ```bash
   python main.py
   ```

4. Invite the bot to your Discord server and try the commands!

### Commands

| Command | What it does |
|---|---|
| `!go` | Get a Pokemon. |
| `!attack @user` | Attack another player's Pokemon. |
| `!feed` | Feed your Pokemon to restore its HP. |

### Pokemon Classes

- **Pokemon:** The normal Pokemon with random HP and power.
- **Wizard:** Has a chance to block an attack and can recover more HP when fed.
- **Fighter:** Can use a stronger attack and has a shorter feeding cooldown.

### Features

- Get random Pokemon.
- See your Pokemon's name, power, and HP.
- Fight other players.
- Feed your Pokemon.
- Get Pokemon images from the PokéAPI.

### Tools Used

- Python
- Discord.py
- Aiohttp
- [PokéAPI](https://pokeapi.co/)

### What I Learned

- How to use classes and objects.
- How to use inheritance.
- How to make a Discord bot.
- How to get data from an API.
