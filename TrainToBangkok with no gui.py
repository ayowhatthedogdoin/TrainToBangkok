"""TrainToBangkok"""
import pandas as pd

#เก็บข้อมูล
information = pd.read_csv(r"TrainToBangkok\TrainToBangkokDATA.csv", index_col="Station")

#รวบรวมว่าสายใน dict ที่เป็น key ติดกับสายอะไรบ้าง โดยให้เป็น value
line = {
  "blueline" : {"redline", "lightblueline", "purpleline", "greenline"},
  "lightblueline" : {"blueline", "greenline", "orangeline"},
  "orangeline" : {"lightblueline"},
  "littleyellowline" : {"lightblueline"},
  "purpleline" : {"pinkline", "redline", "blueline"},
  "redline" : {"purpleline", "blueline", "pinkline"},
  "greenline" : {"pinkline", "blueline", "blackline", "lightblueline", "yellowline"},
  "pinkline" : {"purpleline", "redline", "greenline"},
  "yellowline" : {"blueline", "blackline", "greenline"},
  "blackline" : {"blueline", "greenline", "yellowline"},
}

def find_colorline(currentline, wantline, line):
    #ใช้หาว่ารถไฟต้องผ่านสายไหนบ้าง
    crossline = [((currentline).lower()+"line"), (wantline).lower()+"line"]
    currentline = line[(currentline).lower()+"line"]
    wantline = line[(wantline).lower()+"line"]
    total = -1
    while len(currentline & wantline) == 0:
      crossline.insert(-1, (f"{''.join(wantline)}"))
      wantline = line[(f"{''.join(wantline)}")]
      total -= 1
    if not crossline[-1] in currentline:
      for i in (currentline & wantline):
        crossline.insert(total, i)
    return crossline

#รับ input มาทดลองโปรแกรม
currentstation = input()
wantstation = input()
currentline = information.loc[currentstation]["Colorline"]
wantline = information.loc[wantstation]["Colorline"]
crossline = find_colorline(currentline, wantline, line)
print(crossline)