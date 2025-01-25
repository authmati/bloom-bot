import logging
import json
import os  

def load_config(file_path="config.json"):
    try:
        with open(file_path, "r") as config_file:
            config = json.load(config_file)
            return config
    except FileNotFoundError:
        logging.error("El archivo '{file_path}' no fue encontrado.")
        exit()

def get_token(config):
    token = config.get("TOKEN")
    if not token or not isinstance(token, str):
        logging.error(f"El token proporcionado no es válido. Verifica el archivo 'config.json'.")
        exit()
    return token

# Carga los cogs del bot
async def load_cogs(bot):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")