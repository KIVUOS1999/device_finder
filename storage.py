GLOBAL_STORAGE = {}


def Global_storage_add_entry(mac_address, datas):
    if mac_address not in GLOBAL_STORAGE:
        GLOBAL_STORAGE[mac_address] = datas


def Global_storage_dhcp_update(mac_address, datas):
    if mac_address not in GLOBAL_STORAGE:
        GLOBAL_STORAGE[mac_address] = datas

    else:
        ip, vendor, hostname, _ = datas
        if GLOBAL_STORAGE[mac_address][0] != ip:
            GLOBAL_STORAGE[mac_address][0] = ip

        if GLOBAL_STORAGE[mac_address][1] == None:
            GLOBAL_STORAGE[mac_address][1] = vendor

        if GLOBAL_STORAGE[mac_address][2] == None:
            GLOBAL_STORAGE[mac_address][2] = hostname


def Global_storage_icmp_update(mac_address, ip):
    if mac_address not in GLOBAL_STORAGE:
        GLOBAL_STORAGE[mac_address] = [ip, None, None, mac_address]

    else:
        if GLOBAL_STORAGE[mac_address][0] != ip:
            GLOBAL_STORAGE[mac_address][0] = ip


def Global_storage_get(mac_address):
    if mac_address in GLOBAL_STORAGE:
        return GLOBAL_STORAGE[mac_address]

    else:
        return None


def Global_storage_get_all():
    return GLOBAL_STORAGE
