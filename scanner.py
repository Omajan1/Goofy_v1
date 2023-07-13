import nmap

class bcolors:
    RED = '\u001b[31m'
    END = '\u001b[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
        try:
            print(bcolors.OKBLUE + "[+]" + bcolors.END + " IP " + str(self.ip) + " is " + self.scanner[self.ip].state())
        except:
            print(bcolors.FAIL + "[-]" + bcolors.END + " Seems that the host is not responding to ping, trying with -Pn option...")
            scanning_dict = self.scanner.scan(self.ip, "1-65535", "-A -T4")

        print(self.scanner[self.ip].all_protocols)
        print(self.scanner[self.ip]["tcp"].keys())

    def map_scan(self):
        pass