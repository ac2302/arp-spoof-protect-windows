# arp-spoof-protect-windows
Notifies you if your arp is being spoofed and pops up a window with the mac address of the attacker when it detects an arp spoofing attack.

by default, it searches every 30 seconds. you can change it by changing ```delay``` in main.py

## run
- install python
- download [main.py](main.py)
- cd to the directorycontaining the main.py file
- ```python main.py```
  
## usage
* if you close the window, it will reappear in 30 seconds (or whatever delay you have chosen)
* to stop the message from popping up again, press the ignore button
