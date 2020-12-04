import time
import sys
import tkinter
import threading
import subprocess

# config
delay = 30  #delay in seconds


# command for ignore button
def ignore():
    sys.exit()


# alert window
def alert(mac_addr='unknown'):
    root = tkinter.Tk()
    root.title('alert')
    tkinter.Label(root, padx=25, pady=15, font="default 17", text=f'you have been attacked by an arp spoof attack.\nDisconnect from the wireless network immidiately.\nthe mac-address of the attacker is probably\n{mac_addr}').grid(row=0, column=0)
    tkinter.Button(root, command=ignore, bg='red', fg='white', font="default 17", text="ignore").grid(row=1, column=0)
    root.lift() # focus on window 
    root.bell() # play sound
    root.mainloop()


# getting wifi mac
def wifi_mac():
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\r\n')
    mac = [line.split(': ')[1] for line in output if 'BSSID' in line][0]
    return mac


# getting gateway mac
def gateway_mac():
    # gettimg gateway
    output = subprocess.check_output(['ipconfig']).decode('utf-8').split('\r\n')
    gateway = [line.split(': ')[1] for line in output if 'Default Gateway' in line][0]
    # getting mac
    output = subprocess.check_output(['arp', '-a']).decode('utf-8').split('\r\n')
    mac = [line.split()[1] for line in output if (gateway+' ') in line][0]
    return mac.replace('-', ':')


# the loop
while True:
    hacked = False
    try:
        time.sleep(2)
        hacked = not wifi_mac() == gateway_mac()
        print(hacked)
    except:
        pass
    if hacked:
            alert(gateway_mac())
