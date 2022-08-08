import pyautogui_actions
import keyboard

import os
import common_display

os.system('cls')
while True: 
    common_display.common_display(0)
    choice=input('Enter\n 1. To Start\n 2. To Quit\n')
    if choice=='1':
        actions=pyautogui_actions.get_cord_for_init()
        actions=pyautogui_actions.add_more_actions(actions)
        pyautogui_actions.take_final_actions(actions)

    elif choice=='2':
        exit()
    os.system('cls')