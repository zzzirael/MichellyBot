from dotenv import load_dotenv
load_dotenv()
import discord
from discord.ext import commands
from discord import app_commands
import os
from mbot import get_topchal


api_key = os.environ.get('riot_api_key')
discord_key = os.environ.get('discord_key')


#reactions & normal message commands
class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=635283834467778580) #Syncs the dev server ID to discord
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')


        except Exception as e:
            print(f'Error syncing commands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('oi'):
            await message.channel.send(f'Olá {message.author} você tem um isqueiro?')
        

#slash commands



intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="?", intents=intents)

GUILD_ID = discord.Object(id=635283834467778580) #Adds the slash commands instantly to the server referred by the id

@client.tree.command(name='top10chall', description='Mostra qual o top 10 challengers brasil!', guild=GUILD_ID)
async def saytopchall(interaction: discord.Interaction):
    await interaction.response.send_message("Espera, tô pensando...")
    await interaction.followup.send(get_topchal(api_key=api_key, top=10))


client.run(discord_key)


    