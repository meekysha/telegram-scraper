import os
import pandas as pd
from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("TG_API_ID")
api_hash = os.getenv("TG_API_HASH")

app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Definisati grupu i zeljeni broj poruka
TARGET_GROUP = "zrtvekovidvakcinachat"  # Zameniti sa imenom grupe (deo posle @)
NUM_MESSAGES = 100

messages = []

with app:
    for message in app.get_chat_history(TARGET_GROUP, limit=NUM_MESSAGES):
        msg_id = message.id if message.id else "N/A"
        msg_date = message.date if message.date else "N/A"
        msg_username = message.from_user.username if message.from_user else "N/A"
        msg_text = message.text if message.text else "N/A"

        reactions_count = 0
        if message.reactions:
            for reaction in message.reactions.reactions:
                reactions_count += reaction.count

        messages.append([msg_id, msg_date, msg_username, msg_text, reactions_count])

# Čuvanje u CSV fajlu
df = pd.DataFrame(messages, columns=["Message ID", "Date", "Username", "Message", "Reactions Count"])
df.to_csv("messages.csv", index=False)

print("Messages have been scraped and saved to messages.csv")
