#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

def ip_addressify():
    iface = input("What Interface do you want the IP Address for? ")
    try:
        print((netifaces.ifaddresses(iface)[netifaces.AF_INET])[0]['addr']) 
    except ValueError as err:
        print(f"{iface} is not a valid interface name:", err)

def mac_addr(iface):
    print((netifaces.ifaddresses(iface)[netifaces.AF_LINK])[0]['addr']) 


print("Customization 01")
ip_addressify()

print("Customization 02 for 'docker0'")
mac_addr('docker0')

