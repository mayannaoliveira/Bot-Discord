![image](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white) ![image](https://img.shields.io/badge/Discord-5865F2.svg?style=for-the-badge&logo=Discord&logoColor=white)

# Criando um Bot para Discord com Python
Para criar um bot para Discord usando Python, você precisará seguir estes passos:

## Pré-requisitos
1. Python instalado (versão 3.6 ou superior)    
2. Conta no Discord
3. Biblioteca `discord.py`

## Passo a Passo
### 1. Instalar a biblioteca discord.py
1. Crie uma pasta e depois abra ela no VS Code.
2. Crie o arquivo main.py onde serão adicionados os códigos em Python.
3. Instale a biblioteca do Discord  pelo comando`pip install discord.py`.

### 2. Criar um bot no Portal de Desenvolvedores do Discord
1. Acesse [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique em "New Application"
3. Dê um nome ao seu bot e clique em "Create"
4. Na aba "Bot", clique em "Add Bot"
5. Copie o TOKEN do bot porém esse token não pode ser compartilhado, pode ser adicionado uma `.env` para guardas o token.

### 3. Código básico do bot
Crie um arquivo `bot.py` com o seguinte conteúdo:
```python
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
```
### 4. Executar o bot
Para executar o bot basta utilizar o comando `py -3 main.py` no terminal, caso não esteja funcionando cheque ser o bot foi adicionado ao servidor ou se ele foi atualizado, para atualizar o Discord use o comando CTRL+R.

### 5. Convidar o bot para seu servidor
1. No Portal de Desenvolvedores, vá para "OAuth2" > "URL Generator"
2. Selecione as permissões que seu bot precisa
3. Selecione "bot" nos escopos    
4. Copie a URL gerada e acesse no navegador
5. Escolha o servidor para adicionar o bot

## Funcionalidades adicionais
Diversas funcionalidade podem ser adicionadas ao bot, segue o exemplo de algumas delas.

### Manipulação de eventos
```python
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f'Bem-vindo {member.mention} ao servidor!')
```

### Comandos com permissões
```python
@bot.command()
@commands.has_permissions(administrator=True)
async def limpar(ctx, quantidade: int):
    await ctx.channel.purge(limit=quantidade + 1)
    await ctx.send(f'{quantidade} mensagens foram apagadas!', delete_after=5)
```

### Embeds
```python
@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Informações do Bot",
        description="Um bot simples feito com Python",
        color=discord.Color.blue()
    )
    embed.add_field(name="Criador", value="SeuNome", inline=False)
    embed.add_field(name="Versão", value="1.0", inline=True)
    await ctx.send(embed=embed)
```
