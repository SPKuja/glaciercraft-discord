import discord
import requests
from bs4 import BeautifulSoup
import asyncio
import os
from mcstatus import JavaServer, BedrockServer

# Get Discord bot token, channel ID, and Minecraft server info from environment variables
TOKEN = os.getenv('TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
SERVER_IP = os.getenv('SERVER_IP')
SERVER_PORT = int(os.getenv('SERVER_PORT', 19132))  # Default Bedrock port is 19132

MINECRAFT_BEDROCK_URL = "https://www.minecraft.net/en-us/download/server/bedrock"
last_known_link = None

# Function to check if the Minecraft Bedrock server is online (using mcstatus 2.x)
def is_bedrock_server_online(host: str, port: int = 19132):
    try:
        server = BedrockServer(host, port)
        status = server.status()
        return f"The server is online with {status.players_online} players."
    except Exception as e:
        return f"The server is offline or unreachable. Error: {e}"

# Non-async function that performs blocking I/O for checking updates
def check_minecraft_update_blocking():
    global last_known_link
    try:
        response = requests.get(MINECRAFT_BEDROCK_URL)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            download_link = soup.find('a', text="Download Ubuntu server").get('href')

            if download_link != last_known_link:
                last_known_link = download_link
                return last_known_link
    except Exception as e:
        print(f"Error checking update: {e}")
        return None

class MyBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        channel = self.get_channel(CHANNEL_ID)
        loop = asyncio.get_running_loop()

        while True:
            # Check for Minecraft server updates
            update = await loop.run_in_executor(None, check_minecraft_update_blocking)
            if update:
                await channel.send(f'New Minecraft Bedrock Server update: {update}')

            # Check if the Minecraft server is online
            server_status = await loop.run_in_executor(None, is_bedrock_server_online, SERVER_IP, SERVER_PORT)
            await channel.send(server_status)
            
            await asyncio.sleep(3600)  # Check every hour

client = MyBot(intents=discord.Intents.default())
client.run(TOKEN)
