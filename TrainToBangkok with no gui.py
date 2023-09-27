import pandas as pd

# อ่านข้อมูลจากไฟล์ CSV
information = pd.read_csv("TrainToBangkokDATA.csv", index_col="Station")

# สร้างคำสั่งหาเส้นทางระหว่างสถานี
def find_route(start_station, end_station, lines, line_connections):
    start_line = information.loc[start_station]["Colorline"]
    end_line = information.loc[end_station]["Colorline"]
    
    # ถ้าสายเดียวกัน
    if start_line == end_line:
        print(f"ใช้สาย {start_line}")
    else:
        # หาสายที่เชื่อมระหว่างสายเริ่มต้นและสายปลายทาง
        common_lines = line_connections.get(start_line, set()) & line_connections.get(end_line, set())
        
        if common_lines:
            # ถ้ามีสายรถไฟร่วมกัน
            print(f"ใช้สายรถไฟ {', '.join(common_lines)} และเปลี่ยนที่สถานี {lines[start_line]}")
        else:
            print("ไม่มีเส้นทางรถไฟระหว่างสถานีนี้")

# สร้างดิกชันนารีสำหรับการเชื่อมต่อระหว่างสายรถไฟ
line_connections = {
    "Blue": {"Lightblue", "Green", "Purple", "Red"},
    "Lightblue": {"Blue", "Green", "Orange", "Littleyellow"},
    "Orange": {"Lightblue"},
    "Littleyellow": {"Lightblue"},
    "Purple": {"Pink", "Red", "Blue"},
    "Red": {"Purple", "Blue", "Pink"},
    "Green": {"Pink", "Blue", "Black", "Lightblue", "Yellow"},
    "Pink": {"Purple", "Red", "Green"},
    "Yellow": {"Blue", "Black", "Green"},
    "Black": {"Blue", "Green", "Yellow"},
}
# สร้างดิกชันนารีสำหรับเก็บสถานีที่ต้องการเปลี่ยนสาย
lines = {
    "Blue": "B5",
    "Lightblue": "LY1",
    "Orange": "O3",
    "Littleyellow": "LY3",
    "Purple": "PU16",
    "Red": "R6",
    "Green": "G16",
    "Pink": "PI1",
    "Yellow": "Y1",
    "Black": "BL23",
}

# รับค่าสถานีต้นทางและปลายทางจากผู้ใช้
start_station = input("ป้อนสถานีต้นทาง: ")
end_station = input("ป้อนสถานีปลายทาง: ")

find_route(start_station, end_station, lines, line_connections)

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
    for i in (currentline & wantline):
      crossline.insert(total, i)
    return crossline

#รับ input มาทดลองโปรแกรม
currentstation = input()
wantstation = input()
currentline = information.loc[currentstation]["Colorline"]
wantline = information.loc[wantstation]["Colorline"]
crossline = find_colorline(currentline, wantline, line_connections)
