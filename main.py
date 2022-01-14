import discord
from discord.ext import commands

bot = commands.Bot('f!')

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(922665986774151168)
    for channel in guild.channels():
        if channel.id == 929114720038965269:
            break
    a = await channel.send(embed=discord.Embed(title=f"Hello {member.mention}",description="You can verify yourself by say `verify`!"))
    res = await bot.wait_for('message',timeout=30,check=lambda m: m.author == member and m.channel == channel)
    if res.content.lower() == "verify":
        await res.delete()
        await a.edit(embed=discord.Embed(title="Nice! React the message to finish the verification!"))
        await a.add_reaction("✔")
        res = await bot.wait_for('reaction',timeout=30,check=lambda m: m.author == member and m.channel == channel)
        if str(res.emoji) == "✔":
            await member.send(f"You verified! Congratulations! Now enjoy your stay at {member.guild.name}!")