import discord
from discord.ext import commands
import json

class autorole(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} está listo.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot:
            return
        
        with open("cogs/json/autorole.json", "r") as f:
            auto_role = json.load(f)

        join_role = discord.utils.get(member.guild.roles, name=auto_role[str(member.guild.id)])
        
        if join_role:
         await member.add_roles(join_role)

    @commands.hybrid_group(name="autorole", description="Este comando te permite poner un rol de inicio.")
    @commands.has_permissions(administrator=True)
    async def parent_autorole(self, ctx: commands.Context, role= None):
        if role is None:
            embed_message = discord.Embed(description="Por favor, proporciona un rol.", color=discord.Color.gold())
            await ctx.send(embed= embed_message)
            return

    @parent_autorole.command(name="set", description="Este comando te permite poner un rol de inicio.")
    @commands.has_permissions(administrator=True)
    async def sub_autorole(self, ctx: commands.Context, role: discord.Role):
        with open("cogs/json/autorole.json", "r") as f:
            auto_role = json.load(f)

        auto_role[str(ctx.guild.id)] = str(role.name)

        with open("cogs/json/autorole.json", "w") as f:
            json.dump(auto_role, f, indent=4)
        
        embed_set = discord.Embed(description=f"Prefijo actualizado a {role.mention}", color=discord.Color.gold())
        await ctx.send(embed= embed_set)
        
async def setup(client):
    await client.add_cog(autorole(client))