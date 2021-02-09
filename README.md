# Find and Alert
This Python script uses one's WiFi connection in order to scan incoming traffic on the router, and identify if a device is connected to it. Perfect for a user to be alerted about their loved one's return home, as soon as their phone connects to the WiFi. 

## How it works
This program scans a wifi connections incoming traffic, and identify if a new device is being connected to the network. If it notices that this occurs, it then is designed to speak (or notify) the user that a new user has joined the network. If a pre-configured IP address is instantiated within the code, it will alert the user that the specific person joined the network, as shown below:
```py
IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')
```

## Disclaimer
This python script is intended for **Educational Purposes Only**. This code is written in a manner that prevents one from using this maliciously, as one would need to enter specific wifi credentials of the connection, only attainable if they are hosting the connection, thus limiting the use of this script to household use only, and not public use.
