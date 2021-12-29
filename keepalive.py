from apscheduler.schedulers.blocking import BlockingScheduler
import requests

SITE_URL = "https://github-profile-view.herokuapp.com/"

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def keepAliveCheck():
    requests.get(SITE_URL)
    
sched.start()