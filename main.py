import colorama
import os
import ctypes
import time
import requests

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    
option1 = colorama.Fore.RESET + '[' + colorama.Fore.LIGHTMAGENTA_EX + "1" + colorama.Fore.RESET + "]"
option2 = colorama.Fore.RESET + '[' + colorama.Fore.LIGHTMAGENTA_EX + "2" + colorama.Fore.RESET + "]"
option3 = colorama.Fore.RESET + '[' + colorama.Fore.LIGHTMAGENTA_EX + "3" + colorama.Fore.RESET + "]"
choice_enter = (colorama.Fore.RESET + "[" + colorama.Fore.LIGHTMAGENTA_EX + ">" + colorama.Fore.RESET + "]" + "Enter Choice: ")
lc = (colorama.Fore.RESET + "[" + colorama.Fore.LIGHTMAGENTA_EX + ">" + colorama.Fore.RESET + "]")


def set_window_title(title):
    try:
        # Get the handle to the console window
        console_handle = ctypes.windll.kernel32.GetConsoleWindow()

        # Set the new window title
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    except Exception as e:
        print(f'Error occurred while setting window title: {str(e)}')

def send_discord_message(webhook_url, message):
    payload = {
        "content": message
    }

    response = requests.post(webhook_url, json=payload)

    if response.status_code == 204:
        print(colorama.Fore.GREEN + "[+] Message sent successfully")
    else:
        print(f"Failed to send message. Error: {response.text}")

def webhook_spammer():
    clear()
    webhook_url = input(lc + "Enter your Discord webhook URL: ")
    message = input(lc + "Enter the message you want to send: ")

    # Prompt the user to select the frequency option
    frequency_option = input(lc + "Select the sending frequency option (fast / normal / slow): ")

    # Set the sending frequency based on the selected option
    if frequency_option == "fast":
        frequency = 0.01  # Send every 0.01 seconds (faster)
        clear()
    elif frequency_option == "normal":
        frequency = 1  # Send every 1 second
        clear()
    elif frequency_option == "slow":
        clear()
        frequency = 5  # Send every 5 seconds
        clear()
    else:
        print("Invalid frequency option. Using default frequency (fast).")
        frequency = 0.01

    # Continuously send the message with the specified frequency
    while True:
        send_discord_message(webhook_url, message)
        time.sleep(frequency)

def delete_webhook():
    clear()
    webhook_url = input(lc + "Enter your Discord webhook URL: ")
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print(colorama.Fore.GREEN + "[+] Webhook successfully deleted.")
        input(colorama.Fore.YELLOW + "Press any key to go back...")
        handle_input()
    else:
        print("Failed to delete webhook.")
        input(colorama.Fore.YELLOW + "Press any key to go back...")
        handle_input()
        
def send_message():
    clear()
    webhook_url = input(lc + "Enter your Discord webhook URL: ")
    message = input(lc + "Enter the message you want to send: ")
    send_discord_message(webhook_url, message)
    input(colorama.Fore.YELLOW + "Press any key to go back...")
    handle_input()
        
def handle_input():
    set_window_title("Nexus Webhook Tool discord.gg/nexus-tools")
    clear()
    print(colorama.Fore.LIGHTMAGENTA_EX + '''
                    ███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                    ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                    ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗█████╗██║   ██║   ██║██║   ██║██║     ███████╗
                    ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
                    ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                    ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                discord.gg/nexus-tools
    ''')
    print("                                                " + option1 + "Spam Webhook")
    print("                                                " + option2 + "Delete Webhook")
    print("                                                " + option3 + "Send Single Message")
    choice = int(input(choice_enter))
    if choice == 1:
        webhook_spammer()
    if choice == 2:
        delete_webhook()
    if choice == 3:
        send_message()

handle_input()

