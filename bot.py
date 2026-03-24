# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport

from pyrogram import Client, idle
from config import Config
from web_server import web_server
from aiohttp import web
import os
import asyncio

# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
app = Client(
    "CodeVoultX-imgtolinkbot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
if __name__ == "__main__":
    print(r"""
   ______          __      _  __ ____          __       
  / ____/____  ___/ /___  | |/ // __ ) ____  / /_ _____
 / /   / __ \/ __  / __ \ |   // __  |/ __ \/ __// ___/
/ /___/ /_/ / /_/ /  __/ /   |/ /_/ // /_/ / /_ (__  ) 
\____/\____/\__,_/\___/ /_/|_/_____/ \____/\__/ /____/  
                                                                            
      BOT WORKING PROPERLY....
    """)
    print("Starting Bot...")
    
    # Start Web Server for Render/Heroku
    port = int(os.environ.get("PORT", 8888))
    
    # We need to run standard asyncio loop for both
    loop = asyncio.get_event_loop()
    
    try:
        app.start()
        print("Bot Started! Send /start to verify.")
        
        # Web Server Startup
        web_app = loop.run_until_complete(web_server())
        runner = web.AppRunner(web_app)
        loop.run_until_complete(runner.setup())
        site = web.TCPSite(runner, "0.0.0.0", port)
        loop.run_until_complete(site.start())
        print(f"Web Server started on port {port}")
        
        idle()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        app.stop()
# CodeVoultX_Bots
# Don't Remove Credit
# Telegram Channel @CodeVoultX_Bots
#Supoort group @codesXSupport
