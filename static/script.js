function one() {
    $.ajax({
        url: 'http://127.0.0.1:5000/api',
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
        url: 'http://127.0.0.1:5000/api',
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

function loadHTML() {
    $.ajax({
        url: 'http://127.0.0.1:5000/body',
        type: 'GET',
        success: function (response) {
            $('#data').html(response);
            one();
        },
        error: function (error) {
            console.log(error);
        }
    });
}

loadHTML();
