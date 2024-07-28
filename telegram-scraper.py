import os
import pandas as pd
from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("TG_API_ID")
api_hash = os.getenv("TG_API_HASH")

app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Za public grupu:
TARGET_GROUP = "zrtvekovidvakcinachat"  # Uneti grupni username (deo posle @)

# Za privatnu grupu:
# TARGET_GROUP = "joinchat/abcdef1234567890" # Zameniti sa grupnim invite linkom (deo posle'joinchat/')

# Definisati zeljeni broj poruka
NUM_MESSAGES = 100

messages = []

with app:
    for message in app.get_chat_history(TARGET_GROUP, limit=NUM_MESSAGES):
        
        msg_id = message.id if message.id else "N/A"
        msg_date = message.date if message.date else "N/A"
        msg_username = message.from_user.username if message.from_user else "N/A"
        msg_text = message.text if message.text else "N/A"
        
        messages.append([msg_id, msg_date, msg_username, msg_text])

# Čuvanje skrejpovanih poruka u .csv fajlu
df = pd.DataFrame(messages, columns=["Message ID", "Date", "Username", "Message"])
df.to_csv("messages.csv", index=False)

print("Messages have been scraped and saved to messages.csv")
