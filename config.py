import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "24482734")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "5ccf6a58166cc047a7eba01c5dbc930c") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7092299196:AAFDrftAM2ZuQCXg6fmXZGgSTHZSJ2QJCGA") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1001840046152') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://bharathkalladi38:refaj5BccvHhG2Zl@cluster0.wvsv51o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","metadata")

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "1790775725")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001891110437')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/dbf07ce0f70a6cea7b7d7.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
