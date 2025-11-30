//Fix the code so that each API fetch logs the correct URL and data

//The issue was that var is function-scoped, so i ended up being the final value (urls.length) in all
//.then callbacks. Using let fixes it because it is block-scoped and preserves the correct value.
function fetchData(urls) {
    for (let i = 0; i < urls.length; i++) { 
        fetch(urls[i])
            .then(response => response.json())
            .then(data => console.log('Data from', urls[i], data));
    }
}

fetchData(['api/1', 'api/2', 'api/3']);

