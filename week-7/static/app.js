// serch name
show_name = () => {
  let get_username = document.querySelector("#serch");
  let get_previous_data = document.querySelector(".showing_name");
  if (get_previous_data != null) {
    get_previous_data.remove();
  }
  username = get_username.value;

  fetch(`/api/member?username=${username}`)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      data = data["data"];
      if (data == null) {
        serch_name = "查無此人";
      } else {
        id = data["id"];
        name = data["name"];
        username = data["username"];
        serch_name = `${name} (${username})`;
      }
      let serch_div = document.querySelector(".serch");
      let newP = document.createElement("p");
      newP.classList.add("showing_name");
      let newP_content = document.createTextNode(serch_name);
      serch_div.appendChild(newP);
      newP.appendChild(newP_content);
    });
};
let show_bottun = document.querySelector("#serch_button");
show_bottun.addEventListener("click", show_name);

//update name
update_name = () => {
  let get_newname = document.querySelector("#change");
  let get_previous_data = document.querySelector(".showing_mes");
  if (get_previous_data != null) {
    get_previous_data.remove();
  }
  newname = get_newname.value;

  fetch("/api/member", {
    method: "PATCH",
    body: JSON.stringify({
      name: newname,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      let change_div = document.querySelector(".change");
      let new_p = document.createElement("p");
      let new_p_content = document.createTextNode("更新成功");
      new_p.classList.add("showing_mes");
      change_div.appendChild(new_p);
      new_p.appendChild(new_p_content);

      let head_div = document.querySelector(".head");
      let head_name = document.querySelector(".head p");
      let new_head_name = document.createElement("p");
      let new_head_name_content = document.createTextNode(
        `${newname}，歡迎登入系統`
      );
      new_head_name.appendChild(new_head_name_content);
      head_div.replaceChild(new_head_name, head_name);
    });
};

let update_bottun = document.querySelector("#change_button");
update_bottun.addEventListener("click", update_name);
