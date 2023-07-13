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
    common_services = ["ssh", "ftp", "telnet", "smtp", "domain name system", "http", "https", "pop3", "imap", "imaps", "mysql", "http-proxy"]

    def __init__(self, ip, output_file):
        self.scanner = nmap.PortScanner()
        self.ip = ip
        self.output_file = output_file

    def start_scan(self):
        self.start_nmap()

    def start_nmap(self):
        self.scanner.scan(self.ip, "1-65535", "-A -T4 -oN " + self.output_file)
        try:
            print(bcolors.OKBLUE + "[+]" + bcolors.END + " IP " + str(self.ip) + " is " + self.scanner[self.ip].state())
        except:
            print(bcolors.FAIL + "[-]" + bcolors.END + " Seems that the host is not responding to ping, trying with -Pn option...")
            self.scanner.scan(self.ip, "1-65535", "-A -T4")

        print(bcolors.OKBLUE + "[+]" + bcolors.END + " These ports were open with these services \n")

        print("\t" + bcolors.OKBLUE + "Port" + bcolors.END + " \t\t" + bcolors.OKBLUE + "Service" + bcolors.END + " \t\t" + bcolors.OKBLUE + "Note" + bcolors.END)

        for port in self.scanner[self.ip]["tcp"].keys():
            
            # Notes
            Note = ""
            if (self.scanner[self.ip]["tcp"][port]["name"] in self.common_services):
                match (self.scanner[self.ip]["tcp"][port]["name"]):
                    case "ssh":
                        Note = "Need creds first"
                    case "ftp":
                        Note = "Most likely files on the system"
                    case "telnet":
                        Note = "Rare, but worse ssh"
                    case "smtp":
                        Note = "Mail"
                    case "domain name system":
                        Note = "DNS"
                    case "http":
                        Note = "Webserver"
                    case "https":
                        Note = "Webserver but encrypted traffic"
                    case "pop3":
                        Note = "Mail"
                    case "imap":
                        Note = "Mail"
                    case "imaps":
                        Note = "Mail"
                    case "mysql":
                        Note = "Database"
                    case "http-proxy":
                        Note = "Webserver"

            #tabspace
            if len(self.scanner[self.ip]["tcp"][port]["name"]) > 8:
                tabspace = " \t|\t"
            else:
                tabspace = " \t\t|\t"

            #print result
            print("\t" + str(port) + " \t|\t" + self.scanner[self.ip]["tcp"][port]["name"] + tabspace + Note)

    def map_scan(self):
        pass