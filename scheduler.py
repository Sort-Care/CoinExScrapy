import os, sys
import time

def run_once():
    os.system("cd /Users/jihaoyu/Documents/GitHub/CoinExScrapy/; scrapy crawl coinex")
    print("Ran Once")



while True:
    print("Ended Sleeping, crawling some data...")
    run_once()
    print("Work done, going back to sleep....")

    wake_time = 3600
    while wake_time >= 0:
        m, s = divmod(wake_time, 60)
        time_left = str(m).zfill(2) + ":" + str(s).zfill(2);
        print "Time until waking up: ",
        print time_left + "\r",
        sys.stdout.flush()
        time.sleep(1)
        wake_time -= 1
