'use strict';

const searchInput = document.getElementById('author_search_input_id');
const searchInputBlock = document.getElementById('author_search_input_block_id');

searchInput.onkeyup = (event) => {
  if (event.currentTarget.value.length > 2) {
    const data = {value: event.currentTarget.value};
    console.log(data);

    fetch(authorSearchUrl, {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(responseJSON => {
      searchInputBlock.innerHTML = responseJSON['html'];
    })
  }
}