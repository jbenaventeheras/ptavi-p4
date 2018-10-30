#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import sys
import json
import socketserver
from datetime import datetime, date, time, timedelta

if len(sys.argv) != 2:
    sys.exit('usage error: python3 server.py <port> ')
else:
    try:
        PUERTO = int(sys.argv[1])
        FORMAT = '%H:%M:%S %d-%m-%Y'
    except:
        sys.exit('usage error: python3 server.py <port>')

class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):

        dicc = {'address': '', 'expires': ''}
        list = []
        IP = self.client_address[0]
        PUERTO = self.client_address[1]

        for line in self.rfile:
            list.append(line.decode('utf-8'))
        message = list[0].split(' ')
        expires = list[1].split(' ')
        expires_user = expires[1].split('\r\n')[0]


        if message[0] == 'REGISTER':
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            user = message[1].split(':')[1]
            dicc['address'] = IP + ' ' + user
            expires_date = datetime.now() + timedelta(seconds=int(expires_user))
            dicc['expires'] = expires_date.strftime(FORMAT)
            print(dicc)




if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    serv = socketserver.UDPServer(('', PUERTO), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
