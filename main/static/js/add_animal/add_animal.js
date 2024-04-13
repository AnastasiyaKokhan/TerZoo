const animalForm = document.querySelector("#add_animal_form")
const animalButton = document.querySelector("#add_animal_button")

animalButton.addEventListener("click", sendData)
function sendData() {
    let data = new FormData(animalForm)
    fetch(`http://127.0.0.1:8000/api/add_animal/`, {
        method: "POST", headers: {
            "X-SCRFToken": getCookie("csrftoken"),
        }, body: data,
    })
    .then((resp) => resp.json())
    .then((data) => {
        console.log(data)
    })
}

function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}
