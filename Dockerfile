# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install dependencies for requests, discord.py, BeautifulSoup, and mcstatus
RUN pip install --no-cache-dir discord.py beautifulsoup4 requests mcstatus

# Copy the bot script into the container
COPY bot.py .

# Define environment variables
ENV TOKEN="YOUR_DISCORD_BOT_TOKEN"
ENV CHANNEL_ID="YOUR_CHANNEL_ID"
ENV SERVER_IP="your_server_ip_here"
ENV SERVER_PORT=19132

# Run the bot script when the container launches
CMD ["python", "bot.py"]
