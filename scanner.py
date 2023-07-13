import nmap
from items import bcolors

class scanner():
    scanner = None
    scanning_dict = {}

    def __init__(self, ip):
        self.scanner = nmap.PortScanner()
        self.ip = ip

    def start_scan(self):
        self.start_nmap()

    def start_nmap(self):
        scanning_dict = self.scanner.scan(self.ip, "1-65535", "-A -T4")
        print("[+] IP " + str(self.ip) + " is " + self.scanner[self.ip].state())

        if (self.scanner[self.ip].state() == "down"):
            print(bcolors.FAIL + "[-]" + bcolors.END + " Seems that the host is not responding to ping, trying with -Pn option...")
            scanning_dict = self.scanner.scan(self.ip, "1-65535", "-A -T4")

        print(scanning_dict)

    def map_scan(self):
        pass