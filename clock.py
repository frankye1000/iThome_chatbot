import os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('interval',minutes=1)  # 定期執行，每三分鐘執行一次
def cr():
    print('do crawler')  # 運行時打印出此行訊息
    os.system("python crawl_ithome.py")  # 開啟 crawl_ithome.py

sched.start()