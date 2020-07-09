#Archivo_main.py

from boot import *
from machine import Pin
from time import sleep
import usocket


server=usocket.socket()
server.bind(('192.168.4.1',8000))
server.listen(5)
print("Esperando Conexion")
conexion,addr=server.accept()
print("Conexion Establecida")
t="Bienvenido a MicroPython"
conexion.send(t.encode('UTF-8'))


def enviar_datos(valor):
    conexion.send(valor.encode('UTF-8'))

#int und_seg,dec_seg,und_min,dec_min;
und_seg=0;dec_seg=0;und_min=0;dec_min=0

a=Pin(12,Pin.OUT)
b=Pin(14,Pin.OUT)
c=Pin(27,Pin.OUT)
d=Pin(26,Pin.OUT)
e=Pin(25,Pin.OUT)
f=Pin(33,Pin.OUT)
g=Pin(32,Pin.OUT)

buf1=Pin(4,Pin.OUT)
buf2=Pin(16,Pin.OUT)
buf3=Pin(17,Pin.OUT)
buf4=Pin(5,Pin.OUT)

punto=Pin(18,Pin.OUT)

def led_display(valor):
    a.value(valor[0])
    b.value(valor[1])
    c.value(valor[2])
    d.value(valor[3])
    e.value(valor[4])
    f.value(valor[5])
    g.value(valor[6])
    sleep(0.001)
    

def deco_BCD(i_num):
    num=str(i_num)
    decodificador={'0':(1,1,1,1,1,1,0),'1':(0,1,1,0,0,0,0),'2':(1,1,0,1,1,0,1),'3':(1,1,1,1,0,0,1),'4':(0,1,1,0,0,1,1),'5':(1,0,1,1,0,1,1),'6':(1,0,1,1,1,1,1),'7':(1,1,1,0,0,0,0),'8':(1,1,1,1,1,1,1),'9':(1,1,1,1,0,1,1)}
    led_display(decodificador[num])

while(1):
    #punto.value(1)
    for dec_min in range(0,6):
        for und_min in range(0,10):
            for dec_seg in range(0,6):
                for und_seg in range(0,10):
                    for valor in range(0,10):
                        buf1.value(1)
                        deco_BCD(und_seg)
                        sleep(0.007)
                        buf1.value(0)
                        #sleep(0.003)
                        buf2.value(1)
                        deco_BCD(dec_seg)
                        sleep(0.007)
                        buf2.value(0)
                        punto.value(1)
                        #sleep(0.003)
                        buf3.value(1)
                        deco_BCD(und_min)
                        sleep(0.007)
                        buf3.value(0)
                        punto.value(0)
                        #sleep(0.003)
                        buf4.value(1)
                        deco_BCD(dec_min)
                        sleep(0.007)
                        buf4.value(0)
                        #sleep(0.003)
                        num=str(str(dec_min)+str(und_min)+' . '+str(dec_seg)+str(und_seg))
                        enviar_datos('\n                 '+num+'\n\n\n\n\n\n\n\n\n\n\n\n\n')
                        
                        
                                                                                                                      