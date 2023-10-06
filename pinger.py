import socket
import logger
from pythonping import ping


def generateAllPossibleIPsInNetwork(baseAddress):
    possibleAddress = []
    subnet = ".".join(baseAddress.split(".")[:-1])
    for i in range(1, 255):
        possibleAddress.append(subnet+"."+str(i))
    return possibleAddress


def getMyDeviceIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def pingDevice(address):
    ping(address, count=10, timeout=0)


def pingDevicesInNetwork():
    logger.LOGGER_OBJ.debug("started pinging")
    hostMachineIP = str(getMyDeviceIP())
    addresses = generateAllPossibleIPsInNetwork(hostMachineIP)
    for i in addresses:
        pingDevice(i)
