let input = document.querySelector("#input");
let submit = document.querySelector(".submit");

function getValue() {
  let submitValue = input.value;
  document.location.href = "/square/" + Number(submitValue);
}

submit.addEventListener("click", getValue);
