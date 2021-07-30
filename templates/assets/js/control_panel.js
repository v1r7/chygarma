'use strict'

// const btncom = document.querySelector('#input__file-com')
// btncom.onchange = (e) => {
//     readURLcom(e.target)
// }
//
// let pictureInput = null;
// function readURLcom(btncom) {
//     if (btncom.files && btncom.files[0]) {
//         let old = new FileReader();
//         old.onload = function (e) {
//             pictureInput(e.target.result);
//             console.log(e.target.result);
//             block.style.background = `url(${e.target.result})`;
//             block.style.backgroundSize = `cover`;
//         };
//
//         old.readAsDataURL(btncom.files[0]);
//     }
// }
'use strict'



let categorySelectId = null;

function showOptions(s) {
  categorySelectId = parseInt(s[s.selectedIndex].id, 10); // get category id
}

const nameInput = document.getElementById('name_input_id');
const contentInput = document.getElementById('content_input_id');
const descriptionInput = document.getElementById('description_input_id');
const tagsInput = document.getElementById('tags_input_id');
const sendVerseBtn = document.getElementById('verse_btn_id');
const commentErrorBLock = document.getElementById('verse_error_id');

sendVerseBtn.onclick = (event) => {
  if (contentInput.value.length > 2) {
    const data = {
      name: nameInput.value,
      content: contentInput.value,
      description: descriptionInput.value,
      category_id: categorySelectId,
      tag: tagsInput.value,
      author_id: AuthorId,
    };

    fetch(verseCreateUrl, {
      method: 'POST',
      headers: {
        'Accept': 'application/json, */*, text/plain',
        'Content-type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(responseJSON => {
      document.location.reload();
    })
  } else {
    commentErrorBLock.style.display = 'block';
  }
}