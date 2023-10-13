const wrapper = document.querySelector(".wrapper"),
selectBtn = wrapper.querySelector(".select-btn"),
searchInp = wrapper.querySelector("input"),
options = wrapper.querySelector(".options");

let train_line = ["Green Line (Sukhumvit Line)", "Green Line (Silom Line)", "Gold Line", "Pink Line", "Yellow Line", "Blue Line", "Purple Line",
                 "Airport Rail Link", "Red Line"];

function add_line(selected_line) {
    options.innerHTML = "";
    train_line.forEach(line => {
        let isSelected = line == selected_line ? "selected" : "";
        let li = `<li onclick="updateName(this)" class="${isSelected}">${line}</li>`;
        options.insertAdjacentHTML("beforeend", li);
    });
}
add_line();

function updateName(selectedLi) {
    searchInp.value = "";
    add_line(selectedLi.innerText);
    wrapper.classList.remove("active");
    selectBtn.firstElementChild.innerText = selectedLi.innerText;
}

searchInp.addEventListener("keyup", () => {
    let arr = [];
    let searchWord = searchInp.value.toLowerCase();
    arr = train_line.filter(data => {
        return data.toLowerCase().startsWith(searchWord);
    }).map(data => {
        let isSelected = data == selectBtn.firstElementChild.innerText ? "selected" : "";
        return `<li onclick="updateName(this)" class="${isSelected}">${data}</li>`;
    }).join("");
    options.innerHTML = arr ? arr : `<p style="margin-top: 10px;">Oops! your train line not found</p>`;
});

selectBtn.addEventListener("click", () => wrapper.classList.toggle("active"));

document.getElementById('lines').addEventListener('change', function () {
    var selectedLine = this.value;
    var stationsSelect = document.getElementById('stations');
    var stationsList = document.getElementById('stations-list');

    // Clear existing stations
    stationsList.innerHTML = '';

    // Add stations dynamically based on the selected line
    if (selectedLine === "Green Line (Sukhumvit Line)") {
        populateStations(stationsSelect, 
        ['คูคต', 'แยก คปอ', 'พิพิธภัณฑ์กองทัพอากาศ', 'โรงพยาบาลภูมิพลอดุลยเดช', 
        'สะพานใหม่', 'สายหยุด', 'พหลโยธิน 59', 'วัดพระศรีมหาธาตุ', 'กรมทหารราบที่ 11', 
        'บางบัว', 'กรมป่าไม้', 'มหาวิทยาลัยเกษตรศาสตร์', 'เสนานิคม', 'รัชโยธิน', 'พหลโยธิน 24', 
        'ห้าแยกลาดพร้าว', 'หมอชิต', 'สะพานควาย', 'เสนาร่วม', 'อารีย์', 'สนามเป้า', 'อนุสาวรีย์ชัยสมรภูมิ', 
        'พญาไทย', 'ราชเทวี', 'สยาม', 'ชิดลม', 'เพลินจิต', 'นานา', 'อโศก', 'พร้อมพงษ์', 'ทองหล่อ', 
        'เอกมัย', 'พระโขนง', 'อ่อนนุช', 'บางจาก', 'ปุณณวิถี', 'อุดมสุข', 'บางนา', 'แบริ่ง', 'สำโรง', 
        'ปู่เจ้า', 'ช้างเอราวัณ', 'โรงเรียนนายเรือ', 'ปากน้ำ', 'ศรีนครินทร์', 'แพรกษา', 'สายลวด', 'เคหะฯ']);
    } else if (selectedLine === 'Green Line (Silom Line)') {
        populateStations(stationsSelect, 
        ['บางหว้า สายฟ้า', 'วุฒากาศ', 'ตลาดพลู', 'โพธิ์นิมิตร', 'วงเวียนใหญ่', 'กรุงธนบุรี', 'สะพานตากสิน', 
        'สุรศักดิ์', 'เซนต์หลุยส์', 'ช่องนนทรี', 'ศาลาแดง', 'ราชดำริ', 'สยาม', 'สนามกีฬาแห่งชาติ']);
    } else if (selectedLine === 'Pink Line') {
        populateStations(stationsSelect,
        ['ศูนย์ราชการนนทบุรี', 'แคราย', 'สนามบินน้ำ', 'สามัคคี', 'กรมชลประทาน', 'แยกปากเกร็ด', 'เลี่ยงเมืองปากเกร็ด', 
        'แจ้งวัฒนะปากเกร็ด 28', 'เมืองทองธานี', 'แจ้งวัฒนะ 14', 'ศูนย์ราชการเฉลิมพระเกียรติ', 'โทรคมนาคม', 'หลักสี่', 
        'ราชภัฎพระนครเหนือ', 'วัดพระศรีมหาธาตุ', 'รามอินทรา 3', 'ลาดปลาเค้า', 'รามอินทรา กม.4', 'มัยลาภ', 'วัชรพล', 
        'รามอินทรา กม.6', 'คู้บอน', 'รามอินทรา กม.9', 'วงแหวนรามอินทรา', 'นพรัตน์', 'บางชัน', 'เศรษบุตรบำเพ็ญ', 
        'ตลาดมีนบุรี', 'มีนบุรี']);
    } else if (selectedLine === 'Yellow Line') {
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
    } else if (selectedLine === 'Gold Line') {
        populateStations(stationsSelect,
        ['คลองสาน','เจริญนคร','กรุงธนบุรี']);
    } else {
        hideStations();
    }
});

document.getElementById('stations').addEventListener('change', function () {
    var selectedStation = this.value;
    alert('You selected: ' + selectedStation);
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

// แก้ไขฟังก์ชัน hideStations เป็นแบบไม่ซ่อนองค์ประกอบแต่ละครั้ง
function hideStations() {
    document.getElementById('stations-container').style.display = 'none';
}
