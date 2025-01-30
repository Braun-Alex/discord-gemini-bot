import os
from dotenv import load_dotenv
from discord.ext import commands
from views.prompt_view import PromptView

load_dotenv()

DISCORD_MESSAGE_LENGTH_LIMIT = 2000
MODEL_SELECT_TIMEOUT = 60 * 5
CHAT_TIMEOUT_SECONDS = 60 * 60 * 24

VERTEX_PROJECT_ID = os.getenv("GOOGLE_CLOUD_API_KEY")

class PromptCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="prompt", description="Generate text with Gemini AI")
    async def prompt_command(self, ctx: commands.Context):
        view = PromptView(ctx.author.id)
        await ctx.send("🌟 Select a Gemini model!", view=view)