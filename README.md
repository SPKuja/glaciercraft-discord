Save bot.py to the same directory as the Dockerfile and run:

<code>docker build -t glaciercraft .</code>

<code>docker run -d --name glaciercraft-discord &#92;
    -e TOKEN="YOUR_DISCORD_BOT_TOKEN" &#92;
    -e CHANNEL_ID="YOUR_CHANNEL_ID" &#92;
    -e SERVER_IP="your_server_ip_here" &#92;
    -e SERVER_PORT="19132" &#92;
    spkuja/glaciercraft</code>
