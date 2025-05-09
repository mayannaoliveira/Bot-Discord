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

### Informações sobre o Bot
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

Estrutura dos arquivos no projeto:

```markdown
/projeto_focototal
│   .env
│   main.py
│   .gitignore
```

## Ocultar o Token
O Token do Discord não pode ser repassado então é recomendado o uso # python-dotenv.
1. Instalar o dot env na pasta do projeto `pip install python-dotenv`.
2. Criar um arquivo .env.
3. No arquivo .env inserir a variável para o token:

```env
# Token do Discord
DISCORD_TOKEN=INSERIR-TOKEN-DO-DISCORD
```

4. No arquivo .gitingnore inserir a variável para ocultar o token:

```gitignore 
# Arquivos de ambiente
.env
.env.*
```

5. Por fim o arquivo `main.py` ficará assim:

```python
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
```
6. Para rodar o bot use o comando `py -3 main.py`.