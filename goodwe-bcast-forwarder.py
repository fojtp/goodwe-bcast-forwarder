#!/usr/bin/python

import socket

localPort = 48899
localPort2 = 58899
bufferSize = 1024
GoodWeLAN = '192.168.1.1'
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
ClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
ClientSocket.bind((GoodWeLAN ,localPort2))
while(True):
    try:
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPServerSocket.bind(('', localPort))
        data, addr = UDPServerSocket.recvfrom(bufferSize)
        if data.decode() == "WIFIKIT-214028-READ":
            try:
                ClientSocket.sendto(data, ("255.255.255.255", localPort))
            except Exception as e:
                        print(str(e))
        data2, addr2 = ClientSocket.recvfrom(bufferSize)
        try:
            UDPServerSocket.sendto(data2, addr)
        except Exception as e:
            print(str(e))
    except Exception as e:
        print(str(e))
