// // js for upload pictures
// const backgroundBtn = document.getElementById('background_photo');
//
// backgroundBtn.onclick = () => {
//   fetch("https://theplantaeapi.herokuapp.com/api/v1/id", {
//         method: "POST",
//         headers: {'Content-Type': 'application/json'},
//         body: JSON.stringify(this.state.queryImage)
// })
// .then(res => res.json())
// .then(data => {
//     document.location.href = responseJSON['success_url'];
//
//      })
//    }

   // js for verse
// const categorySelect = document.getElementById('.block-description-select-id');
// categorySelect.addEventListener('change', (event) => {
//   const result = document.getElementById('.result');
//   result.textContent = `You like ${event.target.value}`;
// });
// console.log(categorySelect);
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
      // category: categorySelect,
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