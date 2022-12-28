function showPrice() {
  let xmlHttpReq;
  xmlHttpReq = new XMLHttpRequest();
  xmlHttpReq.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
    document.getElementById("cart-price").textContent = this.responseText;
    }
  };
  xmlHttpReq.open("GET", "price", true);
  xmlHttpReq.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
  xmlHttpReq.send();
  setTimeout(showPrice, 5000)
}

document.addEventListener("DOMContentLoaded", function() {
  // run the first time; all subsequent calls will take care of themselves
  setTimeout(showPrice, 5000);
});