import json
import os

import telebot

CWD = os.getcwd()
DATA_PATH = os.path.join(CWD, "data/")

with open(os.path.join(DATA_PATH, "credentials.json"), "r", encoding="UTF-8") as file_data:
    credentials = json.load(file_data)

bot = telebot.TeleBot(credentials["bot_token"])

def send_water_warning():
    bot.send_message(credentials["chat_id"], "Neue Sensor-Meldung:\nSensor: Wasserstand am Pumpensumpf\nMeldestufe: ⚠️ Alarm ⚠️\nMeldung:\nDer Pumpensumpf droht überzulaufen!💧")

def send_offline_notify():
    bot.send_message(credentials["chat_id"], "⛔️ Der Bot wurde abgeschaltet ⛔️")
    
def send_online_notify():
    bot.send_message(credentials["chat_id"], "✅ Der Bot wurde gestartet ✅")	

send_online_notify()