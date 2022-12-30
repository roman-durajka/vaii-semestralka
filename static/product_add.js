const elements = document.getElementsByClassName('product-add');

for (let i = 0; i < elements.length; i++) {
    elements[i].addEventListener('click', addToCart);
}

function addToCart(e) {
    let id = e.target.id;
    let xmlHttpReq;
    xmlHttpReq = new XMLHttpRequest();
    xmlHttpReq.open("POST", "/shop/cart/add/", true);
    xmlHttpReq.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttpReq.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
    xmlHttpReq.send("id="+id);
    alert("Item added to cart!");
}