#!/usr/bin/python3
"""Learning about Python SSH | rzfeeser@alta3.com"""

# used to remove warnings from packages
import warnings
import json
import paramiko

# filter out any warnings with the word Paramiko
warnings.filterwarnings(action="ignore", module=".*paramiko.*")

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data

    # List of Dictionaries
    #credz = [{"un": "bender", "ip": "10.10.2.3"}, {"un": "zoidberg", "ip": "10.10.2.5"}, {"un": "fry", "ip": "10.10.2.4"}]
    
    # Plain Text File
    #with open("credz.txt", "r") as cred_file:
    #    credz = cred_file.readlines()
    #    print(type(credz))
    #    print(credz)
    #    input()

    # JSON File
    with open("credz.json", "r") as cred_file:
        credz = json.load(cred_file)
        print(type(credz))
        print(credz)

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
    txt = ""
    # loop across the collection credz
    for cred in credz:
        ## create a session object
        sshsession = paramiko.SSHClient()
        #data = cred.split()
        #print(data)
        #input()
        #cred = {"un": data[0], "ip": data[1]}
        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        conn_data = "Connecting to... " + cred.get("un") + "@" + cred.get("ip")
        #                            data[0]                 data[1]
        print(conn_data)
        ## make a connection
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        ## touch the file goodnews.everyone in each user's home directory
        sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

        ## list the contents of each home directory
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))

        ## display output
        ls_command = sessout.read().decode('utf-8')
        print(ls_command)

        txt += f"{conn_data}\n{ls_command}\n"
        #txt += conn_data + ls_command

        ## close/cleanup SSH connection
        sshsession.close()

    print("Thanks for looping with Alta3!")
    #print(txt)
    with open("results.txt", "w") as fi:
        fi.write(txt)
        print("Data saved in results.txt")

main()

