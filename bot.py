from telethon import TelegramClient, events

# Your Telegram API credentials
api_id = 26402318
api_hash = '4a1bf7c39bb4e82f2b71b10c9b35fb05'

# Name must match your session file (without .session extension)
client = TelegramClient('affiliate_session', api_id, api_hash)

# Start client using saved session
client.start()
print("✅ Bot started successfully! Listening for messages...")

# ====== Example Forwarding Logic ======
# Replace with your actual group/channel IDs
SOURCE_GROUP = 'https://t.me/loot_deals_offers_coupon'  # Public group link
DEST_CHANNEL = 'https://t.me/IndiasBB'  # Your Telegram channel

@client.on(events.NewMessage(chats=SOURCE_GROUP))
async def handler(event):
    # Forward message to your bot first (optional if you want to rewrite links)
    # Or just forward directly
    await client.send_message(DEST_CHANNEL, event.message)

# Keep bot running
client.run_until_disconnected()
