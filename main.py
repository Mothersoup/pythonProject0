# -*- coding: UTF-8 -*
import mysql.connector
import test
from rabboni import *
from rabboni import Rabboni
import time, sys

try:
    rabbo = Rabboni(mode="BLE")  # 先宣告一個物件
except Exception as e:
    print(e)
    sys.exit()
try:
    rabbo.scan()
    rabbo.print_device()
    rabbo.connect("D4:3F:41:4D:5F:59")
    time.sleep(2)
    rabbo.read_data()
    print(123)
except:
    print('error')

try:
    control = True
    while control:
        Xv = int(rabbo.Accx*100)
        Yv = int(rabbo.Accy*100)
        Zv = int(rabbo.Accz*100)
        time.sleep(0.25)
        test.update(Xv,Yv,Zv)
except KeyboardInterrupt:
    rabbo.stop()
    con.close()
