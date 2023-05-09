import os
import shutil
import time
from colorama import init, Fore, Back, Style
import datetime
import json
try:
   from rgbprint import gradient_print, Color, rgbprint
   from pypresence import Presence
except:
    os.system("pip install rgbprint")
    os.system("pip install pypresence")
    


with open("config.json") as file:
    fix = json.load(file)

os.system('cls')
init()
if fix['theme']['name'] == "UGCLooter_theme":
    def loading_screen():
        # Loading Bar made by Aspect#6889
        console_width = shutil.get_terminal_size().columns
        console_height = shutil.get_terminal_size().lines
        loading_text = "[ → Loading... ← ]"
        loading_box_width = console_width // 2
        loading_box_height = console_height // 4
        loading_bar_length = loading_box_width - 3
        loading_bar_empty = " " + "░" * loading_bar_length + " "
        # ░ / █ / ○ / ●
        loading_bar_full = " " + "█" * loading_bar_length + " "
        loading_bar_display = loading_bar_empty
        loading_bar_center = (loading_box_width - len(loading_bar_display)) // 2
        loading_text_center = (loading_box_width - len(loading_text)) // 2

        loading_box_display = [Fore.RED + " " * loading_box_width + Style.RESET_ALL] * loading_box_height
        loading_box_display[loading_box_height // 2 - 1] = Fore.LIGHTBLACK_EX + "╭" + "─" * (loading_box_width - 2) + "╮" + Style.RESET_ALL
        loading_box_display[loading_box_height // 2] = Fore.LIGHTBLACK_EX + "◄" + " " * (loading_box_width - 2) + "►" + Style.RESET_ALL
        loading_box_display[loading_box_height // 2 + 1] = Fore.LIGHTBLACK_EX + "╰" + "─" * (loading_box_width - 2) + "╯" + Style.RESET_ALL

        percent_filled = 0

        while percent_filled <= 100:
            loading_bar_display = loading_bar_full[:int(percent_filled / 100 * loading_bar_length)] + "░" * (loading_bar_length - int(percent_filled / 100 *    loading_bar_length)) + " "
            loading_box_display[loading_box_height // 2] = Fore.RED + "◄" + loading_bar_display + "►" + Style.RESET_ALL

            percent_display = f"{percent_filled}%"
            percent_display_center = (loading_box_width - len(percent_display)) // 2
            loading_box_display[loading_box_height // 2 + 2] = Fore.RED + " " * percent_display_center + percent_display + " " * (loading_box_width - percent_display_center -  len(percent_display)) + Style.RESET_ALL

            animation = ["|", "/", "-", "\\"]
            loading_text_display = Fore.LIGHTBLACK_EX + f"{animation[percent_filled % len(animation)]}"+ Style.RESET_ALL + Fore.LIGHTRED_EX + f" {loading_text}" + Style.   RESET_ALL + Fore.LIGHTBLACK_EX + f" {animation[percent_filled % len(animation)]}" + Style.RESET_ALL

            for i in range(loading_box_height):
                print("\033[{};{}H{}".format(console_height // 2 - loading_box_height // 2 + i, console_width // 2 - loading_box_width // 2, loading_box_display[i]))
            print("\033[{};{}H{}".format(console_height // 2 - loading_box_height // 2 - 1, console_width // 2 - len(loading_text) // 2, loading_text_display))

            percent_filled += 1
            time.sleep(0.025)

        # Don't try and steal this - Aspect#6889
        # Credit if you wanna use it in your theme

    loading_screen()
    if fix["presence"]["enabled"] == True:
        client_id = fix['presence']['client_id']
        RPC = Presence(client_id)
        RPC.connect()

        RPC.update(
            details="• Sniping UGC Limiteds",
            state="• UGC Looter Theme",
            large_image="https://i.ibb.co/Lt0YG5d/asset.png",
            large_text="Xolo X UGC Looter",
            buttons=[{"label": "Join Xolo Discord", "url": "https://discord.gg/xolo"}]
        )
    else:
        pass
else:
    os.system("cls")
    
title = ("""
                        ██╗   ██╗ ██████╗  ██████╗    ██╗      ██████╗  ██████╗ ████████╗███████╗██████╗ 
                        ██║   ██║██╔════╝ ██╔════╝    ██║     ██╔═══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔══██╗
                        ██║   ██║██║  ███╗██║         ██║     ██║   ██║██║   ██║   ██║   █████╗  ██████╔╝
                        ██║   ██║██║   ██║██║         ██║     ██║   ██║██║   ██║   ██║   ██╔══╝  ██╔══██╗
                        ╚██████╔╝╚██████╔╝╚██████╗    ███████╗╚██████╔╝╚██████╔╝   ██║   ███████╗██║  ██║
                         ╚═════╝  ╚═════╝  ╚═════╝    ╚══════╝ ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                 
                                                    ☻ Best Ugc Sniper ☺                       
""")
def _print_stats(self) -> None:
        self.start_time = datetime.datetime.now()
        gradient_print(title, start_color=Color(0xe64545), end_color=Color(0xde8181))
        print(f"{Color(0xf28a8a)}                                                          « Info » {Color(0xf28a8a)}")
        print()    
        if self.task == "Item Scraper & Searcher":
            print(f"{Color(0xe64545)}                                              • ╚ Status ╗      →  {Color(0xde8181)}Checking..")
        elif self.task == "Item Buyer":
            print(f"{Color(0xe64545)}                                              • ╚ Status ╗      →  {Color(0xde8181)}Buying..")
        else:
            print(f"{Color(0xe64545)}                                              • ╚ Status ╗      →  {Color(0xde8181)}{self.task}")
        print(f"{Color(0xe64545)}                                              • ╚ Ids ╗         →  {Color(0xde8181)}{', '.join(self.items)}")
        print(f"{Color(0xe64545)}                                              • ╚ Started At ╗  →  {Color(0xde8181)}{self.start_time.strftime('%m/%d/%Y')}")
        print()
        rgbprint("                                              ────────────────────────────────",color=("f2a2a2"))
        print(f"{Color(0xf28a8a)}                                                          « Stats » {Color(0xf28a8a)}")
        print()
        print(f"{Color(0xe64545)}                                              • ╚ Looted ╗      →  {Color(0xde8181)}{self.buys}")
        print(f"{Color(0xe64545)}                                              • ╚ Errors ╗      →  {Color(0xde8181)}{self.errors}")
        print(f"{Color(0xe64545)}                                              • ╚ Speed ╗       →  {Color(0xde8181)}{self.last_time}")
        print(f"{Color(0xe64545)}                                              • ╚ Loot Checks ╗ →  {Color(0xde8181)}{self.checks}")
        print()    
        rgbprint("                                              ────────────────────────────────",color=("f2a2a2"))
        print(f"{Color(0xf28a8a)}                                                          « Credits » {Color(0xf28a8a)}")
        print()
        print(f"{Color(0xe64545)}                                              • ╚ Script ╗      →  {Color(0xde8181)}xolo#4942")
        print(f"{Color(0xe64545)}                                              • ╚ Theme ╗       →  {Color(0xde8181)}Aspect#6889")