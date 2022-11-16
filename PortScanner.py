import sys
import socket
import pyfiglet


ascii_banner = pyfiglet.figlet_format("TryHackMe \n Python 4 Pentesters \nPort Scanner")
print(ascii_banner) #for some reason this part of the programme only works on linux terminal


ip = '10.10.28.84' #chnage this ip to victim IP
open_ports =[]  #empty array to later store scanned ports

ports = range(1, 9999) #scanning range, change if need faster scan, full scan (65535)


def probe_port(ip, port, result = 1): #function tries to connect to port
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socekt variable hold the ip and port
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result


for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    

if open_ports: 
  print ("Open Ports are: ") 
  print (sorted(open_ports)) 
else: 
  print ("Looks like no ports are open :(")
