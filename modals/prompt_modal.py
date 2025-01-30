from vertexai.generative_models import ChatSession
import discord
from discord import Interaction
from discord.ui import Modal, InputText
from inference.process_prompt import process_prompt

class PromptModal(Modal):
    def __init__(self, user_id: int, chat_session: ChatSession):
        super().__init__(title="📝 Enter your prompt")
        self.user_id = user_id
        self.chat_session = chat_session
        self.prompt = InputText(label="💬 Prompt", style=discord.InputTextStyle.long, required=True)
        self.add_item(self.prompt)

    async def callback(self, interaction: Interaction):
        await interaction.response.defer()
        prompt = self.prompt.value
        await process_prompt(interaction, prompt, self.chat_session)