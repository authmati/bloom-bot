# Importar librerias necesarias:
import discord
from discord import app_commands
from discord.ext import commands
import random

# Iniciar cog de saludo:
class serverinfo(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} está listo.")

# Comando para que el bot te salude:
    @commands.hybrid_command(name="serverinfo", description="Muestra información sobre el servidor.")
    async def serverinfo(self, ctx):
        guild = ctx.guild

        embed = discord.Embed(
            title=f"{guild.name}",
            color=discord.Color(0xFFFFFF)
        )

# Embed de información del servidor:
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        embed.add_field(name="🆔 ID Servidor", value=guild.id, inline=True)
        embed.add_field(name="👑 Dueño", value=guild.owner.mention, inline=True)
        
        # Usamos el formato de timestamp de Discord
        timestamp = int(guild.created_at.timestamp())
        embed.add_field(name="📅 Fecha creación", value=f"<t:{timestamp}:d>", inline=True)
        embed.add_field(name="💬 Canales ({})".format(len(guild.channels)), 
                        value=f"**{len(guild.text_channels)}** texto | **{len(guild.voice_channels)}** voz", inline=True)
        embed.add_field(name="👥 Miembros", value=guild.member_count, inline=True)
        embed.add_field(name="🏜 Emojis", value=len(guild.emojis), inline=True)
        embed.add_field(name="🚀 Roles", value=len(guild.roles), inline=True)

        # Agregar el pie de página con la foto de perfil y el nombre del bot
        bot_avatar_url = self.client.user.avatar.url
        bot_name = self.client.user.name
        embed.set_footer(text=bot_name, icon_url=bot_avatar_url)
        
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(serverinfo(client))