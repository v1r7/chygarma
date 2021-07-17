'use strict';
const registerBtn = document.getElementById('register_btn_id');
console.log(registerBtn)

registerBtn.onclick = (event) => {
  event.preventDefault();

  const firstName = document.getElementById('first_name_id').value;
  const firstNameErr = document.getElementById('first_name_error_id');
  const lastName = document.getElementById('last_name_id').value;
  const lastNameErr = document.getElementById('last_name_error_id');
  const email = document.getElementById('email_id').value;
  const emailErr = document.getElementById('email_error_id');
  const login = document.getElementById('login_id').value;
  const loginErr = document.getElementById('login_error_id');
  const pass1 = document.getElementById('pass_1_id').value;
  const passOneErr = document.getElementById('pass_1_error_id');
  console.log(firstName);
  console.log(lastName);
  console.log(pass1);

  let registerFieldsStatus = [
    {firstName: false},
    {lastName: false},
    {email: false},
    {login: false},
    {pass1: false},
  ]
  console.log(registerFieldsStatus);

  if (firstName === '') {
    firstNameErr.style.display = 'block';
    registerFieldsStatus[0].firstName = false;
  } else {
    firstNameErr.style.display = 'none';
    registerFieldsStatus[0].firstName = true;
  }

  if (lastName === '') {
    lastNameErr.style.display = 'block';
    registerFieldsStatus[1].lastName = false;
  } else {
    lastNameErr.style.display = 'none';
    registerFieldsStatus[1].lastName = true;
  }

  if (email === '') {
    emailErr.style.display = 'block';
    registerFieldsStatus[2].email = false;
  } else {
    emailErr.style.display = 'none';
    registerFieldsStatus[2].email = true;
  }

    if (login === '') {
    loginErr.style.display = 'block';
    registerFieldsStatus[3].login = false;
  } else {
    loginErr.style.display = 'none';
    registerFieldsStatus[3].login = true;
  }

  if (pass1 === '') {
    passOneErr.style.display = 'block';
    registerFieldsStatus[4].pass1 = false;
  } else {
    passOneErr.style.display = 'none';
    registerFieldsStatus[4].pass1 = true;
  }


  if (registerFieldsStatus[0].firstName && registerFieldsStatus[1].lastName &&
      registerFieldsStatus[2].email && registerFieldsStatus[3].login && registerFieldsStatus[4].pass1)

  {
    let data = {
      first_name: firstName,
      last_name: lastName,
      email: email,
      login: login,
      pass1: pass1,
    }

    console.log(data);

    fetch(registerUrl, {
      method: 'POST',
      headers: {
        'Accept': 'application/json, */*, text/plain',
        'Content-type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
      },
      body: JSON.stringify(data),
    })
    .then((response) => response.json())
    .then(responseJSON => {
      if (responseJSON['status'] === 400) {
        registerErrorBlock.innerHTML = responseJSON['message'];
        registerErrorBlock.style.display = 'block';
      } else {
        document.location.href = responseJSON['success_url'];
      }
    })
  }

}