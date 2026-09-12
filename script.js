const form = document.getElementById("shortener-form");

const result = document.getElementById("result");
const shortUrl = document.getElementById("short-url");

const copyButton = document.getElementById("copy-button");


form.addEventListener("submit", function(event) {

    event.preventDefault();

    // Temporary result.
    // Python will eventually provide the real shortened URL.

    shortUrl.textContent = "https://short.ly/example";

    result.style.display = "flex";

});


copyButton.addEventListener("click", function() {

    navigator.clipboard.writeText(shortUrl.textContent);

    copyButton.textContent = "Copied!";

    setTimeout(function() {
        copyButton.textContent = "Copy";
    }, 1500);

});