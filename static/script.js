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



function loadHTML() {
    $.ajax({
        url: 'https://api-practice-wine.vercel.app/body',
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