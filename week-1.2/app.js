document.addEventListener("click",clickHidden);
let label = document.querySelector("label");
let mn = document.querySelector(".active");

function clickHidden(eve){
    console.log(eve.target.className, eve.target.tagName)

    if (eve.target.tagName == "LI" || eve.target.tagName == "INPUT" || eve.target.tagName == "UL"){
        mn.style.transform="scaleX(1)"
        console.log("pass")
    }

    else{
        mn.style.transform="scaleX(0)"
    }
}