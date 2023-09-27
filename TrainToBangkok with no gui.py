"""TrainToBangkok"""
import pandas as pd

#เก็บข้อมูล
information = pd.read_csv(r"TrainToBangkok\TrainToBangkokDATA.csv", index_col="Station")

#รวบรวมว่าสายใน dict ที่เป็น key ติดกับสายอะไรบ้าง โดยให้เป็น value
line = {
  "blueline" : {"rightredline", "leftredline", "lightblueline", "purpleline", "greenline"},
  "lightblueline" : {"blueline", "greenline", "orangeline"},
  "orangeline" : {"lightblueline"},
  "littleyellowline" : {"lightblueline"},
  "purpleblueline" : {"pinkline", "leftredline", "blueline"},
  "leftredblueline" : {"purpleline", "blueline"},
  "rightredblueline" : {"pinkline", "blueline"},
  "greenblueline" : {"pinkline", "blueline", "blackline", "lightblueline", "yellowline"},
  "pinkblueline" : {"purpleline", "redline", "greenline"},
  "yellowblueline" : {"blueline", "blackline", "greenline"},
  "blackblueline" : {"blueline", "greenline", "yellowline"},
}

def find_colorline(currentline, wantline, line):
    #ใช้หาว่ารถไฟต้องผ่านสายไหนบ้าง
    crossline = [currentline, wantline]

#รับ input มาทดลองโปรแกรม
currentstation = input()
wantstation = input()
currentline = information.loc[currentstation]["Colorline"]
wantline = information.loc[wantstation]["Colorline"]

find_colorline(currentline, wantline, line)