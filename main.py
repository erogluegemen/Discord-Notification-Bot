from dotenv import load_dotenv
import os
import discord
from discord.utils import get
from discord.ext.commands import dm_only
from discord.ext import commands

load_dotenv()

intents= discord.Intents.all()
client = discord.Client(intents=intents)

word_list = ["IEEE", "CS"] # Bildirim gelmesi istenilen kelimeler.


@client.event
async def on_ready():
    print("Bot hazır!")

@commands.dm_only()
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content in word_list:
        id = client.get_user() # Discord ID buraya gelecek. (int formatında)
        await id.send(content=f"Hey! {message.author} adlı kullanıcı {message.content} hakkında bir şeyler dedi.")

token = os.getenv("TOKEN")
client.run(token)
