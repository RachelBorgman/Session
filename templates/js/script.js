function plus_x(x) {
    var count = document.getElementById("count");
    count = count + parseInt(x)
    display.innerHTML = parseInt(count)
    return parseInt(count)
}