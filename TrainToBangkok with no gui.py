"""TrainToBangkok"""
import pandas as pd
from Data import ConnectStationData, stationpathstorage, Connectline
from math import inf
import time

#เก็บข้อมูล
information = pd.read_csv("Data\TrainToBangkokDATA.csv", index_col="Station")

#หาสถานีเชื่อมที่ใกล้ที่สุด
def startstop(currentstation, word):
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
                start.update({i:(abs(int(tod)-int(checknum)))})
                tod = ""
                continue

    ConnectStationData.connect.update({word:start})

    for i in linecan:
        ConnectStationData.connect[i].update({word:ConnectStationData.connect[word][i]})

#ใช้หาสถานีตอนนี้
def setupstation(station, word):
    if word == "start":
        startstop(station, word)
        stationpathstorage.shortest.update({word:[0, word]})
    else:
        startstop(station, word)
        stationpathstorage.shortest.update({word : [inf, ""]})

def forsort(key):
    if key == "start":
        return -inf
    elif key == "end":
        return inf
    else:
        return (list(ConnectStationData.connect.keys())).index(key)

#หาเส้นทางที่สั้นที่สุดจากสถานีที่เป็นจุดเชื่อมต่างๆ
def shortestpath(start):
    already = set()
    check = start
    tocheck = list()
    while True:
        storage = stationpathstorage.shortest
        base = stationpathstorage.shortest[check][0]
        nextcheck = list(ConnectStationData.connect[check].keys())
        checknow = [i for i in ConnectStationData.connect[check]]
        tocheck.extend(checknow)
        for i in nextcheck:
                if (ConnectStationData.connect[check][i] + base) < stationpathstorage.shortest[i][0]:
                    stationpathstorage.shortest[i][0] = (ConnectStationData.connect[check][i]) + base
                    stationpathstorage.shortest[i][1] = check
        already.add(check)
        if stationpathstorage.shortest == storage and len(already) == len(ConnectStationData.connect):
            break
        else:
            check = tocheck.pop(0)
        

#เชื่อมต่อ function ต่างๆเข้าด้วยกัน
def main():
    currentstation = input("ตอนนี้คุณอยู่ที่สถานี : ")
    wantstation = input("คุณอยากไปที่สถานี : ")
    if "," in information.loc[currentstation]["Station ID"]:
        start = information.loc[currentstation]["Station ID"]
    if "," in information.loc[wantstation]["Station ID"]:
        setupstation(currentstation, "start")
        start = "start"
    else:
        setupstation(currentstation, "start")
        setupstation(wantstation, "end")
        start = "start"
    shortestpath(start)
    print(stationpathstorage.shortest)
    print(time.process_time())
main()
