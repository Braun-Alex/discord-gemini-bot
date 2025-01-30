import os
from vertexai.generative_models import ChatSession
import discord
from discord import Interaction
from discord.ui import Modal, InputText
from inference.process_prompt import process_prompt

class FileUploadModal(Modal):
    def __init__(self, user_id: int, chat_session: ChatSession):
        super().__init__(title="🗂️ Enter your prompt filepath")
        self.user_id = user_id
        self.chat_session = chat_session
        self.prompt_filepath = InputText(label="⬆️ Prompt .txt filepath", style=discord.InputTextStyle.singleline, required=True)
        self.add_item(self.prompt_filepath)

    async def callback(self, interaction: Interaction):
        filepath = self.prompt_filepath.value

        if not os.path.exists(filepath):
            await interaction.response.send_message(f"❌ File \"{filepath}\" not found!", ephemeral=True)
            return

        if not filepath.endswith(".txt"):
            await interaction.response.send_message("❌ Only .txt files are allowed!", ephemeral=True)
            return

        with open(filepath, "r", encoding="utf-8") as file:
            prompt = file.read()

        await interaction.response.defer()
        await process_prompt(interaction, prompt, self.chat_session)