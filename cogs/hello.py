# Importar librerias necesarias:
import logging
from discord.ext import commands
import random

# Iniciar cog de saludo:
class Hello(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"{self.__class__.__name__} está listo.")

    # Mensajes predeterminados al etiquetar al bot:
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if self.client.user in message.mentions:

            RESPONSES = [
                "Robando una vez más 💵, {mention}!",
                "Casha 🤬, {mention}!",
                "Deja de molestarme, {mention}... 😒",
                "Que pasa pibe!",
            ]

            response = random.choice(RESPONSES).format(mention=message.author.mention)
            await message.channel.send(response)
            await self.client.process_commands(message)

    # Comando para que el bot te salude:
    @commands.hybrid_command(name="saludar", description="Saluda al usuario.")
    async def saludar(self, ctx):
        await ctx.send(f"Hola, {ctx.author.mention} pasa los cogollos!")


async def setup(client):
    await client.add_cog(Hello(client))
