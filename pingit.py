#!/usr/bin/python3
import os
import argparse

## Ping router - returns True or False
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False


def parze():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", nargs='+', default=None, help="IP you want to ping")
    args = parser.parse_args()
    return args


def main():
    args = parze()
    print(args)
    if args.ip:
        switchlist = args.ip
    else:
        switchlist = ["172.0.1.2", "sw-1", "sw-2", "8.8.8.8"]   # CUSTOMIZE THIS LIST WITH IPs to PING
    print(switchlist)
    input()

    ## Use a loop to check each device for ICMP responses
    print("\n***** STARTING ICMP CHECKING *****")
    for x in switchlist:
        if ping_router(x):
            print(f"IP address {x} is responding to ICMP")
        else:
            print(f"IP address {x} is not responding to ICMP")

if __name__ == "__main__":
    main()

