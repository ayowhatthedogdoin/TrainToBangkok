"""TrainToBangkok"""
import pandas as pd
from Data import ConnectStationData, stationpathstorage,Connectline

#เก็บข้อมูล
information = pd.read_csv("Data\TrainToBangkokDATA.csv", index_col="Station")
connect = ConnectStationData.connect

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

#ใช้หาสถานีตอนนี้
def setupstation(currentstation, wantstation):
    if "," in currentstation:
        ConnectStationData.connect["start"] = ConnectStationData.connect.pop[information.loc[currentstation]["Station ID"]]
        ConnectStationData.connect["end"] = ConnectStationData.connect.pop[information.loc[wantstation]["Station ID"]]
    else:
        startstop(information.loc[currentstation]["Station ID"], "start")
        startstop(information.loc[wantstation]["Station ID"], "end")

#หาเส้นทางที่สั้นที่สุดจากสถานีที่เป็นจุดเชื่อมต่างๆ
def shortestpath(currentstation, wantstation):
    allconnect = list(connect.keys())
    """while len(allconnect) != 0:
        print(allconnect)"""

#เชื่อมต่อ function ต่างๆเข้าด้วยกัน
def main():
    currentstation = input("ตอนนี้คุณอยู่ที่สถานี : ")
    wantstation = input("คุณอยากไปที่สถานี : ")
    setupstation(currentstation, wantstation)

main()
