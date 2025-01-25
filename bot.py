# Importar librerias necesarias:
import logging
from prefixes_loader import get_prefix
from cogs_loader import load_cogs
import discord
from discord.ext import commands
import json
import asyncio

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Leer el token desde config.json:
with open("config.json", "r") as config_file:
    config = json.load(config_file)
    TOKEN = config["TOKEN"]

# Crea una instancia del bot
bot = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all())

# Mensajes de sincronización
@bot.event
async def on_ready():
    logging.info(f"Bot {bot.user.name} ({bot.user.id}) está listo y conectado.")
    try:
        await bot.tree.sync()
        logging.info(f"Comandos de {bot.user.name} ({bot.user.id}) sincronizados.")
    except Exception as e:
        logging.error(f"Error al sincronizar los comandos: {e}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Ese comando no existe")
    else:
        logging.error(f"Error en el comando '{ctx.command}': {error}")

        
# Inicia el bot
async def main():
    async with bot:
        await load_cogs(bot)
        await bot.start(TOKEN)


asyncio.run(main())
