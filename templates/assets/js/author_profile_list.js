let testBool  = true;
        function toggle() {
            testBool = testBool  ? false : true;
            console.log(testBool);
            let data = {
                like: testBool,
                author_id: authorId,
            };
            fetch(authorDetailUrl, {
              method: 'POST',
              headers: {
                'Accept': 'application/json, */*, text/plain',
                'Content-type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
              },
              body: JSON.stringify(data)
            })
            .then(response => response.json())
}

