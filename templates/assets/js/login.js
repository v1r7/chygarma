'use strict';
const loginBtn = document.getElementById('login_btn_id');
const loginErrorBlock = document.getElementById('login_error_block_id');


loginBtn.onclick = (event) => {
  event.preventDefault();

  const login = document.getElementById('id_login').value;
  const password = document.getElementById('id_password').value;

  const data = {
    login: login,
    password: password,
  }
  console.log(data);

  fetch(loginUrl, {
    method: 'POST',
    headers: {
      'Accept': 'application/json, text/plain, */*',
      'Content-type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify(data)
  })
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw Error(response.statusText);
    }
  })
  .then(responseJSON => {
    document.location.href = responseJSON['success_url'];
  })
  .catch(error => {
    loginErrorBlock.style.display = 'block';
  })
}