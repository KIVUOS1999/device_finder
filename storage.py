import time
import db

GLOBAL_STORAGE = {}
MANUFACTURE = {}

# update this whenever we addd any entry
# datas = [ip, vendor, hostname, mac_to_class, time, mac]


def Global_storage_add_entry(mac_address, datas):
    if mac_address not in GLOBAL_STORAGE:
        GLOBAL_STORAGE[mac_address] = datas


def Global_storage_dhcp_update(mac_address, datas):
    if mac_address not in GLOBAL_STORAGE:
        GLOBAL_STORAGE[mac_address] = datas
        if db.get_from_db(mac_address) == None:
            db.insert_to_db(mac_address, datas[2], datas[1])
        else:
            _, hostname, vendor = db.get_from_db(mac_address)
            if hostname != datas[2] and datas[1] != None:
                db.update_hostname(mac_address, datas[2])
            if vendor != datas[1] and datas[1] != None:
                db.update_vendor(mac_address, datas[1])

    else:
        present = True
        ip, vendor, hostname, _, _, _ = datas
        if db.get_from_db(mac_address) == None:
            present = False
            db.insert_to_db(mac_address, hostname, vendor)

        if GLOBAL_STORAGE[mac_address][0] != ip:
            GLOBAL_STORAGE[mac_address][0] = ip

        if GLOBAL_STORAGE[mac_address][1] == None:
            GLOBAL_STORAGE[mac_address][1] = vendor
            if present:
                db.update_vendor(mac_address, vendor)

        if GLOBAL_STORAGE[mac_address][2] == None:
            GLOBAL_STORAGE[mac_address][2] = hostname
            if present:
                db.update_hostname(mac_address, hostname)

        GLOBAL_STORAGE[mac_address][-2] = time.time()


def Global_storage_icmp_update(mac_address, ip):
    retrivedDataFromDB = db.get_from_db(mac_address)
    vendor = None
    hostname = None
    if retrivedDataFromDB != None:
        _, hostname, vendor = retrivedDataFromDB

    if mac_address not in GLOBAL_STORAGE:
        GLOBAL_STORAGE[mac_address] = [
            ip, vendor, hostname, GetManufacture(mac_address), time.time(), mac_address]

    else:
        if GLOBAL_STORAGE[mac_address][0] != ip:
            GLOBAL_STORAGE[mac_address][0] = ip

        GLOBAL_STORAGE[mac_address][-2] = time.time()


def Global_storage_get(mac_address):
    if mac_address in GLOBAL_STORAGE:
        return GLOBAL_STORAGE[mac_address]

    else:
        return None


def Global_storage_get_all():
    return GLOBAL_STORAGE


def GetManufacture(mac_address):
    stripped_mac = mac_address.upper()[:8]
    if stripped_mac in MANUFACTURE:
        return MANUFACTURE[stripped_mac]
