import logging
import discord
from discord.ext import commands
import json

class AutoBotRole(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"{self.__class__.__name__} está listo.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot:
            with open("cogs/json/autobotrole.json", "r") as f:
                auto_bot_role = json.load(f)

        bot_role = discord.utils.get(member.guild.roles, name=auto_bot_role[str(member.guild.id)])

        await member.add_roles(bot_role)

    @commands.hybrid_group(name="autobotrole", description="Este comando te permite poner un rol de inicio.")
    @commands.has_permissions(administrator=True)
    async def parent_autorole(self, ctx: commands.Context, role= None):
        if role is None:
            embed_message = discord.Embed(description="Por favor, proporciona un rol.", color=discord.Color.gold())
            await ctx.send(embed= embed_message)
            return

    @parent_autorole.command(name="set", description="Este comando te permite poner un rol de inicio.")
    @commands.has_permissions(administrator=True)
    async def sub_autorole(self, ctx: commands.Context, role: discord.Role):
        with open("cogs/json/autobotrole.json", "r") as f:
            auto_role = json.load(f)

        auto_role[str(ctx.guild.id)] = str(role.name)

        with open("cogs/json/autobotrole.json", "w") as f:
            json.dump(auto_role, f, indent=4)
        
        embed_set = discord.Embed(description=f"Prefijo actualizado a {role.mention}", color=discord.Color.gold())
        await ctx.send(embed= embed_set)

async def setup(client):
    await client.add_cog(AutoBotRole(client))
