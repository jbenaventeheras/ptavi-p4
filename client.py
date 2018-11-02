#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Programa cliente UDP que abre un socket a un servidor."""

import socket
import sys

if len(sys.argv) != 6:
        sys.exit('Usage: client.py ip puerto register' +
                 'sip_address')

SERVER = sys.argv[1]
PORT = int(sys.argv[2])
Client_user = sys.argv[4]
Mess_type = sys.argv[3]
expires_value = sys.argv[5]
Line_To_Send = ""


if Mess_type == 'register':
    Line_To_Send = ('REGISTER sip:' + Client_user + ' SIP/2.0\r\n' +
                    'Expires: ' + expires_value + '\r\n\r\n')
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
            my_socket.connect((SERVER, PORT))
            my_socket.send(bytes(Line_To_Send, 'utf-8') + b'\r\n')
            data = my_socket.recv(1024)
            print('Recibido -- ', data.decode('utf-8'))
else:
    sys.exit('Usage: client.py ip puerto register sip_address')

print("Socket terminado.")
