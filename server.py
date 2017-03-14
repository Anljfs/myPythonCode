# -*- coding: utf-8 -*-
'''
Created on 2017年3月8日

@author: anlj
'''
import time
import socket
import sys
import threading
#from telnetlib import theNULL
#from _operator import length_hint

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as e :
    print('Bind failed. Error Code : ' + str(e[0]) + ' Message ' + e[1])
    sys.exit()
     
print('Socket bind complete')
 
#Start listening on socket
s.listen(10)
print('Socket now listening')

def receive(conn, length):
    str = conn.recv(length)
    while len(str)< length:
        #print(str)
        str = str + conn.recv(length - len(str))
    
    return str
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client     
    #infinite loop so that function do not terminate and thread do not end.
    #while True:
         
    #Receiving from client
    length = receive(conn, 4)
    print(length)
    data = ""
    if len(length) == 4 :
        data = receive(conn, int(length))
    else:
        print("接受长度太短")
        conn.send(b"receive valied")
    print(data)
    reply = b'0227021000000012M0101401014          0162284301200371850110000000000012017030610300801    101021201703062017010401030000041201703060001SMQD        011560001030000041              00000000000000000000586F9DA88F5541588D5DA8AA384F1D3D'
    if not data: 
        conn.close()
        return
    print("before")
    time.sleep(2)
    conn.sendall(reply)
    print("after")
    #came out of loop
    conn.close()
    print("end connection")
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    t = threading.Thread(target=clientthread, args=(conn,))
    t.start()
 
s.close()
