var document = "index.html"
var slider = document.getElementById("r");
var output = document.getElementById("d");
output.innerHTML = slider.value;

slider.oninput = function() {
    output.innerHTML = this.value;
}