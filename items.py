import os
import json

def logo_print():
  print("""      
              .-'''-.        .-'''-.                          
             '   _    \     '   _    \                        
            /   /` '.   \  /   /` '.   \                       
     .--./).   |     \  ' .   |     \  '   _.._.-.          .- 
     /.''\\ |   '      |  '|   '      |  '.' .._|\ \        / / 
   | |  | |\    \     / / \    \     / / | '     \ \      / /  
    \`-' /  `.   ` ..' /   `.   ` ..' /__| |__    \ \    / /   
    /("'`      '-...-'`       '-...-'`|__   __|    \ \  / /    
    \ '---.                              | |        \ `  /     
     /'""'.\                             | |         \  /      
    ||     ||                            | |         / /       
     \'. __//                             | |     |`-' /        
     `'---'                              |_|      '..'         """)

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def menu():

  no_option_chosen = True

  while(no_option_chosen):
    clear()
    logo_print()

    with open("info.json", "r") as outfile:
      json_obj = json.load(outfile)
      print("A. Target IP: " + json_obj["target_ip"])
      print("B. Target SSH Password: " + json_obj["target_ssh_pass"])
      print("C. Your IP: " + json_obj["your_ip"])
      print("D. (opt) Output scanner file path: " + json_obj["out_file"])

      print("1. Scan target")
      print("\t- nmap \n\t- dirbuster")
      print("2. Transfer file source -> target")
      print("3. Transfer file target -> source")
      print("4. Transfer winpeas or linpeas to target")

      print("\nOr type \"exit\"")

    inp = input("> ")

    match inp:
      case "A":
        target_ip = input("Target IP: ")
        update_json("target_ip", target_ip)
      case "B":
        target_ssh_pass = input("Target SSH Pass: ")
        update_json("target_ssh_pass", target_ssh_pass)
      case "C":
        your_ip = input("Your IP: ")
        update_json("your_ip", your_ip)
      case "D":
        output_file = input("Output scanner path: ")
        update_json("out_file", output_file)
      case "1":
        no_option_chosen = False
      case "2":
        no_option_chosen = False
      case "3":
        no_option_chosen = False
      case "4":
        no_option_chosen = False
      case "exit":
        exit()

def update_json(key, value):
  with open("info.json", "r") as outfile:
    json_obj = json.load(outfile)
  json_obj[str(key)] = value
  with open("info.json", "w") as outfile:
    json.dump(json_obj, outfile)