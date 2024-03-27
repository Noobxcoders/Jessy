from telegraph import upload_file
from pyrogram import filters
from AnonXMusic import app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["tgm" , "link"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("💫𝖬𝖺𝗄𝖾 𝖠 𝖫𝗂𝗇𝗄🌟")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f' 🍒𝖸𝗈𝗎𝗋 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗉𝗁 🍒 {url}')
