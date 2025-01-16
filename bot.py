# Importar librerias necesarias:
import discord
from discord import app_commands
from discord.ext import commands
import json
import os
import asyncio

# Leer el token desde config.json:
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    TOKEN = config["TOKEN"]

# Cargar prefijos personalizados de servidores:
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        new_prefix = json.load(f)

    return new_prefix[str(message.guild.id)]

# Crea una instancia del bot
bot = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all())

# Mensajes de sincronización
@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} ({bot.user.id}) está listo y conectado.")
    await bot.tree.sync()
    print(f"Comandos de {bot.user.name} ({bot.user.id}) sincronizados.")

# Carga los cogs del bot
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

# Inicia el bot
async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)

asyncio.run(main())
