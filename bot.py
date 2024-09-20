import discord

from bot_logic import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hi'):
        await message.channel.send("Helloo!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$random_password'):
        await message.channel.send(f'Password: {gen_pass(8)}')
    elif message.content.startswith('$flip_coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$random_emo'):
        await message.channel.send(gen_emodji())
    else:
        await message.channel.send(message.content)

client.run("MTI4NDMwMjE5MzE0NjQ2MjIxifqQVxOw0M4cc8SAq_AC9rtbpQ")
