document.getElementById('lines').addEventListener('change', function () {
    var selectedLine = this.value;
    var stationsSelect = document.getElementById('stations');
    var stationsList = document.getElementById('stations-list');

    stationsList.innerHTML = '';

    if (selectedLine === "sukhumvit") {
        populateStations(stationsSelect,
        ['คูคต', 'แยก คปอ', 'พิพิธภัณฑ์กองทัพอากาศ', 'โรงพยาบาลภูมิพลอดุลยเดช', 
        'สะพานใหม่', 'สายหยุด', 'พหลโยธิน 59', 'วัดพระศรีมหาธาตุ', 'กรมทหารราบที่ 11', 
        'บางบัว', 'กรมป่าไม้', 'มหาวิทยาลัยเกษตรศาสตร์', 'เสนานิคม', 'รัชโยธิน', 'พหลโยธิน 24', 
        'ห้าแยกลาดพร้าว', 'หมอชิต', 'สะพานควาย', 'เสนาร่วม', 'อารีย์', 'สนามเป้า', 'อนุสาวรีย์ชัยสมรภูมิ', 
        'พญาไท', 'ราชเทวี', 'สยาม', 'ชิดลม', 'เพลินจิต', 'นานา', 'อโศก', 'พร้อมพงษ์', 'ทองหล่อ', 
        'เอกมัย', 'พระโขนง', 'อ่อนนุช', 'บางจาก', 'ปุณณวิถี', 'อุดมสุข', 'บางนา', 'แบริ่ง', 'สำโรง', 
        'ปู่เจ้า', 'ช้างเอราวัณ', 'โรงเรียนนายเรือ', 'ปากน้ำ', 'ศรีนครินทร์', 'แพรกษา', 'สายลวด', 'เคหะฯ']);
    } else if (selectedLine === 'silom') {
        populateStations(stationsSelect,
        ['บางหว้า สายฟ้า', 'วุฒากาศ', 'ตลาดพลู', 'โพธิ์นิมิตร', 'วงเวียนใหญ่', 'กรุงธนบุรี', 'สะพานตากสิน', 
        'สุรศักดิ์', 'เซนต์หลุยส์', 'ช่องนนทรี', 'ศาลาแดง', 'ราชดำริ', 'สยาม', 'สนามกีฬาแห่งชาติ']);
    } else if (selectedLine === 'gold') {
        populateStations(stationsSelect,
        ['คลองสาน','เจริญนคร','กรุงธนบุรี']);
    } else if (selectedLine === 'pink') {
        populateStations(stationsSelect,
        ['ศูนย์ราชการนนทบุรี', 'แคราย', 'สนามบินน้ำ', 'สามัคคี', 'กรมชลประทาน', 'แยกปากเกร็ด', 'เลี่ยงเมืองปากเกร็ด', 
        'แจ้งวัฒนะปากเกร็ด 28', 'เมืองทองธานี', 'แจ้งวัฒนะ 14', 'ศูนย์ราชการเฉลิมพระเกียรติ', 'โทรคมนาคม', 'หลักสี่', 
        'ราชภัฎพระนครเหนือ', 'วัดพระศรีมหาธาตุ', 'รามอินทรา 3', 'ลาดปลาเค้า', 'รามอินทรา กม.4', 'มัยลาภ', 'วัชรพล', 
        'รามอินทรา กม.6', 'คู้บอน', 'รามอินทรา กม.9', 'วงแหวนรามอินทรา', 'นพรัตน์', 'บางชัน', 'เศรษบุตรบำเพ็ญ', 
        'ตลาดมีนบุรี', 'มีนบุรี']);
    } else if (selectedLine === 'yellow') {
        populateStations(stationsSelect,
        ['ลาดพร้าว', 'ภาวนา', 'โชคชัย 4', 'ลาดพร้าว 71', 'ลาดพร้าว 83', 'มหาดไทย', 'ลาดพร้าว 101', 'บางกะปิ', 
        'แยกลำสาลี', 'ศรีกรีฑา', 'หัวหมาก', 'กลันตัน', 'ศรีนุช', 'ศรีนครินทร์ 38', 'สวนหลวง ร.9', 'ศรีอุดม', 'ศรีเอี่ยม', 
        'ศรีลาซาล', 'ศรีแบริ่ง', 'ศรีด่าน', 'ศรีเทพา', 'ทัพวัล', 'สำโรง']);
    } else if (selectedLine === 'blue') {
        populateStations(stationsSelect,
        ['หลักสอง', 'บางแค', 'ภาษีเจริญ', 'เพชรเกษม 48', 'บางหว้า', 'บางไผ่', 'ท่าพระ', 'จรัญฯ 13', 'ไฟฉาย', 
        'บางขุนนนท์', 'บางยี่ขัน', 'สิรินธร', 'บางพลัด', 'บางอ้อ', 'บางโพ', 'เตาปูน', 'บางซี่อ', 'กำแพงเพชร', 'สวนจตุจักร', 
        'ลาดพร้าว', 'รัชดาภิเษก', 'สุทธิสาร', 'ห้วยขวาง', 'ศูนย์วัฒนธรรมแห่งประเทศไทย', 'พระราม 9', 'เพชรบุรี', 'สุขุมวิท', 
        'พร้อมพงษ์', 'ศูนย์ประชุมแห่งชาติสิริกิติ์', 'คลองเตย', 'ลุมพินี', 'สีลม', 'สามย่าน', 'หัวลำโพง', 'วัดมังกร', 'สามยอด', 
        'สนามไชย', 'อิสรภาพ']);
    } else if (selectedLine === 'purple') {
        populateStations(stationsSelect,
        ['คลองบางไผ่', 'ตลาดบางใหญ่', 'สามแยกบางใหญ่', 'บางพลู', 'บางรักใหญ่', 'บางรักน้อยท่าอิฐ', 'ไทรม้า', 'สะพานพระนั่งเหล้า', 
        'แยกนนทบุรี 1', 'บางกระสอ', 'ศูนย์ราชการนนทบุรี', 'กระทรวงสาธารณสุข', 'แยกติวานนท์', 'วงศ์สว่าง', 'บางซ่อน', 'เตาปูน']);
    } else if (selectedLine === 'airportlink') {
        populateStations(stationsSelect,
        ['พญาไท', 'ราชปรารภ', 'มักกะสัน', 'รามคำแหง', 'หัวหมาก', 'บ้านทับช้าง', 'ลาดกระบัง', 'สุวรรณภูมิ']);
    } else if (selectedLine === 'red') {
        populateStations(stationsSelect,
        ['ตลิ่งชัน', 'บางบำหรุ', 'บางกรวย', 'สะพานพระราม 6', 'บางซ่อน', 'สถานีกลางกรุงเทพอภิวัฒน์', 'จตุจักร', 'วัดเสมียนนารี', 
        'บางเขน', 'ทุ่งสองห้อง', 'หลักสี่', 'การเคหะฯ', 'ดอนเมือง', 'หลักหก', 'รังสิต']);
    } else {
        hideStations();
    }
});

document.getElementById('lines_2').addEventListener('change', function () {
    var selectedLine = this.value;
    var stationsSelect = document.getElementById('stations_2');
    var stationsList = document.getElementById('stations-list_2');

    stationsList.innerHTML = '';

    if (selectedLine === "sukhumvit") {
        populateStations(stationsSelect,
        ['คูคต', 'แยก คปอ', 'พิพิธภัณฑ์กองทัพอากาศ', 'โรงพยาบาลภูมิพลอดุลยเดช', 
        'สะพานใหม่', 'สายหยุด', 'พหลโยธิน 59', 'วัดพระศรีมหาธาตุ', 'กรมทหารราบที่ 11', 
        'บางบัว', 'กรมป่าไม้', 'มหาวิทยาลัยเกษตรศาสตร์', 'เสนานิคม', 'รัชโยธิน', 'พหลโยธิน 24', 
        'ห้าแยกลาดพร้าว', 'หมอชิต', 'สะพานควาย', 'เสนาร่วม', 'อารีย์', 'สนามเป้า', 'อนุสาวรีย์ชัยสมรภูมิ', 
        'พญาไท', 'ราชเทวี', 'สยาม', 'ชิดลม', 'เพลินจิต', 'นานา', 'อโศก', 'พร้อมพงษ์', 'ทองหล่อ', 
        'เอกมัย', 'พระโขนง', 'อ่อนนุช', 'บางจาก', 'ปุณณวิถี', 'อุดมสุข', 'บางนา', 'แบริ่ง', 'สำโรง', 
        'ปู่เจ้า', 'ช้างเอราวัณ', 'โรงเรียนนายเรือ', 'ปากน้ำ', 'ศรีนครินทร์', 'แพรกษา', 'สายลวด', 'เคหะฯ']);
    } else if (selectedLine === 'silom') {
        populateStations(stationsSelect,
        ['บางหว้า สายฟ้า', 'วุฒากาศ', 'ตลาดพลู', 'โพธิ์นิมิตร', 'วงเวียนใหญ่', 'กรุงธนบุรี', 'สะพานตากสิน', 
        'สุรศักดิ์', 'เซนต์หลุยส์', 'ช่องนนทรี', 'ศาลาแดง', 'ราชดำริ', 'สยาม', 'สนามกีฬาแห่งชาติ']);
    } else if (selectedLine === 'gold') {
        populateStations(stationsSelect,
        ['คลองสาน','เจริญนคร','กรุงธนบุรี']);
    } else if (selectedLine === 'pink') {
        populateStations(stationsSelect,
        ['ศูนย์ราชการนนทบุรี', 'แคราย', 'สนามบินน้ำ', 'สามัคคี', 'กรมชลประทาน', 'แยกปากเกร็ด', 'เลี่ยงเมืองปากเกร็ด', 
        'แจ้งวัฒนะปากเกร็ด 28', 'เมืองทองธานี', 'แจ้งวัฒนะ 14', 'ศูนย์ราชการเฉลิมพระเกียรติ', 'โทรคมนาคม', 'หลักสี่', 
        'ราชภัฎพระนครเหนือ', 'วัดพระศรีมหาธาตุ', 'รามอินทรา 3', 'ลาดปลาเค้า', 'รามอินทรา กม.4', 'มัยลาภ', 'วัชรพล', 
        'รามอินทรา กม.6', 'คู้บอน', 'รามอินทรา กม.9', 'วงแหวนรามอินทรา', 'นพรัตน์', 'บางชัน', 'เศรษบุตรบำเพ็ญ', 
        'ตลาดมีนบุรี', 'มีนบุรี']);
    } else if (selectedLine === 'yellow') {
        populateStations(stationsSelect,
        ['ลาดพร้าว', 'ภาวนา', 'โชคชัย 4', 'ลาดพร้าว 71', 'ลาดพร้าว 83', 'มหาดไทย', 'ลาดพร้าว 101', 'บางกะปิ', 
        'แยกลำสาลี', 'ศรีกรีฑา', 'หัวหมาก', 'กลันตัน', 'ศรีนุช', 'ศรีนครินทร์ 38', 'สวนหลวง ร.9', 'ศรีอุดม', 'ศรีเอี่ยม', 
        'ศรีลาซาล', 'ศรีแบริ่ง', 'ศรีด่าน', 'ศรีเทพา', 'ทัพวัล', 'สำโรง']);
    } else if (selectedLine === 'blue') {
        populateStations(stationsSelect,
        ['หลักสอง', 'บางแค', 'ภาษีเจริญ', 'เพชรเกษม 48', 'บางหว้า', 'บางไผ่', 'ท่าพระ', 'จรัญฯ 13', 'ไฟฉาย', 
        'บางขุนนนท์', 'บางยี่ขัน', 'สิรินธร', 'บางพลัด', 'บางอ้อ', 'บางโพ', 'เตาปูน', 'บางซี่อ', 'กำแพงเพชร', 'สวนจตุจักร', 
        'ลาดพร้าว', 'รัชดาภิเษก', 'สุทธิสาร', 'ห้วยขวาง', 'ศูนย์วัฒนธรรมแห่งประเทศไทย', 'พระราม 9', 'เพชรบุรี', 'สุขุมวิท', 
        'พร้อมพงษ์', 'ศูนย์ประชุมแห่งชาติสิริกิติ์', 'คลองเตย', 'ลุมพินี', 'สีลม', 'สามย่าน', 'หัวลำโพง', 'วัดมังกร', 'สามยอด', 
        'สนามไชย', 'อิสรภาพ']);
    } else if (selectedLine === 'purple') {
        populateStations(stationsSelect,
        ['คลองบางไผ่', 'ตลาดบางใหญ่', 'สามแยกบางใหญ่', 'บางพลู', 'บางรักใหญ่', 'บางรักน้อยท่าอิฐ', 'ไทรม้า', 'สะพานพระนั่งเหล้า', 
        'แยกนนทบุรี 1', 'บางกระสอ', 'ศูนย์ราชการนนทบุรี', 'กระทรวงสาธารณสุข', 'แยกติวานนท์', 'วงศ์สว่าง', 'บางซ่อน', 'เตาปูน']);
    } else if (selectedLine === 'airportlink') {
        populateStations(stationsSelect,
        ['พญาไท', 'ราชปรารภ', 'มักกะสัน', 'รามคำแหง', 'หัวหมาก', 'บ้านทับช้าง', 'ลาดกระบัง', 'สุวรรณภูมิ']);
    } else if (selectedLine === 'red') {
        populateStations(stationsSelect,
        ['ตลิ่งชัน', 'บางบำหรุ', 'บางกรวย', 'สะพานพระราม 6', 'บางซ่อน', 'สถานีกลางกรุงเทพอภิวัฒน์', 'จตุจักร', 'วัดเสมียนนารี', 
        'บางเขน', 'ทุ่งสองห้อง', 'หลักสี่', 'การเคหะฯ', 'ดอนเมือง', 'หลักหก', 'รังสิต']);
    } else {
        hideStations();
    }
});
function populateStations(select, stationNames) {
    select.innerHTML = '';

    stationNames.forEach(function (stationName) {
        var option = document.createElement('option');
        option.value = stationName.toLowerCase().replace(/\s/g, '_');
        option.textContent = stationName;
        select.appendChild(option);
    });

    document.getElementById('stations-container').style.display = 'block';
}

const stationSearch = document.getElementById('stationSearch');
const stationsSelect = document.getElementById('stations');

stationSearch.addEventListener('input', () => {
    const searchTerm = stationSearch.value.toLowerCase();

    Array.from(stationsSelect.options).forEach(option => {
        if (option.value.toLowerCase().includes(searchTerm)) {
            option.style.display = 'block';
        } else {
            option.style.display = 'none';
        }
    });
});

const stationSearch_2 = document.getElementById('stationSearch_2');
const stationsSelect_2 = document.getElementById('stations_2');

stationSearch_2.addEventListener('input', () => {
    const searchTerm_2 = stationSearch_2.value.toLowerCase();

    Array.from(stationsSelect_2.options).forEach(option => {
        if (option.value.toLowerCase().includes(searchTerm_2)) {
            option.style.display = 'block';
        } else {
            option.style.display = 'none';
        }
    });
});

