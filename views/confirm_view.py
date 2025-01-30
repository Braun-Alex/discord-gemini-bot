from vertexai.generative_models import ChatSession
import discord
from discord.ui import View
from modals.file_upload_modal import FileUploadModal
from modals.prompt_modal import PromptModal

CHAT_TIMEOUT_SECONDS = 60 * 60 * 24

class ConfirmView(View):
    def __init__(self, user_id: int, chat_session: ChatSession):
        super().__init__(timeout=CHAT_TIMEOUT_SECONDS)
        self.user_id = user_id
        self.chat_session = chat_session

    @discord.ui.button(label="📘 Long", style=discord.ButtonStyle.green)
    async def long(self, _, interaction):
        if interaction.user.id == self.user_id:
            modal = FileUploadModal(self.user_id, self.chat_session)
            await interaction.response.send_modal(modal)

    @discord.ui.button(label="📝 Short", style=discord.ButtonStyle.red)
    async def short(self, _, interaction):
        if interaction.user.id == self.user_id:
            modal = PromptModal(self.user_id, self.chat_session)
            await interaction.response.send_modal(modal)