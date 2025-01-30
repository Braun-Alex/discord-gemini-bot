import os
import vertexai
from vertexai.generative_models import GenerativeModel
import discord
from discord import SelectOption
from discord.ui import View
from dotenv import load_dotenv
from views.confirm_view import ConfirmView

load_dotenv()

MODEL_SELECT_TIMEOUT = 60 * 5

VERTEX_PROJECT_ID = os.getenv("VERTEX_PROJECT_ID")

class PromptView(View):
    def __init__(self, user_id: int):
        super().__init__(timeout=MODEL_SELECT_TIMEOUT)
        self.user_id = user_id
        self.selected_model = None
        self.chat_session = None

    @discord.ui.select(
        options=[
            SelectOption(label="🚀 Gemini 1.5 Flash", value="gemini-1.5-flash"),
            SelectOption(label="✨ Gemini 1.5 Pro", value="gemini-1.5-pro"),
            SelectOption(label="🌌 Gemini-Exp-1206", value="gemini-exp-1206")
        ]
    )
    async def callback(self, select, interaction):
        if interaction.user.id == self.user_id:
            self.selected_model = select.values[0]
            vertexai.init(project=VERTEX_PROJECT_ID, location="us-central1")
            model = GenerativeModel(self.selected_model)
            self.chat_session = model.start_chat()
            await interaction.response.send_message(f"✅ You selected {select.values[0]}. Chat session started!", ephemeral=True)

    @discord.ui.button(label="🤖 Prompt", style=discord.ButtonStyle.green)
    async def send(self, _, interaction):
        if interaction.user.id == self.user_id:
            if self.selected_model:
                view = ConfirmView(self.user_id, self.chat_session)
                await interaction.response.send_message("📄 It is chat prompt view. Send your prompt here. Message is long if it exceeds 4000 characters, short otherwise.", view=view, ephemeral=True)
            else:
                await interaction.response.send_message("⚠️ Please select a Gemini model first.", ephemeral=True)

    @discord.ui.button(label="🚪 Leave", style=discord.ButtonStyle.danger)
    async def leave(self, _, interaction):
        if interaction.user.id == self.user_id:
            await interaction.message.delete()