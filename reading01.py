#!/usr/bin/env python3
"""Reading in and writing out files"""

def main():
    # old method for opening files
    # requires closing the file object when done
    myfile = open("vendor.txt", 'r')

    # new method for opening files
    # closes file when indentation ends
    with open('vendor-ips.txt', 'w') as myoutfile:
        for line in myfile.readlines():
            splitline = line.split(' ')
            print(splitline[-1].strip())
            #myoutfile.write(splitline[-1] + '\n')

# ['', 'cisco', 'v18', 'ios', 'http://example.com/cisco', '192.168.1.55\n']
#   0      1       2      3                 4                     5
#   -6     -5     -4     -3                -2                    -1


    # close the open file object
    myfile.close()
main()

