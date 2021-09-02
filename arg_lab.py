#!/usr/bin/env python3
import argparse

def server(port):
    x = "Your choice was server and it will run on port " + str(port)
    return x

def client(port):
    x = "Your choice was client and it will run on port " + str(port)
    return x

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    # if role == client , then we will run the client() function
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    parser.add_argument('-t', default='UDP', help='Choose Protocol')
    args = parser.parse_args()
    print(args)
    print(f"You will be using the {args.t} protocol")
    function = choices[args.role]
    print(function(args.p))

