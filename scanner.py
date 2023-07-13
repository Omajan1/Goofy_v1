import nmap

class scanner():
    scanner = None

    def __init__(self, ip):
        self.scanner = nmap.PortScanner()
        self.ip = ip

    def start_scan(self):
        self.start_nmap()

    def start_nmap(self):
        self.scanner.scan(self.ip, "1-65535", "-A -T4")
        print("[+] IP " + self.ip + " is " + self.scanner[self.ip].state)

    def map_scan(self):
        pass