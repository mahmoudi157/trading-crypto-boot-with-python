import configparser
import telepot
import time 
from database import Status
import datetime as dt
import place_orders as po
import requests



config = configparser.ConfigParser()
config.read("config.ini")

bot_token = str(config["Telegram"]["bot_token"])
my_chat_id = str(config["Telegram"]["my_chat_id"])

def time_now():
    time = dt.datetime.now()
    time = time.strftime("%H:%M:%S    //   %d-%m-%Y") #10:42:30   //   01-03-2021
    return time

bot = telepot.Bot(bot_token)

def send_msg(text):
    url = "https://api.telegram.org/bot"+bot_token+"/sendMessage?chat_id="+my_chat_id+"&parse_mode=Markdown&text="
    request = url+text
    response = requests.get(request)
    return response.json()
    
def handle(msg):
    user_name = msg["from"]["first_name"]
    content_type, chat_typt, chat_id = telepot.glance(msg)

    if content_type == "text":
        my_command = msg["text"]
        if "/start" in my_command:
            bot.sendMessage(chat_id,
            "Welcome "+user_name+" in your AutoTrafing bot! \n /help give your more information about your bot.")
        elif "/help" == my_command:
            bot.sendMessage(chat_id,
            "Available command is :\n ** [ON, OFF] - Control the bot \n ** [Balance] - Get your free USDT balance")
        elif "ON" == my_command.upper():
            Status.save_status(collection = "Status", status = my_command.upper(), time = time_now())
            bot.sendMessage(chat_id, "System activated now.", parse_mode = "Markdown")
            with open("log.txt", "a") as log_file:
                log_file.write("System is activted at : "+time_now()+"/n")

        elif "OFF" == my_command.upper():
            Status.save_status(collection = "Status", status = my_command.upper(), time = time_now())
            bot.sendMessage(chat_id, "System   `disactivated` now.", parse_mode = "Markdown")
            with open("log.txt", "a") as log_file:
                log_file.write("System is disactivted at : "+time_now()+"/n")            

        elif "BALANCE" in my_command.upper():
            free_balance = po.get_usdt_balance()
            bot.sendMessage(chat_id,
            "Your free USDT balance is : `"+str(free_balance)+"USDT`", parse_mode = "Markdown" )
        else:
            bot.sendMessage(chat_id,
            "Unknown command, use /help to get more information.")

bot.message_loop(handle)

#while True:
    #time.sleep(20)
