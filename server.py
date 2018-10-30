#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import sys
import json
import socketserver
from datetime import datetime, date, time, timedelta

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):

        dicc = {'address': ''}
        list = []
        IP = self.client_address[0]
        PUERTO = self.client_address[1]

        for line in self.rfile:
            list.append(line.decode('utf-8'))
            message = list[0].split(' ')
        print(message)

        if message[0] == 'REGISTER':
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            user = message[1].split(':')[1]
            dicc['address'] = IP + ' ' + user
            print(dicc['address'])


if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    serv = socketserver.UDPServer(('', 6001), EchoHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
