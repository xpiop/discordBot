import discord
import asyncio
import os
from datetime import datetime

client = discord.Client()
token = os.getenv('DISCORD_TOKEN')

async def send_scheduled_message():
    while True:
        now = datetime.now()
        # 매주 월요일 10시에 메시지를 보냅니다.
        if now.weekday() == 0 and now.hour == 3 and now.minute == 38:
            for guild in client.guilds:
                default_channel = guild.text_channels[0]  # 각 서버의 기본 채널을 첫 번째 채널로 설정합니다.
                await default_channel.send('스케줄된 메시지입니다!')
            # 1분 대기 후 다음 시간을 확인합니다.
            await asyncio.sleep(60)
        else:
            # 10초마다 현재 시간을 확인합니다.
            await asyncio.sleep(10)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(send_scheduled_message())

# 봇 실행
client.run(token)