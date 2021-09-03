import pyshark

def main():
    cap = pyshark.FileCapture("pythoncapture.pcap")

    for packet in cap:
        print(packet)

main()
