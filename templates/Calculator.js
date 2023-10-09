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