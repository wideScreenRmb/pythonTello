#3python3

import socket
import time
import ast
import msvcrt


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

def battTest():
    print("now i test power level")
    socket.sendto('battery?'.encode('utf-8'), ryze_addr)
    responseBatt, ip = socket.recvfrom(256)
    responseBattInt=int(responseBatt)
    lenBatt = len(responseBatt)
    if (responseBattInt <10):
        print("ryzeTello power level too low: " , responseBattInt , "%")
    print("ryzeTello power level: " , int(responseBatt[0:3]), "%")
    print("power level > 10 % lets go fly")

def heightTest():
    socket.sendto('height?'.encode('utf-8'), ryze_addr)
    responseHeight, ip = socket.recvfrom(256)
    print("ryzeTello Height: " , responseHeight)

def tofTest():
    print("Tof/height measurement...")
    socket.sendto('tof?'.encode('utf-8'), ryze_addr)
    responseTof, ip = socket.recvfrom(256)
    actualHeight = int(responseTof[0:3])
    print("actual height: " , actualHeight)

def takeOff():
    print("now i start")
    socket.sendto('takeoff'.encode('utf-8'), ryze_addr)
    responseTake, ip = socket.recvfrom(256)
    print("takeOff: " , responseTake)

def rotateCw():
    socket.sendto('cw 30'.encode('utf-8'), ryze_addr)
    responseCw, ip = socket.recvfrom(256)
    print("cw 30: " , responseCw)

def land():
    socket.sendto('land'.encode('utf-8'), ryze_addr)
    responseLand, ip = socket.recvfrom(256)
    print("land: " , responseLand)

def calculate():
    socket.sendto('tof?'.encode('utf-8'), ryze_addr)
    responseTof, ip = socket.recvfrom(256)
    print("tof: " , responseTof)
    actualHeight = int(responseTof[0:3])
    print("actual height [mm]: " , actualHeight)
    if actualHeight > 400 :
        downValue = int((actualHeight - 400)/10)
        strDownValue = str(downValue)
        print ("diff [cm]: " , strDownValue)
        socket.sendto(('down %s' % strDownValue).encode('utf-8'), ryze_addr)
        responseDown, ip = socket.recvfrom(256)
        print(responseDown)
    #socket.sendto('tof?'.encode('utf-8'), ryze_addr)
    #responseTof, ip = socket.recvfrom(256)
    #newActualHeight = int(responseTof[0:4])
    #print("new height [mm] is:" , newActualHeight)

def regulator():
    b=0
    while True:
            socket.sendto('tof?'.encode('utf-8'), ryze_addr)
            responseTof, ip = socket.recvfrom(256)
            lenResponseTof = len(responseTof)
            b=b+1
            print("***" , b)
            print("tof lenght: " , lenResponseTof)
            print("tof: " , responseTof)
            if lenResponseTof == 8:
                actualHeight = int(responseTof[0:4])
            if lenResponseTof == 7:
                actualHeight = int(responseTof[0:3])  
            print("actual height [mm]: " , actualHeight)
            if actualHeight > 400 :
                downValue = int((actualHeight - 400)/10)
                if downValue < 20 :
                    downValue = 0
                strDownValue = str(downValue)
                print ("diff down [cm]: " , strDownValue)
                socket.sendto(('down %s' % strDownValue).encode('utf-8'), ryze_addr)
                responseDown, ip = socket.recvfrom(256)
                print(responseDown)
                tofTest()
            if actualHeight < 400 :
                upValue = int((400 - actualHeight)/10)
                if upValue < 20 :
                    upValue = 0
                strUpValue = str(upValue)
                print ("diff up [cm]: " , strUpValue)
                socket.sendto(('up %s' % strUpValue).encode('utf-8'), ryze_addr)
                responseUp, ip = socket.recvfrom(256)
                print(responseUp)
                tofTest()
            if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
                aborted = True
                break
                
socket.sendto('command'.encode('utf-8'), ryze_addr)

try:
    while True:
        print ("begin comm Test...")
        responseComm, ip = socket.recvfrom(256)
        responseComm = (chr(responseComm[0]) + chr(responseComm[1]))
        print (responseComm)
        if responseComm != 'ok' :
            print ("no command - sorry i dont make any tests your ryzoTello")
            break;
        print ("a connection was made to RyzeTello...")
        battTest()
        takeOff()
        heightTest()
        calculate() #400 mm
        regulator()
        land()
        break
except KeyboardInterrupt:
    print("main_end")
        

