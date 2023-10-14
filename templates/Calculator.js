document.getElementById('lines').addEventListener('change', function () {
    var selectedLine = this.value;
    var stationsSelect = document.getElementById('stations');
    var stationsList = document.getElementById('stations-list');

    // Clear existing stations
    stationsList.innerHTML = '';

    // Add stations dynamically based on the selected line
    if (selectedLine === "sukhumvit") {
        populateStations(stationsSelect, 
        ['คูคต', 'แยก คปอ', 'พิพิธภัณฑ์กองทัพอากาศ', 'โรงพยาบาลภูมิพลอดุลยเดช', 
        'สะพานใหม่', 'สายหยุด', 'พหลโยธิน 59', 'วัดพระศรีมหาธาตุ', 'กรมทหารราบที่ 11', 
        'บางบัว', 'กรมป่าไม้', 'มหาวิทยาลัยเกษตรศาสตร์', 'เสนานิคม', 'รัชโยธิน', 'พหลโยธิน 24', 
        'ห้าแยกลาดพร้าว', 'หมอชิต', 'สะพานควาย', 'เสนาร่วม', 'อารีย์', 'สนามเป้า', 'อนุสาวรีย์ชัยสมรภูมิ', 
        'พญาไทย', 'ราชเทวี', 'สยาม', 'ชิดลม', 'เพลินจิต', 'นานา', 'อโศก', 'พร้อมพงษ์', 'ทองหล่อ', 
        'เอกมัย', 'พระโขนง', 'อ่อนนุช', 'บางจาก', 'ปุณณวิถี', 'อุดมสุข', 'บางนา', 'แบริ่ง', 'สำโรง', 
        'ปู่เจ้า', 'ช้างเอราวัณ', 'โรงเรียนนายเรือ', 'ปากน้ำ', 'ศรีนครินทร์', 'แพรกษา', 'สายลวด', 'เคหะฯ']);
    } else if (selectedLine === 'silom') {
        populateStations(stationsSelect, 
        ['บางหว้า สายฟ้า', 'วุฒากาศ', 'ตลาดพลู', 'โพธิ์นิมิตร', 'วงเวียนใหญ่', 'กรุงธนบุรี', 'สะพานตากสิน', 
        'สุรศักดิ์', 'เซนต์หลุยส์', 'ช่องนนทรี', 'ศาลาแดง', 'ราชดำริ', 'สยาม', 'สนามกีฬาแห่งชาติ']);
    } else if (selectedLine === 'Gold Line') {
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
    } else if (selectedLine === 'Gold Line') {
        populateStations(stationsSelect,
        ['คลองสาน','เจริญนคร','กรุงธนบุรี']);
    } else if (selectedLine === 'Gold Line') {
        populateStations(stationsSelect,
        ['คลองสาน','เจริญนคร','กรุงธนบุรี']);
    } else if (selectedLine === 'Gold Line') {
        populateStations(stationsSelect,
        ['คลองสาน','เจริญนคร','กรุงธนบุรี']);
    } else {
        hideStations();
    }
});

function populateStations(select, stationNames) {
    // Clear existing options
    select.innerHTML = '';

    stationNames.forEach(function (stationName) {
        var option = document.createElement('option');
        option.value = stationName.toLowerCase().replace(/\s/g, '_');
        option.textContent = stationName;
        select.appendChild(option);
    });

    document.getElementById('stations-container').style.display = 'block';
}

