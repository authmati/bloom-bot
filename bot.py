# Importar librerias necesarias:
import os
from prefixes_loader import get_prefix
from config_loader import load_cogs
from discord.ext import commands
from dotenv import load_dotenv
import logging
import discord
import asyncio

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cargar configuración y variables de entorno
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

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

if __name__ == "__main__":
    asyncio.run(main())
