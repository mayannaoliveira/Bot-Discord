import discord
from discord import app_commands
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

class BotFocoTotal(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="$",
            intents=intents
        )
        self.tree = app_commands.CommandTree(self)

    # Iniciar os comandos
    async def setup_hook(self):
        try:
            await self.tree.sync()
        except Exception as e:
            print(f"Error ao sincronizar os comandos: {e}")
        

    async def on_ready(self):
        print(f"O {self.user} foi iniciado com sucesso!")
        print(f'ID do bot: {bot.user.id}')
 
bot = BotFocoTotal()

# Boas vindas
@bot.tree.command(name="boas_vindas", description="Bot do servidor Foco Total")
async def olamundo(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá {interaction.user.mention}, que legal você por aqui!☕️")
    # Checando envio
    print("Boas vindas enviadas!")


# Lista de canais
@bot.tree.command(name="listar_canais", description="Lista todos os canais do servidor")
async def listar_canais(interaction: discord.Interaction):
    if not interaction.guild:
        await interaction.response.send_message("Este comando só pode ser usado em um servidor para listar os canais.")
        return
    
    # Obter todos os canais do servidor
    canais = interaction.guild.channels
    
    # Separar canais por texto e voz
    canais_texto = [c.mention for c in canais if isinstance(c, discord.TextChannel)]
    canais_voz = [c.mention for c in canais if isinstance(c, discord.VoiceChannel)]
    
    # Criar a mensagem de resposta
    embed = discord.Embed(
        title="📋 Canais do Servidor",
    )
    # Canais de texto
    if canais_texto:
        embed.add_field(name="💬 Canais de Texto", value="\n".join(canais_texto), inline=False)
    # Canais de voz
    if canais_voz:
        embed.add_field(name="🔊 Canais de Voz", value="\n".join(canais_voz), inline=False)
        # Checando envio
        print("Lista dos canais!")
    
    # Informações sobre o bot
    await interaction.response.send_message(embed=embed)

# Descrição do bot
@bot.tree.command(name="informacao", description="Lista a versão do servidor.")
async def info(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Informações do Bot",
        description="Bot feito em Python somente para estudo.",
    )
    
    # Autor e versão
    embed.add_field(name="Mayanna Oliveira", value="Criadora", inline=False)
    embed.add_field(name="Versão", value="1.0", inline=True)
    await interaction.response.send_message(embed=embed)
    # Checando envio
    print("Informações do bot!")

# Canal de Regras
@bot.tree.command(name="regras", description="Redireciona para o canal de regras")
@app_commands.guild_only()  # Só funciona em servidores
async def regras(interaction: discord.Interaction):
    """Envia um link para o canal de regras usando seu ID fixo."""
    # Busca o canal pelo ID (1369009659079561348)
    canal_regras = interaction.guild.get_channel(1369009659079561348)
    
    if not canal_regras:
        # Se o canal não existe (ID inválido ou sem permissão)
        await interaction.response.send_message(
            "❌ O canal de regras não foi encontrado! Contate um administrador.",
            ephemeral=True
        )
        return

    # Embed com menção de link
    embed = discord.Embed(
        title="📜 Leia as Regras do Servidor!",
        description=f"Por favor, acesse {canal_regras.mention} para ler as regras.\n"
                    f"[Clique aqui para ir direto ao canal.]({canal_regras.jump_url})"
    )
    embed.set_footer(text="Obrigado por colaborar! ❤️")

    # Responde ao usuário (visível apenas para ele)
    await interaction.response.send_message(embed=embed, ephemeral=True)


# Token do Discord não pode ser passado para outro usuário.
# Obtém o token via arquivo .env
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    raise ValueError("Token não encontrado! Verifique seu arquivo .env")
bot.run(TOKEN)

# Token para rodar o bot sem .env
# bot.run("TOKEN-DO-DISCORD")