"""traintobangkok"""

blue = ["หลักสอง", "บางแค", "ภาษีเจริญ", "เพชรเกษม 48", ("บางหว้า สายน้ำเงิน", "บางหว้า สายฟ้า") \
          , "บางไผ่", "ท่าพระ"]
blueswap = ["จรัญฯ 13", "ไฟฉาย", "บางขุนนนท์", "บางยี่ขัน", "สิรินธร", "บางพลัด","บางอ้อ", "บางโพ", \
          ("เตาปูน สายน้ำเงิน", "เตาปูน สายม่วง"), ("บางซี่อ", "สถานีกลางกรุงเทพอภิวัฒน์ซ้าย", "สถานีกลางกรุงเทพอภิวัฒน์ขวา"), \
          "กำแพงเพชร", ("สวนจตุจักร", "หมอชิต"), ("พหลโยธิน", "ห้าแยกลาดพร้าว"), \
          ("ลาดพร้าว สายฟ้า", "ลาดพร้าว สายเหลือง"), "รัชดาภิเษก", "สุทธิสาร", "ห้วยขวาง", "ศูนย์วัฒนธรรมแห่งประเทศไทย",\
            "พระราม 9",("เพชรบุรี", "มักกะสัน"), "สุขุมวิท", ("พร้อมพงษ์", "อโศก"), "ศูนย์ประชุมแห่งชาติสิริกิติ์", \
            "คลองเตย", "ลุมพินี", ("สีลม", "ศาลาแดง"), "สามย่าน", "หัวลำโพง", "วัดมังกร", "สามยอด", "สนามไชย", "อิสรภาพ"]
lightblue = [("บางหว้า สายฟ้า", "บางหว้า สายน้ำเงิน"), "วุฒากาศ", ("ตลาดพลู", "ราชพฤกษ์"), "โพธิ์นิมิตร", "วงเวียนใหญ่",\
              ("กรุงธนบุรี สายฟ้า", "กรุงธนบุรี สายส้ม"), "สะพานตากสิน", "สุรศักดิ์", "เซนต์หลุยส์", ("ช่องนนทรี", "สาทร"), \
              ("ศาลาแดง", "สีลม"), "ราชดำริ", ("สยาม สายฟ้า", "สยาม สายเขียว"), "สนามกีฬาแห่งชาติ"]
orange = ["คลองสาน", "เจริญนคร", ("กรุงธนบุรี สายส้ม", "กรุงธนบุรี สายฟ้า")]
littleyellow = [("ราชพฤกษ์", "ตลาดพลู"), "สะพานพระราม 3", "เจริญราษฎร์", "สะพานพระราม 9", "วัดดอกไม้", "วัดปริวาส",\
                  "วัดด่าน", "นราราม 3", "ถนนจันทน์", "เทคนิคกรุงเทพ", "อาคารสงเคราะห์", ("สาทร", "ช่องนนทรี")]
purple = ["คลองบางไผ่", "ตลาดบางใหญ่", "สามแยกบางใหญ่", "บางพลู", "บางรักใหญ่", "บางรักน้อยท่าอิฐ", "ไทรม้า", \
          "สะพานพระนั่งเหล้า", "แยกนนทบุรี 1", "บางกระสอ", ("ศูนย์ราชการนนทบุรี สายม่วง", "ศูนย์ราชการนนทบุรี สายชมพู"), \
            "กระทรวงสาธารณสุข", "แยกติวานนท์", "วงศ์สว่าง", ("บางซ่อน สายม่วง", "บางซ่อน สายแดง"), ("เตาปูน สายม่วง", "เตาปูน สายน้ำเงิน")]
leftred = ["ตลิ่งชัน", "บางบำหรุ", "บางกรวย", "สะพานพระราม 6", ("บางซ่อน สายแดง", "บางซ่อน สายม่วง"), ("สถานีกลางกรุงเทพอภิวัฒน์ซ้าย", "สถานีกลางกรุงเทพอภิวัฒน์ขวา", "บางซี่อ")]
rightred = [( "สถานีกลางกรุงเทพอภิวัฒน์ขวา", "สถานีกลางกรุงเทพอภิวัฒน์ซ้าย", "บางซี่อ"), "จตุจักร", "วัดเสมียนนารี", "บางเขน", \
            "ทุ่งสองห้อง", ("หลักสี่ สายแดง", "หลีกสี่ สายชมพู"), "การเคหะฯ", "ดอนเมือง", "หลักหก", "รังสิต"]
green = ["คูคต", "แยก คปอ", "พิพิธภัณฑ์กองทัพอากาศ", "โรงพยาบาลภูมิพลอดุลยเดช", "สะพานใหม่", " สายหยุด", \
          "พหลโยธิน 59", ("วัดพระศรีมหาธาตุ สายเขียว", "วัดพระศรีมหาธาตุ สายชมพู"),"กรมทหารราบที่ 11", "บางบัว", \
          "กรมป่าไม้", "มหาวิทยาลัยเกษตรศาสตร์", "เสนานิคม", "รัชโยธิน", "พหลโยธิน 24", ("ห้าแยกลาดพร้าว","พหลโยธิน"), \
            ("หมอชิต", "สวนจตุจักร"), "สะพานควาย", "เสนาร่วม", "อารีย์", "สนามเป้า", "อนุสาวรีย์ชัยสมรภูมิ", \
              ("พญาไทย สายเขียว", "พญาไทย สายดำ"), "ราชเทวี", ("สยาม สายเขียว", "สยาม สายฟ้า"), "ชิดลม", \
                "เพลินจิต", "นานา", ("อโศก", "สุขุมวิท"), "พร้อมพงษ์", "ทองหล่อ", "เอกมัย", "พระโขนง", \
                  "อ่อนนุช", "บางจาก", "ปุณณวิถี", "อุดมสุข", "บางนา", "แบริ่ง", ("สำโรง สายเขียว", "สำโรง สาย เหลื่อง"), \
                    "ปู่เจ้า", "ช้างเอราวัณ", "โรงเรียนนายเรือ", "ปากน้ำ", "ศรีนครินทร์", "แพรกษา", "สายลวด", "เคหะฯ"]
pink = [("ศูนย์ราชการนนทยุรี สายชมพู", "ศูนย์ราชการนนทยุรี สายม่วง"), "แคราย", "สนามบินน้ำ", "สามัคคี", "กรมชลประทาน", "แยกปากเกร็ด", "เลี่ยงเมืองปากเกร็ด", \
        "แจ้งวัฒนะปากเกร็ด 28", "เมืองทองธานี", "แจ้งวัฒนะ 14", "ศูนย์ราชการเฉลิมพระเกียรติ", "โทรคมนาคม", ("หลักสี่ สายชมพู", "หลักสี่ สายแดง"), "ราชภัฎพระนครเหนือ", \
          ("วัดพระศรีมหาธาตุ สายชมพู", "วัดพระศรีมหาธาตุ สายเขียว"), "รามอินทรา 3", "ลาดปลาเค้า", "รามอินทรา กม.4", "มัยลาภ", "วัชรพล", \
            "รามอินทรา กม.6", "คู้บอน", "รามอินทรา กม.9", "วงแหวนรามอินทรา", "นพรัตน์", "บางชัน", "เศรษบุตรบำเพ็ญ", \
              "ตลาดมีนบุรี", "มีนบุรี"]
yellow = [("ลาดพร้าว สายเหลือง", "ลาดพร้าว สายน้ำเงิน"), "ภาวนา", "โชคชัย 4", "ลาดพร้าว 71", "บาดพร้าว 83", "มหาดไทย", \
          "ลาดพร้าว 101", "บางกะปิ", "แยกลำสาลี", "ศรีกรีฑา", ("หัวหมาก สายเหลือง", "หัวหมาก สายแดง"), "กลันตัน", \
            "ศรีนุช", "ศรีนครินทร์ 38", "สวนหลวง ร.9", "ศรีอุดม", "ศรีเอี่ยม", "ศรีลาซาล", "ศรีแบริ่ง", "ศรีด่าน", "ศรีเทพา", \
              "ทัพวัล", ("สำโรง สายเหลือง", "สำโรง สายเขียว")]
black = [("พญาไทย สายดำ", "พญาไทย สายเขียว"), "ราชปรารภ", ("มักกะสัน", "เพชรบุรี"), "รามคำแหง", \
         ("หัวหมาก สายดำ", "หัวหมาก สายเหลือง"), "บ้านทับช้าง", "ลาดกระบัง", "สุวรรณภูมิ"]