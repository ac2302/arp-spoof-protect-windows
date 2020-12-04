# arp-spoof-protect-windows
Notifies you if your arp is being spoofed and pops up a window with the mac address of the attacker when it detects an arp spoofing attack.

by default, it searches every 30 seconds. you can change it by changing ```delay``` in main.py

## installation
- download the .exe from the [releases](example.com)
- create a shortcut to the .exe in ```C:\Users\<User>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup``` . replace the <User> with the name of your user.
- the program will now start when you boot the pc
  
## usage
* if you close the window, it will reappear in 30 seconds (or whatever delay you have chosen)
* to stop the message from popping up again, press the ignore button
