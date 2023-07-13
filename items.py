import os
import json
import scanner

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

def logo_print():
  logo = bcolors.END + u"""
  ⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠄⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠠⠌⠂⠂⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⠂⠂⢰⣾⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⣶⡇⠂⠂⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⠂⢀⣾⣼⠌⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠌⣷⣷⡀⠂⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⢠⣾⣫⢹⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⣏⣫⣷⡄⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⣴⣟⣫⢮⡏⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢹⡵⣽⣫⣦⡀⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⢀⣾⣫⣵⢯⡟⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢻⡽⣮⣫⣷⡄⠂⠂⠂⠂
  ⠂⠂⠂⠂⣾⣫⡮⣯⡿⡇⠂⠂⠂⠂⠂⣀⣀⣄⣀⣀⣀⣠⣀⣀⠂⠂⠂⠂⠂⢸⣟⡮⡮⣫⣷⠂⠂⠂⠂
  ⠂⠂⠂⢸⡮⣫⣟⣫⣿⡇⠂⠂⣠⠴⢿⣽⡶⣶⣾⣿⣷⣖⢶⣯⣟⠦⣄⠂⠂⢸⣟⣫⣻⣫⡮⡇⠂⠂⠂
  ⠂⠂⠂⣸⡮⣫⣺⣫⣧⣟⣄⣾⣷⡮⡽⢽⡾⣟⣿⣿⣿⣟⢷⡯⢿⡮⣾⣷⣠⣟⣼⡿⡮⣫⡮⣧⠂⠂⠂
  ⠂⠂⠂⣟⣫⣧⡮⣾⡮⣫⣟⣿⣟⢏⡾⢋⠕⣘⣿⣿⣿⡏⢀⡙⢷⡙⣟⣿⣟⣟⡮⣷⡮⣼⣫⣟⠂⠂⠂
  ⠂⠂⠂⢻⣫⣟⣫⣫⣟⣫⣟⣿⣫⣟⣫⣷⣫⣟⣿⣿⣿⣟⣫⣫⣫⣟⣾⣿⣟⣫⣫⣫⣫⣟⣫⡿⠂⠂⠂
  ⠌⡄⠂⢸⣫⣫⣫⡮⣫⣻⣟⣟⣿⣿⣫⠟⣽⣟⣿⣿⣿⣿⣯⠻⣫⣿⣿⣟⣟⣟⣫⡮⣫⣫⣫⡇⠂⢠⠌
  ⢸⠰⠂⠘⣟⣫⣫⣫⣫⣿⣿⣿⡿⠛⣡⣾⣟⣟⣫⣫⣫⣟⣟⣷⣌⠛⢿⣿⣿⣿⣫⣫⣫⣫⣟⠃⠂⠌⡇
  ⠈⣶⡧⡀⢻⣟⣟⣿⣿⠿⣛⡵⢪⣾⣫⣫⣿⣿⡮⣟⡮⣿⣟⣷⣫⣷⣕⢮⣛⠿⣿⣿⣟⣟⡟⢀⢼⣶⠁
  ⠂⠹⣫⣫⣦⣿⣟⣽⣷⣯⡮⡮⡿⢋⣾⣟⣟⣟⣫⣿⣫⣟⣟⣟⣷⡝⢿⡮⡮⡮⣾⣯⣟⣿⣴⣫⣫⠏⠂
  ⠂⠂⣟⣫⣫⣿⣿⣟⣟⡿⣟⠁⣠⣾⣫⣫⣫⣫⣟⣿⣟⣫⣫⣫⣫⣷⣄⠈⣻⢿⣟⣟⣿⣿⣟⣯⣟⠂⠂
  ⠂⠂⣟⣿⣟⣟⣿⣿⣟⢿⣫⣾⣫⡮⡮⣫⣫⣿⣿⣫⣿⣿⣫⣫⡮⡮⣫⣷⣝⡿⣟⣿⣿⣟⣟⣿⣟⠂⠂
  ⠂⠂⠸⣫⡧⣫⣿⣭⣷⣿⣟⣫⡮⡮⡮⣫⣫⣫⣫⣫⣫⣫⣫⣫⡮⡮⡮⣫⣟⣿⣾⣭⣿⣫⢾⣫⠏⠂⠂
  ⠂⠂⠂⢻⣿⣟⣿⣟⣿⡿⣫⣫⡮⡮⡮⡿⡮⣯⣟⣿⣟⣽⡮⢿⡮⡮⡮⣫⣟⢿⣿⣟⣿⣟⣿⡟⠂⠂⠂
  ⠂⠂⠂⢸⣟⣟⣟⣫⣟⣧⡈  """ + bcolors.RED + "O" + bcolors.END + """ ⠊⢫⣟⣟⡮⣟⣟⡝⠑ """ + bcolors.RED + "O" + bcolors.END + """  ⢁⣼⣫⣫⣟⣟⣟⣧⠂⠂⠂
  ⠂⠂⠂⢸⣫⣟⣟⡮⡮⣷⣗⠦⣀⣀⣀⣀⣾⣟⣫⡮⣫⣟⣷⣀⣀⣀⣀⠴⣾⣾⡮⡮⣟⣟⣫⡇⠂⠂⠂
  ⠂⠂⠂⠂⢿⣟⣟⣟⠿⡮⡮⡮⣶⡮⡮⡮⣷⣫⡮⡮⡮⣫⣾⣷⡮⡮⣶⡮⡮⡮⠿⣫⣟⣟⡿⠂⠂⠂⠂
  ⠂⠂⠂⠂⠘⢿⡿⢻⣷⣮⣽⣛⡮⣽⣫⠿⡿⢾⡮⡮⡮⡷⢿⠿⣫⣯⡮⣛⣯⣵⣾⡟⢿⡿⠃⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⢸⣸⣿⣟⣫⣫⣟⣟⣾⣻⡮⡮⡮⡮⡮⣟⣷⣟⣟⣫⣫⣟⣿⣧⡇⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⢸⣫⣫⠋⣟⣟⣟⣿⣟⣿⣟⣫⡮⣫⣟⣿⣟⣿⣟⣟⣟⠛⣫⣫⡇⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⢘⠝⠁⢀⣹⠛⣫⣫⣫⣫⣟⣟⣫⣟⣟⣫⣫⣫⣫⠛⣏⡠⠈⠻⡃⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⠈⠩⣻⡮⣟⣄⡽⢿⣫⣶⣶⣮⡮⣵⣶⣶⣫⡿⢫⣠⣟⡮⣟⠍⠁⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⠂⠂⠱⡮⡾⣟⣟⣽⠈⡉⢉⢍⣫⡩⡉⢉⠁⣯⣿⣟⢧⡮⠎⠂⠂⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠘⣻⣟⣶⠘⡰⣿⣿⣿⣿⣿⣿⣿⢆⠣⣶⣻⣟⠃⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠸⣫⣿⣇⠌⢹⣨⣷⣫⣾⣅⡏⠌⣸⣿⣫⠇⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢻⣟⡻⣷⡿⣟⡮⡮⡮⣻⢿⣷⢟⣿⡟⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⢸⣟⣟⣯⣾⡮⡮⡮⡮⡮⣷⣽⣟⣟⡇⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠈⠛⠿⣟⣫⡮⡮⡮⡮⡮⣫⣟⠿⠛⠁⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂
  ⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠈⠻⠿⠿⠛⠿⠿⠟⠁⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂⠂"""
  logo = logo.replace("⠂","-")
  print(logo)
  print(u"\n--- " + bcolors.RED + "Devils_Breath" + bcolors.END + " version 1.0 Enumeration Tool ---")
  print("--- Omajan 2023 ---\n")

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def menu():
  no_option_chosen = True

  # options menu
  while(no_option_chosen):
    clear()
    logo_print()

    with open("info.json", "r") as outfile:
      json_obj = json.load(outfile)
      print(u"A. Target IP: " + json_obj["target_ip"])
      print(u"B. (opt) Output scanner file path: " + json_obj["out_file"])

      print("\nType letter for options")
      print("Type start to \"start\" the scan")

      print("Or type \"exit\"")

    inp = input("> ")

    match inp:
      case "A":
        target_ip = input("Target IP: ")
        update_json("target_ip", target_ip)
      case "B":
        output_file = input("Output scanner path: ")
        update_json("out_file", output_file)
      
      case "Start":
        no_option_chosen = False
        start_scan()
      case "start":
        no_option_chosen = False
        start_scan()

      case "exit":
        exit()

def start_scan():
  with open("info.json", "r") as outfile:
    json_obj = json.load(outfile)
    scanner_obj = scanner.scanner(json_obj["target_ip"])
    scanner_obj.start_scan()

def update_json(key, value):
  with open("info.json", "r") as outfile:
    json_obj = json.load(outfile)
  json_obj[str(key)] = value
  with open("info.json", "w") as outfile:
    json.dump(json_obj, outfile)