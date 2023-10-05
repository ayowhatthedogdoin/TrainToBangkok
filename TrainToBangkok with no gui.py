"""TrainToBangkok"""
import pandas as pd
from Data import ConnectStationData, stationpathstorage, Connectline
from math import inf

#เก็บข้อมูล
information = pd.read_csv("Data\TrainToBangkokDATA.csv", index_col="Station")

#หาสถานีเชื่อมที่ใกล้ที่สุด
def startstop(currentstation, word):
    stationnow = information.loc[currentstation]["Station ID"]
    linecan = list(Connectline.line[information.loc[currentstation]["Colorline"]])
    
    checkline = (stationnow.split())[0] #ใช้สร้างตัวเชคสีสาย
    checknum = (stationnow.split())[1]

    start = {}
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
def setupstation(currentstation, wantstation):
    if "," in currentstation:
        ConnectStationData.connect["start"] = ConnectStationData.connect.pop[information.loc[currentstation]["Station ID"]]
        ConnectStationData.connect["end"] = ConnectStationData.connect.pop[information.loc[wantstation]["Station ID"]]
        stationpathstorage.shortest["start"] = stationpathstorage.shortest.pop[information.loc[currentstation]["Station ID"]]
        stationpathstorage.shortest["end"] = stationpathstorage.shortest.pop[information.loc[wantstation]["Station ID"]]
    else:
        startstop(currentstation, "start")
        stationpathstorage.shortest.update({"start":0})
        startstop(wantstation, "end")
        stationpathstorage.shortest.update({"end":inf})

def forsort(key):
    if key == "start":
        return -inf
    elif key == "end":
        return inf
    else:
        return (list(ConnectStationData.connect.keys())).index(key)

#หาเส้นทางที่สั้นที่สุดจากสถานีที่เป็นจุดเชื่อมต่างๆ
def shortestpath(currentstation, wantstation):
    allconnect = list(ConnectStationData.connect.keys())
    allconnect.sort(key=forsort)
    check = "start"
    #while len(allconnect) != 0:
    for i in ConnectStationData.connect[check]:
        if ConnectStationData.connect[check][i] < stationpathstorage.shortest[i][0]:
            stationpathstorage.shortest[i][0] = ConnectStationData.connect[check][i]
            stationpathstorage.shortest[i][1] = check
    

#เชื่อมต่อ function ต่างๆเข้าด้วยกัน
def main():
    currentstation = input("ตอนนี้คุณอยู่ที่สถานี : ")
    wantstation = input("คุณอยากไปที่สถานี : ")
    setupstation(currentstation, wantstation)
    """shortestpath(currentstation, wantstation)"""
    print(ConnectStationData.connect)
main()
