# Importar librerias necesarias:
import discord
from discord import app_commands
from discord.ext import commands
import random

# Iniciar cog de saludo:
class hello(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} está listo.")

# Mensajes predeterminados al etiquetar al bot:
    @commands.Cog.listener()
    async def on_message(self, message):
        if self.client.user in message.mentions:
                    responses = [
            f"Robando una vez más 💵, {message.author.mention}!",
            f"Casha 🤬, {message.author.mention}!",
            f"Deja de molestarme, {message.author.mention}... 😒"
        ]
        response = random.choice(responses)
        await message.channel.send(response)
        await self.client.process_commands(message)

# Comando para que el bot te salude:
    @commands.hybrid_command(name="saludar", description="Saluda al usuario.")
    async def saludar(self, ctx):
         await ctx.send(f"Hola, {ctx.author.mention} pasa los cogollos!")

async def setup(client):
    await client.add_cog(hello(client))