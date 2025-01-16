# Importar librerias necesarias:
import discord
from discord import app_commands
from discord.ext import commands
import os

# Iniciar cog de reinicio de cogs:
class manager(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} está listo.")

# Comando para reiniciar los cogs del bot:
    @app_commands.command(name="reset", description="Reinicia los comandos.")
    @commands.has_permissions(administrator = True)
    async def reset(self, interaction: discord.Interaction):
         await interaction.response.send_message(f"Recargando cogs...", ephemeral= True)

         for filename in os.listdir("./cogs"):
             if filename.endswith(".py"):
                 try:
                     await self.client.unload_extension(f"cogs.{filename[:-3]}")
                     await self.client.load_extension(f"cogs.{filename[:-3]}")
                     print(f"Cog {filename} recargado.")
                 except Exception as e:
                     print(f"Error al recargar el cog {filename}: {e}")
                     await interaction.response.send_message(f"Error al recargar el cog {filename}: {e}", ephemeral= True)

         await interaction.followup.send("Cogs recargados con éxito.", ephemeral= True)

async def setup(client):
    await client.add_cog(manager(client))