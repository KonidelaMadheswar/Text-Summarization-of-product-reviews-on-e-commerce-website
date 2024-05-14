function displayResults() {
    const productName = document.querySelector('.searchTerm').value;
    const amazonResult = document.createElement('div');
    amazonResult.className = 'result';
    amazonResult.innerText = `Amazon: Search results for ${productName}`;
    const flipkartResult = document.createElement('div');
    flipkartResult.className = 'result';
    flipkartResult.innerText = `Flipkart: Search results for ${productName}`;
    const resultContainer = document.querySelector('.wrap');
    resultContainer.appendChild(amazonResult);
    resultContainer.appendChild(flipkartResult);
}
