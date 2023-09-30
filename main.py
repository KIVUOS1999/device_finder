import listiner
import displayer
import threading
import pinger
import time
import constants


def execute_display_global():
    while True:
        print("====================== printing global storage =====================\n")
        displayer.Print_global_storage()
        print("\n\n\n")

        time.sleep(constants.TIME_INTERVAL)


def execute_listiner():
    listiner.start_all_time_listiner()


def execute_pingger():
    while True:
        pinger.pingDevicesInNetwork()
        time.sleep(constants.PING_TIME_INTERVAL)


# starting display events
threadDisplay = threading.Thread(target=execute_display_global)
threadDisplay.start()

# starting listiner
thread = threading.Thread(target=execute_listiner)
thread.start()

# starting pingger
threadPingger = threading.Thread(target=execute_pingger)
threadPingger.start()
