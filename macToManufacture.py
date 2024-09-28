import constants
import storage

manufacture_file = constants.MANUFACTURE_PATH


def Parse_manufacture_file():
    with open(manufacture_file, 'r',  encoding='utf-8') as file:
        for line in file:
            arr = (line.strip()).split("\t")
            mac_address = arr[0]
            manufacture_name = arr[1][:8]

            storage.MANUFACTURE[mac_address] = manufacture_name
