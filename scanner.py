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

    def __init__(self, ip, output_file):
        self.scanner = nmap.PortScanner()
        self.ip = ip
        self.output_file = output_file

    def start_scan(self):
        self.start_nmap()

    def start_nmap(self):
        self.scanner.scan(self.ip, "1-65535", "-A -T4 -oN ")
        try:
            print(bcolors.OKBLUE + "[+]" + bcolors.END + " IP " + str(self.ip) + " is " + self.scanner[self.ip].state())
        except:
            print(bcolors.FAIL + "[-]" + bcolors.END + " Seems that the host is not responding to ping, trying with -Pn option...")
            self.scanner.scan(self.ip, "1-65535", "-A -T4")

        print(bcolors.OKBLUE + "[+]" + bcolors.END + " These ports were open with these services \n")

        print("\t" + bcolors.OKBLUE + "Port" + bcolors.END + " \t\t" + bcolors.OKBLUE + "Service" + bcolors.END)

        for port in self.scanner[self.ip]["tcp"].keys():
            print("\t" + str(port) + " \t|\t" + self.scanner[self.ip]["tcp"][port]["name"])

    def map_scan(self):
        pass