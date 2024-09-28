import socket
import storage
import db


def is_windows_specific_ports_open(ip):
    # windows specific port
    isOpen = False

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, 135))
    if result == 0:
        isOpen = True
    sock.close()

    return isOpen


def get_hostname(ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except:
        return None


def execute_misc():
    global_storage = storage.Global_storage_get_all()
    try:
        for i, j in global_storage.items():
            if j[1] == None:
                if is_windows_specific_ports_open(j[0]):
                    storage.GLOBAL_STORAGE[i][1] = "windows"
                    db.update_vendor(i, "windows")

            if j[2] == None:
                hostname = get_hostname(j[0])
                if hostname != None:
                    storage.GLOBAL_STORAGE[i][2] = hostname
                    db.update_hostname(i, hostname)
    except:
        pass
