import logging
import discord
from discord.ext import commands
from googletrans import Translator, LANGUAGES

class Translation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"{self.__class__.__name__} está listo.")

    @commands.hybrid_command(name="traducir", description="Traduce texto a un idioma específico")
    async def translate(self, ctx, idioma, *, texto):

        """
        Comando para traducir texto a un idioma específico
        
        Parámetros:
        - idioma: Código del idioma de destino (ej. 'en', 'es', 'fr')
        - texto: Texto a traducir
        """
        
        try:
            # Verificar si el código de idioma es válido
            if idioma.lower() not in LANGUAGES:
                await ctx.send(f"⚠️ Código de idioma inválido. Usa códigos como 'en', 'es', 'fr'.")
                return

            # Detectar idioma de origen
            deteccion = self.translator.detect(texto)
            idioma_origen = deteccion.lang

            # Traducir el texto
            traduccion = self.translator.translate(texto, dest=idioma)

            # Crear un embed para mostrar la traducción
            embed = discord.Embed(title="🌐 Traducción", color=discord.Color.blue())
            embed.add_field(name=f"Idioma Original ({idioma_origen})", value=texto, inline=False)
            embed.add_field(name=f"Traducción a {idioma.upper()}", value=traduccion.text, inline=False)
            
            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"Ocurrió un error al traducir: {str(e)}")

    @commands.hybrid_command(name="idiomas", description="Muestra la lista de códigos de idiomas disponibles")
    async def list_languages(self, ctx):
        """
        Comando para mostrar los códigos de idiomas disponibles
        """
        # Crear una cadena con los códigos y nombres de idiomas
        idiomas = "\n".join([f"{codigo}: {nombre}" for codigo, nombre in LANGUAGES.items()])
        
        # Dividir el mensaje si es muy largo
        if len(idiomas) > 1900:
            idiomas = idiomas[:1900] + "..."

        await ctx.send(f"**Códigos de Idiomas Disponibles:**\n```\n{idiomas}\n```")

async def setup(bot):
    await bot.add_cog(Translation(bot))