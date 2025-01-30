import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from cogs.prompt import PromptCog

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_API_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

if __name__ == "__main__":
    bot.add_cog(PromptCog(bot))
    bot.run(TOKEN)