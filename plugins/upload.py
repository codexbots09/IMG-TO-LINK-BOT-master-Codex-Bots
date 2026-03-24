# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
import os
import requests
from config import Config
from database import db
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
def upload_to_catbox(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "userhash": ""}
    try:
        with open(file_path, "rb") as f:
            response = requests.post(url, data=data, files={"fileToUpload": f})
        
        if response.status_code == 200:
            return response.text.strip(), None
        else:
            return None, f"Catbox Error: {response.text}"
    except Exception as e:
        return None, f"Catbox Connection Error: {str(e)}"
# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
@Client.on_message(filters.photo | filters.animation | filters.video)
async def upload_media(client: Client, message: Message):
    if db and await db.is_banned(message.from_user.id):
        return await message.reply_text("**🚫 Yᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ꜰʀᴏᴍ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ!**")

    status_msg = await message.reply_text("Downloading media...", quote=True)
    
    try:
        # Download media
        file_path = await message.download()
        
        await status_msg.edit_text("Uploading to Catbox...")
        
        # Try Catbox first
        link, error = upload_to_catbox(file_path)
        
        if not link:
            await status_msg.edit_text(f"Catbox failed ({error}).")
        
        # Clean up downloaded file
        if os.path.exists(file_path):
            os.remove(file_path)
            
        if link:
            await status_msg.edit_text(
                text=(
                    f"**✅ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ Uᴘʟᴏᴀᴅᴇᴅ!**\n\n"
                    f"**> Lɪɴᴋ:** `{link}`\n"
                    f"**> Dɪʀᴇᴄᴛ Lɪɴᴋ:** [Cʟɪᴄᴋ Hᴇʀᴇ]({link})"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("🔗 Oᴘᴇɴ Lɪɴᴋ", url=link)]]
                ),
                disable_web_page_preview=True
            )
            if db:
                await db.add_upload(message.from_user.id, link)

            # Log to Channel
            if Config.LOG_CHANNEL:
                try:
                    log_text = (
                        f"**#Nᴇᴡ_Uᴘʟᴏᴀᴅ**\n\n"
                        f"**👤 Uꜱᴇʀ:** {message.from_user.mention} (`{message.from_user.id}`)\n"
                        f"**🔗 Lɪɴᴋ:** `{link}`\n"
                        f"**🕒 Tɪᴍᴇ:** {message.date}"
                    )
                    # Send message to log channel
                    await client.send_message(
                        chat_id=int(Config.LOG_CHANNEL),
                        text=log_text,
                        disable_web_page_preview=True
                    )
                except Exception as e:
                    print(f"Log Channel Error: {e}")

        else:
            await status_msg.edit_text(f"Failed to upload.\nReason: {error}")
            
    except Exception as e:
        await status_msg.edit_text(f"An error occurred: {str(e)}")
        # Clean up if exists
        try:
            if 'file_path' in locals() and os.path.exists(file_path):
                os.remove(file_path)
        except:
            pass
# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport