from AnonXMusic import app
from os import environ
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest


# Extract environment variables or provide default values
chat_id_env = environ.get("CHAT_ID")
CHAT_ID = [int(app) for app in chat_id_env.split(",")] if chat_id_env else []

TEXT = environ.get("APPROVED_WELCOME_TEXT", "❅─────✧❅✦❅✧─────❅\n🥀𝖧𝖾𝗒 {mention}\n\n💫𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖨𝗇 𝖭𝖾𝗐 𝖦𝗋𝗈𝗎𝗉💫\n\n➻ {title}\n\n💞𝖭𝗈𝗐 𝖬𝖺𝗄𝖾 𝖭𝖾𝗐 𝖥𝗋𝗂𝖾𝗇𝖽𝗌 𝖠𝗇𝖽 𝖲𝗍𝖺𝗒 𝖠𝗅𝗐𝖺𝗒𝗌 𝖮𝗇𝗅𝗂𝗇𝖾 𝖨𝗇 𝖳𝗁𝗂𝗌 𝖦𝗋𝗈𝗎𝗉🥳\n❅─────✧❅✦❅✧─────❅**")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Define an event handler for chat join requests
@app.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: app, message: ChatJoinRequest):
    chat = message.chat  # Chat
    user = message.from_user  # User
    print(f"{user.first_name} Joined 🤝")  # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))
