function fetchdata() {
    $.ajax({
        url: "/index/refresh-counter",
        type: "get",
    }).done(function (data) {
        document.getElementById("counter").innerHTML = data["counter"]
    })
}

setInterval(fetchdata, 2000);