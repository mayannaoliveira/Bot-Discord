import discord
from discord import app_commands

class BotFocoTotal(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="$",
            intents=intents
        )
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"O {self.user} foi iniciado com sucesso!")

bot = BotFocoTotal()

@bot.tree.command(name="boas_vindas", description="Bot do servidor Foco Total")
async def olamundo(interaction: discord.Interaction):
    await interaction.response.send_message(f"olá {interaction.user.mention} que legal você por aqui!")

# Token do Discord não pode ser passado para outro usuário.
bot.run("TOKEN-DO-BOT")
