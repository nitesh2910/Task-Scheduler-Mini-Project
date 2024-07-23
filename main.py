import schedule
import time


def print_message():
    print("Hey, Take A break and drink Water:", time.strftime("%H:%M:%S"))


# Schedule task to run every 5 seconds
schedule.every(5).seconds.do(print_message)

# Keep the program running to allow scheduled tasks to execute
while True:
    schedule.run_pending()
    time.sleep(1)