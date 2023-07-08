# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "27910418"))
API_HASH = os.environ.get("API_HASH", "bff187eb26c9ba202262fca02220c134")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5968901159:AAEBZ8zB8mV4_YZiVBs-HxRX2Js1d7eJ3vQ")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("Owner Id")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "hdxxxxxxxxxxxxd4")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://8874720143:8874720143@cluster0.eblnxtk.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6095870142")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001857321996")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "MonetLinksUpdate") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
