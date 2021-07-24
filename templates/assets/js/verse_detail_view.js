const commentInput = document.getElementById('comment_input_id');
const sendCommentBtn = document.getElementById('comment_btn_id');
const commentErrorBLock = document.getElementById('comment_error_id');

sendCommentBtn.onclick = (event) => {
  if (commentInput.value.length > 3) {
    const data = {
      comment: commentInput.value,
      verse_id: verseId,
    };

    fetch(verseDetailUrl, {
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