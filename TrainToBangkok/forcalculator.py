"""TrainToBangkok"""
import pandas as pd
from copy import deepcopy
from math import inf
from Data import ConnectStationData, stationpathstorage, Connectline

#เก็บข้อมูล
information = pd.read_csv("TrainToBangkok\Data\TrainToBangkokDATA.csv", index_col="Station")
informationID = pd.read_csv("TrainToBangkok\Data\TrainToBangkokDATA.csv", index_col="Station ID")

#หาสถานีเชื่อมที่ใกล้ที่สุด
def startstop(currentstation, word, connect):
    stationnow = information.loc[currentstation]["Station ID"]
    linecan = Connectline.line[information.loc[currentstation]["Colorline"]]

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
    for i in range(len(passstation)-1):
        going = connect[passstation[i]][passstation[i+1]]
        if come[1] != going[1]:
            total += come[0]
            line.append((come[1], total, [first, passstation[i]]))
            total = 0
            first = passstation[i]
        else:
            total += come[0]
        come = going
    total += come[0]
    line.append((come[1], total, (first, passstation[-1])))
    return line, passstation

#เชื่อมต่อ function ต่างๆเข้าด้วยกัน
def searchpath(currentstation, wantstation):
    connect = deepcopy(ConnectStationData.connect)
    shortest = deepcopy(stationpathstorage.shortest)
    
    start = information.loc[currentstation]["Station ID"]
    end = information.loc[wantstation]["Station ID"]

    if "," not in information.loc[currentstation]["Station ID"]:
        start = information.loc[currentstation]["Station ID"]
        connect, shortest = setupstation(currentstation, wantstation, start, shortest, connect)
    elif "," in information.loc[currentstation]["Station ID"]:
        shortest[start][0] = 0
        shortest[start][1] = start
    if "," not in information.loc[wantstation]["Station ID"]:
        end = information.loc[wantstation]["Station ID"]
        connect, shortest = setupstation(currentstation, wantstation, end, shortest, connect)

    shortest = shortestpath(start, connect ,shortest)
    station, check = findpath(start, end, connect, shortest)

    """if information.loc[currentstation]["Colorline"] != information.loc[wantstation]["Colorline"] or len(check) > 3:
        for i in station:
            come = informationID.loc[i[-1][0]]["Station"]
            go = informationID.loc[i[-1][1]]["Station"]
            print(f"เดินทางจาก {come} ไปยัง {go} เป็นระยะทาง {i[1]} สถานี ด้วยสายสี {i[0]}")
    else:
        start = int((information.loc[currentstation]["Station ID"].split())[1])
        end = int((information.loc[wantstation]["Station ID"].split())[1])
        print(f'เดินทางจาก {currentstation} ไปยัง {wantstation} เป็นระยะทาง', abs(start-end), "สถานี")"""
    return station
