import art
def common_display(f):
    my_art = art.text2art("Auto Message Sender")
    print(my_art)
    if f==1:
        print('First hover over text input area of website once there press i , Then hover over send buton area once there press i,\nPress r to Reset the Coord if you want in between the 2 coords')
    elif f==2:
        print('Enter Time in the future to send the automated message in (if nothing provided sends on current time): \nEnter how many times do you want it repeated (if nothing provided sends only one time): \nEnter what message to send.')
    