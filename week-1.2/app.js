  //獲取當前螢幕解析度
// console.log(winWide)
// let wideScreen = false;
let mn = document.querySelector(".active");
document.addEventListener("click",clickHidden);

window.addEventListener("resize",function(wide){
    winWide = window.innerWidth;
    let mn = document.querySelector(".active");
    
    if (winWide <= 600){
        mn.style.transform="scaleX(0)";
    }else{
        mn.style.transform="scaleX(1)";
    }
});

winWide = window.innerWidth;
console.log(winWide)
function clickHidden(eve){
    if(winWide <= 600){        
        if (eve.target.tagName == "LI" || eve.target.tagName == "INPUT" || eve.target.tagName == "UL"){
                mn.style.transform="scaleX(1)";
                console.log("pass");
        }else{
            mn.style.transform="scaleX(0)";
        }            
    }

}


// document.addEventListener("click",clickHidden);
// let mn = document.querySelector(".active");
// function clickHidden(eve){
//     // console.log(eve.target.className, eve.target.tagName)
//     if(winWide <= 600){ 
//         if (eve.target.tagName == "LI" || eve.target.tagName == "INPUT" || eve.target.tagName == "UL"){
//             mn.style.transform="scaleX(1)";
//             console.log("pass");
//         }

        
//     }
// }







