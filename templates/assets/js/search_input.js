'use strict';


const searchInput = document.getElementById('search_input_id');
const searchInputBlock = document.getElementById('search_input_block_id');
console.log(searchInputBlock);

searchInput.onkeyup = (event) => {
  if (event.currentTarget.value.length > 2) {
    const data = {value: event.currentTarget.value};

    fetch(verseSearchUrl, {
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
      searchInputBlock.innerHTML = responseJSON['html'];
    })
  }
}