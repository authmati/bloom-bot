# Importar librerias necesarias:
import discord
from discord import app_commands
from discord.ext import commands

# Iniciar cog de ping:
class ping(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} está listo.")

# Comando para ver el ping del bot:
    @app_commands.command(name="ping", description="Este comando muestra la latencia del bot.")
    async def ping(self, interaction: discord.Interaction):
        latencia = round(self.client.latency * 1000)
        await interaction.response.send_message(f"La latencía del bot es **{latencia}** ms.", ephemeral=True)

async def setup(client):
    await client.add_cog(ping(client))