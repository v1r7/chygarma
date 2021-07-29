'use strict';

const searchInput = document.getElementById('verse_search_input_id');
const searchInputBlock = document.getElementById('verse_search_input_block_id');


searchInput.onkeyup = (event) => {
  if (event.currentTarget.value.length > 2) {
    const data = {value: event.currentTarget.value};
    console.log(data);

    fetch(allVerseSearchUrl, {
      method: 'POST',
      headers: {
        'Content-type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(responseJSON => {
      searchInputBlock.innerHTML = responseJSON['html'];
    })
  }
}