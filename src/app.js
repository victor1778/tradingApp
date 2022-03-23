const tickers = document.getElementById('tickers')

console.log(tickers)

const getData = () => {
    fetch('http://127.0.0.1:8000/get', {
        method: 'GET'
    })
    .then(resp => resp.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))
}

getData()

