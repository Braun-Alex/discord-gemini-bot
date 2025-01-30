import asyncio
from vertexai.generative_models import ChatSession
from discord import Interaction

DISCORD_MESSAGE_LENGTH_LIMIT = 2000

async def process_prompt(interaction: Interaction, prompt: str, chat_session: ChatSession):
    async with interaction.channel.typing():
        try:
            response = await asyncio.to_thread(chat_session.send_message, prompt)
            text = response.text

            while text:
                if len(text) <= DISCORD_MESSAGE_LENGTH_LIMIT:
                    await interaction.followup.send(text)
                    break

                split_index = text.rfind("\n", 0, DISCORD_MESSAGE_LENGTH_LIMIT)
                if split_index == -1:
                    split_index = DISCORD_MESSAGE_LENGTH_LIMIT

                chunk, text = text[:split_index], text[split_index:].lstrip()
                await interaction.followup.send(chunk)
        except Exception as error:
            await interaction.followup.send(f"❌ Error: \"{error}\"")