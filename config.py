import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("APP_ID", ""))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    
    # Database
    MONGO_URL = os.getenv("MONGO_URL", "")
    
    # Admin
    ADMIN_STR = os.getenv("ADMIN_ID", "")
    ADMINS = [int(x) for x in ADMIN_STR.split()] if ADMIN_STR else []
    
    # Channel
    FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "") # username or ID
    
    # UI
    START_PICS = [
        "https://ibb.co/XZZhqDs0",
        "https://ibb.co/3XCzkZL",
        "https://ibb.co/7NgxrXwz",
        "https://ibb.co/23Tmfs7T",
        "https://ibb.co/sp1f1s7C",
        "https://ibb.co/svCR2VfB"
    ]
    START_PIC = os.getenv("START_PIC", "") # Manual override via env if needed
    
    # Log Channel
    LOG_CHANNEL = os.getenv("LOG_CHANNEL", "") # Channel ID (e.g. -100xxxx)

# Telegram Configuration

