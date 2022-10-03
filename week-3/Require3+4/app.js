//讀資料&換圖換字
let allLength = 0;
function changeForm() {
  let allImg = document.querySelectorAll("img.change");
  let allP = document.querySelectorAll(".second p");

  fetch(
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
  )
    .then(function (response) {
      return response.json(); //因為拿到的資料是JSON，所以要用.json來解讀他
    })
    .then(function (data) {
      let list = data["result"]["results"];
      allLength = list.length;
      for (let i = 0; i < allImg.length; i++) {
        //   console.log(list[i]["file"].toLowerCase().split(".jpg")[0] + ".jpg");
        let oldImg = allImg[i];
        let imgParent = oldImg.parentNode;
        let newImg = document.createElement("img");
        newImg.classList.add("change");
        newImg.src = list[i]["file"].toLowerCase().split(".jpg")[0] + ".jpg";
        imgParent.replaceChild(newImg, oldImg);

        // console.log(data["result"]["results"][0]);
        let oldP = allP[i];
        let pParent = oldP.parentNode;
        let newP = document.createElement("p");
        let newP_content = document.createTextNode(list[i].stitle);
        newP.appendChild(newP_content);
        pParent.replaceChild(newP, oldP);
      }
    });
  //   return allImg.length;
}
changeForm();

//載入更多

let loadButton = document.querySelector(".button button");
let allImg = document.querySelectorAll("img.change");
loadButton.addEventListener("click", loadMore);
function loadMore() {
  let form = document.querySelector(".mid");
  for (let i = 0; i < 8; i++) {
    // 增新div
    let newDiv = document.createElement("div");
    newDiv.classList.add("content");
    form.appendChild(newDiv);
    // 增新圖片
    let newImg = document.createElement("img");
    newImg.classList.add("change");
    newImg.src = "";
    newDiv.appendChild(newImg);
    // 增新文字
    let newP = document.createElement("p");
    newDiv.appendChild(newP);
    allImg = document.querySelectorAll("img.change");
  }

  if (allImg.length == allLength) {
    loadButton.style.display = "none";
  }
  changeForm();
}

//漢堡選單
let mn = document.querySelector(".active");
document.addEventListener("click", clickHidden);

window.addEventListener("resize", function (wide) {
  console.log("resize");
  winWide = window.innerWidth;
  let mn = document.querySelector(".active");

  if (winWide <= 600) {
    mn.style.transform = "scaleX(0)";
  } else {
    mn.style.transform = "scaleX(1)";
  }
});

winWide = window.innerWidth;
// console.log(winWide);
function clickHidden(eve) {
  if (winWide <= 600) {
    if (
      eve.target.tagName == "LI" ||
      eve.target.tagName == "INPUT" ||
      eve.target.tagName == "UL"
    ) {
      mn.style.transform = "scaleX(1)";
      console.log("pass");
    } else {
      mn.style.transform = "scaleX(0)";
    }
  }
}
