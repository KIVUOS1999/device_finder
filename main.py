import listiner
import displayer
import threading
import pinger
import time
import constants
import macToManufacture


def execute_display_global():
    while True:
        displayer.Print_global_storage()
        print("\n\n\n")

        time.sleep(constants.TIME_INTERVAL)


def execute_listiner():
    listiner.start_all_time_listiner()


def execute_pingger():
    while True:
        pinger.pingDevicesInNetwork()
        time.sleep(constants.PING_TIME_INTERVAL)


# fill the manufacture_data
macToManufacture.Parse_manufacture_file()

# starting display events
threadDisplay = threading.Thread(target=execute_display_global)
threadDisplay.start()

# starting listiner
thread = threading.Thread(target=execute_listiner)
thread.start()

# starting pingger
threadPingger = threading.Thread(target=execute_pingger)
threadPingger.start()
