function showPrice() {
  let xhttp;
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
    document.getElementById("cart-price").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "price", true);
  xhttp.send();
  setTimeout(showPrice, 5000)
}

document.addEventListener("DOMContentLoaded", function() {
  // run the first time; all subsequent calls will take care of themselves
  setTimeout(showPrice, 5000);
});