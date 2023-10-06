import storage
import time
import constants


def isOnline(old_time):
    if time.time() - old_time > constants.ONLINE_LIMIT:
        return False
    else:
        return True


def Print_global_storage():
    global_storage = storage.Global_storage_get_all()
    for i, j in global_storage.items():
        for k in j:
            print(k, end="\t")
        if isOnline(j[-2]):
            print("online")
        else:
            print("offline")
