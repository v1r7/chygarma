'use strict';

const searchInput = document.getElementById('author_search_input_id');
const searchInputBlock = document.getElementById('author_search_input_block_id');

searchInput.onkeyup = (event) => {
  if (event.currentTarget.value.length > 2) {
    const data = {value: event.currentTarget.value};

    fetch(authorSearchUrl, {
      method: 'POST',
      headers: {
        'Accept': 'application/json, */*, text/plain',
        'Content-type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
      },
      body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(responseJSON => {
      searchInputBlock.innerHTML = responseJSON['html'];
    })
  }
}