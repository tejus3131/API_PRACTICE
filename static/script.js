function addExtensions() {
    var scriptElement = document.createElement('script');
    var linkElement = document.createElement('link');
    linkElement.rel = 'stylesheet';
    linkElement.href = 'https://api-practice-wine.vercel.app/static/styles.css';
    scriptElement.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
    scriptElement.onload = function () {
        document.body.innerHTML = '<h1>API Page</h1><div id="content"></div>';
        one();
    };
    document.head.appendChild(linkElement);
    document.head.appendChild(scriptElement);
}

function one() {
    $.ajax({
        url: 'https://api-practice-wine.vercel.app/api',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ "value": "one" }),
        success: function (response) {
            $('#content').html(response.page);
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function two() {
    $.ajax({
        url: 'https://api-practice-wine.vercel.app/api',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ "value": "two" }),
        success: function (response) {
            $('#content').html(response.page);
        },
        error: function (error) {
            console.log(error);
        }
    });
}

addExtensions();
