#3python3

import socket
import time

host = '' 
port = 9000
myAddr = host,port

def rectangle():
     
     socket.sendto('forward 50'.encode('utf-8'), ryze_addr)
     response, ip = socket.recvfrom(1024)
     if response == b'ok':
          socket.sendto('ccw 90'.encode('utf-8'), ryze_addr)
          response, ip = socket.recvfrom(1024)
          if response == b'ok':
               time.sleep(1)
     

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((myAddr))

ryze_ip = '192.168.10.1'
ryze_port = 8889
ryze_addr = (ryze_ip, ryze_port)

socket.sendto('command'.encode('utf-8'), ryze_addr)
repeat = 0

try:
     while True:
          response, ip = socket.recvfrom(1024)
          if response != b'ok':
               print ("no command - sorry we dont fly")
               break
          socket.sendto('battery?'.encode('utf-8'), ryze_addr)
          response, ip = socket.recvfrom(1024)
          response = int(response)
          print("battery power: " , response , "%")
          if response < 10:
               print ("It is a pity that we will not fly, the state of the battery is: " , response , "%")
               break
          socket.sendto('takeoff'.encode('utf-8'), ryze_addr)
          response, ip = socket.recvfrom(1024)
          print("takeOff: " , response)
          if response == b'ok':
               socket.sendto('speed 99'.encode('utf-8'), ryze_addr)
               response, ip = socket.recvfrom(1024)
               print("speed: " , response)
               if response == b'ok':
                    while repeat<=3:
                         rectangle()
                         repeat=repeat+1
          socket.sendto('land'.encode('utf-8'), ryze_addr)
          print("land")
          break
except KeyboardInterrupt:
    print("main_end")
    



