"""TrainToBangkok"""
import pandas as pd
from copy import deepcopy
from math import inf
from .ConnectStationData import *
from .stationpathstorage import *
from .Connectline import *

#เก็บข้อมูล
information = pd.read_csv("TrainToBangkok\TrainToBangkok\TrainToBangkokDATA.csv", index_col="Station")
informationID = pd.read_csv("TrainToBangkok\TrainToBangkok\TrainToBangkokDATA.csv", index_col="Station ID")

#หาสถานีเชื่อมที่ใกล้ที่สุด
def startstop(currentstation, word, connect):
    stationnow = information.loc[currentstation]["Station ID"]
    linecan = line[information.loc[currentstation]["Colorline"]]

    checkline = (stationnow.split())[0] #ใช้สร้างตัวเชคสีสาย
    checknum = (stationnow.split())[1]

    start = dict()
    tod = ""
    for i in linecan:
        vali = i.split(",")
        for j in vali:
            if checkline in j:
                tod = (j.split())[1]
                start.update({i:((abs(int(tod)-int(checknum))), information.loc[currentstation]["Colorline"])})
                tod = ""
                continue

    connect.update({word:start})

    for i in linecan:
        connect[i].update({word:(connect[word][i][0], information.loc[currentstation]["Colorline"])})
    return connect

#ใช้หาสถานีตอนนี้
def setupstation(currentstation, wantstation, word, shortest, connect):
    if word == information.loc[currentstation]["Station ID"]:
        connect = startstop(currentstation, word, connect)
        shortest.update({word:[0, word]})
    else:
        connect = startstop(wantstation, word, connect)
        shortest.update({word : [inf, ""]})
    return connect, shortest

#หาเส้นทางที่สั้นที่สุดจากสถานีที่เป็นจุดเชื่อมต่างๆ
def shortestpath(start, connect, shortest):
    already = set()
    check = start
    tocheck = list()
    while True:
        storage = shortest
        base = shortest[check][0]
        nextcheck = list(connect[check].keys())
        tocheck.extend(nextcheck)
        for i in nextcheck:
            if (connect[check][i][0] + base) < shortest[i][0]:
                shortest[i][0] = (connect[check][i][0]) + base
                shortest[i][1] = check
        already.add(check)
        if shortest == storage and len(already) == len(connect):
            break
        else:
            check = tocheck.pop(0)
    return shortest
        
#ใช้หาทางไปที่สถานี
def findpath(start, end, connect, shortest):
    check = end
    passstation = list()
    while check != start:
        passstation.append(check)
        check = shortest[check][1]
    passstation.append(start)
    passstation = passstation[::-1]

    line = list()
    first = passstation[0]
    total = 0
    come = [0, connect[passstation[0]][passstation[1]][1]]
    for i in range(1, len(passstation)):
        back = connect[passstation[i]][passstation[i-1]]
        if come[1] != back[1]:
            total += come[0]
            line.append([first, come[1], total, passstation[i-1]])
            total = 0
            first = passstation[i-1]
        else:
            total += come[0]
        come = back
    total += come[0]
    line.append([first, come[1], total, passstation[i]])
    return line

def inputvalue(currentstation, wantstation):
    special = ('บางซี่อ', 'สถานีกลางกรุงเทพอภิวัฒน์', 'พหลโยธิน', 'ห้าแยกลาดพร้าว', 'เพชรบุรี', 'มักกะสัน', 'สุขุมวิท', 'อโศก', \
               'สีลม', 'ศาลาแดง', 'ตลาดพลู', 'ราชพฤกษ์', 'ช่องนนทรี', 'สาทร')
    for i in [currentstation, wantstation]:
        if i in special:
            check = 'BLUE 17,RED 6' if i == 'บางซี่อ' or i == 'สถานีกลางกรุงเทพอภิวัฒน์' else False
            check = 'BLUE 20,GREEN 16' if i == 'พหลโยธิน' or i == 'ห้าแยกลาดพร้าว' else check
            check = 'BLUE 27,BLACK 3' if i == 'เพชรบุรี' or i == 'มักกะสัน' else check
            check = 'BLUE 28,GREEN 29' if i == 'สุขุมวิท' or i == 'อโศก' else check
            check = 'BLUE 32,LIGHTB 11' if i == 'สีลม' or i == 'ศาลาแดง' else check
        else:
            check = information.loc[i]["Station ID"]
        start = check if i == currentstation else start
        end = check if i == wantstation else False
    return start, end

def outputval(station):
    special = ('BLUE 17,RED 6', 'BLUE 20,GREEN 16', 'BLUE 27,BLACK 3', 'BLUE 28,GREEN 29', 'BLUE 32,LIGHTB 11')
    for connect in station:
        if connect[0] in special:
            for i in connect[0].split(','):
                if connect[1].upper() in i:
                    station[station.index(connect)][0] = informationID.loc[i]["Station"]
        else:
            connect[0] = informationID.loc[connect[0]]["Station"]
        if connect[-1] in special:
            for i in connect[-1].split(','):
                if connect[1].upper() in i:
                    station[station.index(connect)][-1] = informationID.loc[i]["Station"]
        else:
            connect[-1] = informationID.loc[connect[-1]]["Station"]
        
        station[station.index(connect)][1] = 'sukhumvit' if station[station.index(connect)][1] == 'green' else station[station.index(connect)][1]
        station[station.index(connect)][1] = 'silom' if station[station.index(connect)][1] == 'lightb' else station[station.index(connect)][1]
        station[station.index(connect)][1] = 'gold' if station[station.index(connect)][1] == 'orange' else station[station.index(connect)][1]
        station[station.index(connect)][1] = 'airportlink' if station[station.index(connect)][1] == 'black' else station[station.index(connect)][1]

    return station

#เชื่อมต่อ function ต่างๆเข้าด้วยกัน
def searchpath(currentstation, wantstation):
    connect = deepcopy(storageconnect)
    shortest = deepcopy(storageshortest)
    
    start, end = inputvalue(currentstation, wantstation)

    if "," not in start:
        start = information.loc[currentstation]["Station ID"]
        connect, shortest = setupstation(currentstation, wantstation, start, shortest, connect)
    elif "," in start:
        shortest[start][0] = 0
        shortest[start][1] = start
    if "," not in end:  
        end = information.loc[wantstation]["Station ID"]
        connect, shortest = setupstation(currentstation, wantstation, end, shortest, connect)
    
    shortest = shortestpath(start, connect ,shortest)
    station = findpath(start, end, connect, shortest)
    station = outputval(station)
    return station

