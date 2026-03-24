# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from database import db
import asyncio

# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
@Client.on_message(filters.command("users") & filters.user(Config.ADMINS))
async def stats(client: Client, message: Message):
    if not db:
        return await message.reply_text("**⚠️ Dᴀᴛᴀʙᴀꜱᴇ Nᴏᴛ Cᴏɴɴᴇᴄᴛᴇᴅ!**")
    
    count = await db.total_users_count()
    await message.reply_text(f"**📊 Tᴏᴛᴀʟ Uꜱᴇʀꜱ:** `{count}`")

# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
@Client.on_message(filters.command("broadcast") & filters.user(Config.ADMINS))
async def broadcast(client: Client, message: Message):
    if not db:
        return await message.reply_text("**⚠️ Dᴀᴛᴀʙᴀꜱᴇ Nᴏᴛ Cᴏɴɴᴇᴄᴛᴇᴅ!**")
    
    if not message.reply_to_message:
        return await message.reply_text("**⚠️ Pʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ.**")

    users_list = await db.get_all_users()
    users = await users_list.to_list(length=None) # Convert cursor to list for length
    total_users = len(users)
    msg = message.reply_to_message
    
    sent = 0
    failed = 0
    status_msg = await message.reply_text("**⏳ Bʀᴏᴀᴅᴄᴀꜱᴛ Sᴛᴀʀᴛᴇᴅ...**")
    
    import time
    start_time = time.time()

    async def update_progress(current, total):
        percent = (current / total) * 100
        completed = "▓" * int(percent // 10)
        remaining = "░" * (10 - int(percent // 10))
        text = (
            f"**⏳ Bʀᴏᴀᴅᴄᴀꜱᴛɪɴɢ...**\n\n"
            f"**📊 Pʀᴏɢʀᴇꜱꜱ:** `{completed}{remaining}` {percent:.1f}%\n"
            f"**✅ Sᴇɴᴛ:** `{sent}`\n"
            f"**❌ Fᴀɪʟᴇᴅ:** `{failed}`\n"
            f"**👥 Tᴏᴛᴀʟ:** `{total}`"
        )
        try:
            await status_msg.edit_text(text)
        except:
            pass

    for i, user in enumerate(users):
        try:
            await msg.copy(chat_id=user['id'])
            sent += 1
        except Exception:
            failed += 1
        
        # Update progress every 20 users or 5 seconds to avoid flood
        if i % 20 == 0:
            await update_progress(i + 1, total_users)
        
        await asyncio.sleep(0.1)

    await status_msg.edit_text(
        f"**✅ Bʀᴏᴀᴅᴄᴀꜱᴛ Cᴏᴍᴘʟᴇᴛᴇᴅ!**\n\n"
        f"**> Sᴇɴᴛ:** `{sent}`\n"
        f"**> Fᴀɪʟᴇᴅ:** `{failed}`\n"
        f"**> Tɪᴍᴇ:** `{int(time.time() - start_time)}s`"
    )

# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
@Client.on_message(filters.command("ban") & filters.user(Config.ADMINS))
async def ban(client: Client, message: Message):
    if not db:
        return
    if len(message.command) < 2:
        return await message.reply_text("**> Usᴇ:** `/ban user_id`")
    
    try:
        user_id = int(message.command[1])
        await db.ban_user(user_id)
        await message.reply_text(f"**🚫 Uꜱᴇʀ {user_id} Bᴀɴɴᴇᴅ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!**")
    except Exception as e:
        await message.reply_text(f"**⚠️ Eʀʀᴏʀ:** {e}")

# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
@Client.on_message(filters.command("unban") & filters.user(Config.ADMINS))
async def unban(client: Client, message: Message):
    if not db:
        return
    if len(message.command) < 2:
        return await message.reply_text("**> Usᴇ:** `/unban user_id`")
    
    try:
        user_id = int(message.command[1])
        await db.unban_user(user_id)
        await message.reply_text(f"**✅ Uꜱᴇʀ {user_id} Uɴʙᴀɴɴᴇᴅ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ!**")
    except Exception as e:
        await message.reply_text(f"**⚠️ Eʀʀᴏʀ:** {e}")
# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport