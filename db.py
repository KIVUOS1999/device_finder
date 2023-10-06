import sqlite3


def start_db():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        mac TEXT PRIMARY KEY,
                        hostname TEXT,
                        vendorclass TEXT)''')

    conn.commit()
    return conn, cursor


def insert_to_db(mac, hostname, vendorclass):
    if hostname == None:
        hostname = ""

    if vendorclass == None:
        vendorclass = ""

    conn, cursor = start_db()
    cursor.execute("INSERT INTO users (mac, hostname, vendorclass) VALUES (?, ?, ?)",
                   (mac, hostname, vendorclass))
    conn.commit()
    conn.close()


def get_from_db(mac):
    conn, cursor = start_db()
    cursor.execute("select * from users  where mac = ?", (mac, ))
    data = cursor.fetchone()
    conn.close()
    return data


def update_hostname(mac, hostname):
    conn, cursor = start_db()
    cursor.execute(
        "update users set hostname = ? where mac = ?", (hostname, mac))

    conn.commit()
    conn.close()


def update_vendor(mac, vendor):
    conn, cursor = start_db()
    cursor.execute(
        "update users set vendorclass = ? where mac = ?", (vendor, mac))

    conn.commit()
    conn.close()


# insert_to_db("86:e4:df:0f:db:eg", "souvik-a2", "android-12")
# data = get_from_db("86:e4:df:0f:db:eg")
# update_vendor("86:e4:df:0f:db:eg", "apple")
update_hostname("86:e4:df:0f:db:eg", "souvik-a3")
# data = get_from_db("86:e4:df:0f:db:eg")
# print(data)
