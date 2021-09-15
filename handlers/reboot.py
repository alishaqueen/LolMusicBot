from pyrogram import Client, filters
from handlers import check_heroku

@Client.on_message(filters.command('restart') & filters.user(1323020756))
@check_heroku
async def gib_restart(client, message, hap):
    msg_ = await message.reply_text("Restarting....Wait 1 minute")
    hap.restart()
