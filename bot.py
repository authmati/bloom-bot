# Importar librerias necesarias:
from prefixes_loader import get_prefix
from cogs_loader import load_cogs
import discord
from discord.ext import commands
import json
import asyncio

# Leer el token desde config.json:
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    TOKEN = config["TOKEN"]

# Crea una instancia del bot
bot = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all())

# Mensajes de sincronización
@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} ({bot.user.id}) está listo y conectado.")
    await bot.tree.sync()
    print(f"Comandos de {bot.user.name} ({bot.user.id}) sincronizados.")

# Inicia el bot
async def main():
    async with bot:
        await load_cogs(bot)
        await bot.start(TOKEN)

asyncio.run(main())
