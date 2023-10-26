#file ใช้สร้างตัวเก็บข้อมูลเอาไว้หาทางที่สั้นที่สุด
from math import inf

shortest = {
    "PURPLE 11,PINK 1" : [inf, ""],
    "RED 11,PINK 13" : [inf, ""],
    "GREEN 8,PINK 15" : [inf, ""],
    "BLUE 20,GREEN 16" : [inf, ""],
    "GREEN 23,BLACK 1" : [inf, ""],
    "BLUE 28,GREEN 29" : [inf, ""],
    "GREEN 40,YELLOW 23" : [inf, ""],
    "BLUE 27,BLACK 3": [inf, ""],
    "YELLOW 11,BLACK 5":[inf, ""],
    "BLUE 21,YELLOW 1": [inf, ""],
    "BLUE 5,LIGHTB 1": [inf, ""],
    "BLUE 16,PURPLE 16": [inf, ""],
    "BLUE 17,RED 6": [inf, ""],
    "BLUE 32,LIGHTB 11" : [inf, ""], 
    "LIGHTB 3,LITTLEY 1" : [inf, ""],
    "LIGHTB 6,ORANGE 3" : [inf, ""],
    "LIGHTB 10,LITTLEY 12": [inf, ""],
    "PURPLE 15,RED 5" : [inf, ""],
    "LIGHTB 13,GREEN 25" : [inf, ""]
}