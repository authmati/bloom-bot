# Importar librerias necesarias:
import discord
from discord import app_commands
from discord.ext import commands

# Iniciar cog de información de usuario:
class userinfo(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} está listo.")

# Comando para acceder a la información de un usuario en especifico:
    @commands.hybrid_command(name="user", description="Este comando muestra la información del usuario.")
    async def user(self, ctx, usuario: discord.Member = None):
        if usuario is None:
            usuario = ctx.author
        elif usuario is not None:
            usuario = usuario

# Mención de roles de usuario:
        roles = [role.mention for role in usuario.roles[1:]]  # Excluye el rol @everyone

# Embed con información del usuario:
        info_embed = discord.Embed(title=f"{usuario.display_name}", description="**Información del usuario**", color=discord.Color(0xFFFFFF))
        info_embed.set_thumbnail(url=usuario.avatar)
        info_embed.add_field(name="ID:", value=usuario.id, inline=False)
        info_embed.add_field(name="Usuario:", value=usuario.name, inline=False)
        info_embed.add_field(name="Nombre:", value=usuario.display_name, inline=False)
        info_embed.add_field(name="Nick:", value=usuario.nick if usuario.nick is not None else "No tiene" , inline=False)
        info_embed.add_field(name="Color:", value=str(usuario.color).upper(), inline=False)
        info_embed.add_field(name="Roles", value=", ".join(roles) if roles else "No tiene roles", inline=False)

# Agregar el pie de página con la foto de perfil y el nombre del bot
        bot_avatar_url = self.client.user.avatar.url
        bot_name = self.client.user.name
        info_embed.set_footer(text=bot_name, icon_url=bot_avatar_url)


        await ctx.send(embed = info_embed)

async def setup(client):
    await client.add_cog(userinfo(client))