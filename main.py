import telegram
from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_apscheduler import APScheduler
import os
import time
import atexit
import requests
import logging

#BOT CONFIG
REQUEST_RATE_LIMIT = "20 per 15 minute"
NOTIFIER_CHAT_ID = int(os.environ.get("USER_CHAT_ID"))
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SITE_URL = os.environ.get("SITE_URL")

#init bot service
bot = telegram.Bot(token=BOT_TOKEN)
logging.info(bot.get_me()['first_name'] + "is Started")

#init server
app = Flask(__name__)  

#rate limiter 
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["500 per day", "50 per hour"]
)

#hook
@app.route('/github', methods=['GET'])
@limiter.limit(REQUEST_RATE_LIMIT)
def gitHubHook():
    if(request.method == 'GET'):
        bot.send_message(NOTIFIER_CHAT_ID, "Someone viewed your github profile")
    return ""

#set cron job to keep dyno alive
def KeepAlivePing(*args):
    try:
        requests.get(SITE_URL)
        logging.info("KeppAlive ping ---" + bot.get_me()['first_name'])
        bot.send_message(NOTIFIER_CHAT_ID,bot.get_me()['first_name'] + "Service is down")
    except:
        bot.send_message(NOTIFIER_CHAT_ID,bot.get_me()['first_name'] + "Service is down")

if __name__ == '__main__':
    
    #schedule a cron job
    scheduler = APScheduler()
    scheduler.add_job(id = 'Keep Alive Ping', func = KeepAlivePing, trigger = 'interval', seconds = 60)
    scheduler.start()
    
    #start server 
    app.run(debug = False)