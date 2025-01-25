# Importar librerias necesarias:
import logging
import discord
from discord import app_commands
from discord.ext import commands, tasks
from mcstatus import JavaServer

# Iniciar cog de estado del servidor de minecraft:
class MacStatus(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.server = JavaServer("onlyrats.ddns.net")  # Cambia esto por tu servidor de Minecraft
        self.update_status.start()

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"{self.__class__.__name__} está listo.")

# Comando para ver el estado del servidor de minecraft:
    @app_commands.command(name="mcstatus", description="Muestra el estado del servidor de Minecraft.")
    async def mcstatus(self, interaction: discord.Interaction):
            status = self.server.status()
            await interaction.response.send_message(f"El servidor tiene {status.players.online} jugadores conectados de un máximo de {status.players.max}. El ping es {status.latency} ms.", ephemeral= True)

# Estado de actividad del bot:
    @tasks.loop(minutes=3)
    async def update_status(self):
        try:
            status = self.server.status()
            activity = discord.Activity(
                name=f"{status.players.online}/{status.players.max} Jugadores",
                type=discord.ActivityType.watching
            )
            await self.client.change_presence(activity=activity)
        except Exception as e:
            logging.error(f"Error al actualizar el estado del servidor: {e}")

    @update_status.before_loop
    async def before_update_status(self):
        await self.client.wait_until_ready()

async def setup(client):
    await client.add_cog(MacStatus(client))
