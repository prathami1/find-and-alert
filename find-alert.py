import sys
import subprocess 
import os
from decouple import config

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')

fproc = subprocess.Popen(["ping", IP_NETWORK],stdout=subprocess.PIPE)
while True:
  line = proc.stdout.readline()
  if not line:
    break
  #filtering Process Begins Here
  connected_ip = line.decode('utf-8').split()[3]

  if connected_ip == IP_DEVICE:
      subprocess.Popen(["say", "User just connected to the network"])
