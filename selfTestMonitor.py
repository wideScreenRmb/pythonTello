#3python3

import socket
import time
import ast


host = '' 
port = 9000
myAddr = host,port

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((myAddr))

ryze_ip = '192.168.10.1'
ryze_port = 8889
ryze_addr = (ryze_ip, ryze_port)

#battery?
#time?
#height?
#temp?
#attitude?
#baro?
#tof?

delay = 2

def battTest():
    socket.sendto('battery?'.encode('utf-8'), ryze_addr)
    responseBatt, ip = socket.recvfrom(256)
    responseBattInt=int(responseBatt)
    lenBatt = len(responseBatt)
    if (responseBattInt <10):
        print("ryzeTello power level too low: " , responseBattInt , "%")
    print("ryzeTello power level: " , int(responseBatt[0:2]), "%")
    print("length String: " , lenBatt)
    
def timeTest():
    socket.sendto('time?'.encode('utf-8'), ryze_addr)
    responseTime, ip = socket.recvfrom(256)
    print("time: " , responseTime)
    
def heightTest():
    socket.sendto('height?'.encode('utf-8'), ryze_addr)
    responseHeight, ip = socket.recvfrom(256)
    print("ryzeTello Height: " , responseHeight)
    

def tempTest():
    socket.sendto('temp?'.encode('utf-8'), ryze_addr)
    responseTemp, ip = socket.recvfrom(256)
    print("actual string Temp: " , responseTemp)
    print("actual lowTemp: " , int(responseTemp[0:2]) , chr(responseTemp[5]))
    print("actual lowTemp: " , int(responseTemp[3:5]) , chr(responseTemp[5]))
    
    
def attTest():
    socket.sendto('attitude?'.encode('utf-8'), ryze_addr)
    responseAtt, ip = socket.recvfrom(256)
    print("att: " , responseAtt)

def pressTest():
    socket.sendto('baro?'.encode('utf-8'), ryze_addr)
    responsePress, ip = socket.recvfrom(256)
    print("baro: " , responsePress)

def tofTest():
    socket.sendto('tof?'.encode('utf-8'), ryze_addr)
    responseTof, ip = socket.recvfrom(256)
    print("tof: " , responseTof)

def takeOff():
    socket.sendto('takeoff'.encode('utf-8'), ryze_addr)
    responseTake, ip = socket.recvfrom(256)
    print("take: " , responseTake)
    #print ('takeoff')

def land():
    socket.sendto('land'.encode('utf-8'), ryze_addr)
    responseLand, ip = socket.recvfrom(256)
    print("land: " , responseLand)
    #print ('land')
   

socket.sendto('command'.encode('utf-8'), ryze_addr)

try:
    while True:
        responseComm, ip = socket.recvfrom(256)
        responseComm = (chr(responseComm[0]) + chr(responseComm[1]))
        print (responseComm)
        if responseComm != 'ok' :
            print ("no command - sorry i dont make any tests your's ryzoTello")
            break
        print("start")
        battTest()
        timeTest()
        heightTest()
        tempTest()
        attTest()
        pressTest()
        tofTest()
        takeOff()
        battTest()
        timeTest()
        heightTest()
        tempTest()
        attTest()
        pressTest()
        tofTest()
        land()
        break
except KeyboardInterrupt:
    print("main_end")
            

        
