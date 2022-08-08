from datetime import datetime
import pyautogui
import keyboard
import common_display
import os 
import time as tm

def get_cord_for_init():
    def get_cord_for_init_values(point):
        x_cord=point.x 
        y_cord=point.y
        if keyboard.is_pressed('i'):
            os.system('cls')
            common_display.common_display(1)
            print('Coord Obtained: '+str((x_cord,y_cord)))
            return ((x_cord,y_cord))

        if keyboard.is_pressed('r'):
            os.system('cls')
            common_display.common_display(1)
            return ('reset')
        else: 
            pass
    os.system('cls')
    important_keys=[]
    common_display.common_display(1)
    while True:
        coord=get_cord_for_init_values(pyautogui.position())
        if coord!='reset':
            important_keys.append(coord)
        elif coord=='reset':
            important_keys=[]

        important_keys=dict.fromkeys(important_keys)        
        t_important_keys=important_keys
        important_keys=[]
        for i in t_important_keys:
            if i!=None:
                important_keys.append(i)
        
        if len(important_keys)==2:
            print('Text input Location: '+str(important_keys[0])+'\nSend Button Location: '+str(important_keys[1]))
            halt=input('Press Enter to continue')
            return important_keys

def add_more_actions(actions):
    os.system('cls')
    common_display.common_display(2)
    actions=actions
    actions.append(input('Enter Time in the Future:'))
    actions.append(input('Enter How many times to resend:'))
    actions.append(input('Enter the Message to send: '))
    actions.append(input('Shutdown after msging: '))
    
    if actions[3]=='':
        actions[3]=1

    if actions[5]=='':
        actions[5]=0
    
    return actions

def take_final_actions(actions):
    def message_it(first_location,msg,second_locations,repeat):
        for i in range(0,int(repeat)):
            pyautogui.moveTo(first_location)
            pyautogui.click()
            pyautogui.write(msg,interval=0.025)
            pyautogui.moveTo(second_locations)
            pyautogui.click()
    
    first_location=actions[0]
    second_locations=actions[1]
    time=actions[2]
    if ':' in time:
        time=time.split(':')
        if len(time)==3:
            hr=int(time[0])
            min=int(time[1])
            sec=int(time[2])
        else:
            hr=int(time[0])
            min=int(time[1])
            sec=0
    
    repeat=actions[3]
    msg=actions[4]
    shut_flag=int(actions[5])
    if time=='':
        message_it(first_location,msg,second_locations,repeat)
        print(actions)
        print('------------------------Executing The Planned task-------------------------')
        print('Current Time: '+str(datetime.now))
        print('Message Time: '+str(datetime.now))
    else:
        while True: 
            now=datetime.now()
            os.system('cls')
            common_display.common_display(3)
            print(actions)
            print('------------------------Executing The Planned task-------------------------')
            print('Current Time: '+str(now.hour)+':'+str(now.minute)+':'+str(now.second))
            print('Message Time: '+str(hr)+':'+str(min)+':'+str(sec))
            if hr==int(now.hour) and min==int(now.minute) and sec==int(now.second):
                message_it(first_location,msg,second_locations,repeat)
                break
            tm.sleep(0.5)
    
    if shut_flag==1:
        os.system('shutdown /s /t 1')