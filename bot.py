import os
from telethon import TelegramClient, events

# ==== Read from Railway environment variables ====
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

# ==== Telegram details ====
source_group = "https://t.me/loot_deals_offers_coupon"
my_bot_username = "@ekconverter20bot"
my_channel = "https://t.me/IndiasBB"

client = TelegramClient("affiliate_session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    try:
        original_message = event.raw_text
        
        # Send to your affiliate converter bot
        await client.send_message(my_bot_username, original_message)
        
        # Wait for bot's reply
        async for response in client.iter_messages(my_bot_username, limit=1):
            affiliate_message = response.raw_text
            break
        
        # Send to your Telegram channel
        await client.send_message(my_channel, affiliate_message)
        
        print("? Message processed and sent!")
    
    except Exception as e:
        print("? Error:", e)

print("?? Bot started in Railway cloud...")
client.start()
client.run_until_disconnected()
