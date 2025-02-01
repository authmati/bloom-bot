import os
import json

# Cargar prefijos personalizados de servidores:
def get_prefix(message):
    with open("prefixes.json", "r") as f:
        new_prefix = json.load(f)

    return new_prefix[str(message.guild.id)]

# Carga los cogs del bot
async def load_cogs(bot):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")