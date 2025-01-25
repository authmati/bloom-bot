# Importar librerias necesarias:
import logging
import discord
from discord.ext import commands
import json
import os

# Iniciar cog de prefijos:
class Prefix(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"{self.__class__.__name__} está listo.")

# Poner prefijo predeterminado al unir el bot a un servidor:
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if not os.path.exists("prefixes.json"):
            with open("prefixes.json", "w") as f:
                json.dump({}, f)

        with open("prefixes.json", "r") as f:
            new_prefix = json.load(f)

        new_prefix[str(guild.id)] = "!"

        with open("prefixes.json", "w") as f:
            json.dump(new_prefix, f, indent=4)

# Eliminar prefijos al expulsar bot del servidor:
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        if not os.path.exists("prefixes.json"):
            return
        
        with open("prefixes.json", "r") as f:
            new_prefix = json.load(f)

        new_prefix.pop(str(guild.id), None)

        with open("prefixes.json", "w") as f:
            json.dump(new_prefix, f, indent=4)

# Comandos para cambiar el prefijo predeterminado del bot:
    @commands.hybrid_group(name="prefix", description="Este comando te permite cambiar el prefijo del bot.")
    async def parent_prefix(self, ctx: commands.Context, prefix= None):
        if prefix is None:
            embed_message = discord.Embed(description="Por favor, proporciona un nuevo prefijo.", color=discord.Color.gold())
            await ctx.send(embed= embed_message)
            return

    @parent_prefix.command(name="set", description="Este comando te permite cambiar el prefijo del bot.")
    async def sub_prefix(self, ctx: commands.Context, prefix):
        with open("prefixes.json", "r") as f:
            new_prefix = json.load(f)

        new_prefix[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
            json.dump(new_prefix, f, indent=4)
        
        embed_set = discord.Embed(description=f"Prefijo actualizado a {prefix}", color=discord.Color.gold())
        await ctx.send(embed= embed_set)
        
async def setup(client):
    await client.add_cog(Prefix(client))