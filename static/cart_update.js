const Template = ({key, preview, name, text, quantity, price}) => `
    <div
        class="card rounded-3 mb-4 product"
        id="product${key}">
        <div
            class="card-body p-4">
            <div
                class="row d-flex justify-content-between align-items-center">
                <div
                    class="col-md-2 col-lg-2 col-xl-2">
                    <img
                        src="${preview}"
                        class="img-fluid rounded-3"
                        alt="${name}">
                </div>
                <div class="col-md-3 col-lg-3 col-xl-3">
                    <p class="lead fw-normal mb-2">${name}</p>
                    <p>${text}</p>
                </div>
                <div class="col-md-3 col-lg-3 col-xl-2 d-flex">
                    <input id="form${key}" min="0" name="quantity" value="${quantity}" type="number"
                           class="form-control form-control-sm quantityControl"/>
                </div>
                <div class="col-md-3 col-lg-2 col-xl-2 offset-lg-1">
                    <h5 class="mb-0">${price}$</h5>
                </div>
                <div class="col-md-1 col-lg-1 col-xl-1 text-end">
                    <button type="button" class="btn btn-danger remove-item" id="removeItem${key}">X</button>
                </div>
            </div>
        </div>
    </div>`;

function updateCart() {
    let xmlHttpReq;
    xmlHttpReq = new XMLHttpRequest();
    xmlHttpReq.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            let data = JSON.parse(this["response"]);
            document.getElementById("cart-price").textContent = data["price"];
            delete data["price"];

            for (let key in data) {
                if (!document.getElementById("product" + key)) {
                    let div = document.createElement("div");
                    div.innerHTML = [{
                        "key": key,
                        "preview": data[key]["preview"],
                        "name": data[key]["name"],
                        "text": data[key]["text"],
                        "quantity": data[key]["quantity"],
                        "price": data[key]["price"]
                    }].map(Template).join('');

                    document.getElementById("products-parent").prepend(div);

                    const input = document.getElementById('form' + key);
                    const removeButton = document.getElementById('removeItem' + key);
                    input.addEventListener('input', updateValue);
                    removeButton.addEventListener('click', removeItem);
                } else {
                    document.getElementById("product" + key).querySelector(".quantityControl").value = data[key]["quantity"];
                }
            }
        }
    };
    xmlHttpReq.open("GET", "update", true);
    xmlHttpReq.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttpReq.send();
    setTimeout(updateCart, 5000)
}

document.addEventListener("DOMContentLoaded", function () {
        setTimeout(updateCart, 1000);
    }
);

function updateValue(e) {
    let id = e.target.id;
    let xmlHttpReq;
    xmlHttpReq = new XMLHttpRequest();
    xmlHttpReq.open("POST", "update/quantity/", true);
    xmlHttpReq.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttpReq.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
    xmlHttpReq.send("id=" + id + "&value=" + e.target.value);
}

function removeItem(e) {
    let id = e.target.id;
    let xmlHttpReq;
    xmlHttpReq = new XMLHttpRequest();
    xmlHttpReq.open("POST", "remove/", true);
    xmlHttpReq.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttpReq.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
    xmlHttpReq.send("id=" + id);
    let num = id.match(/\d/g);
    num = num.join("");
    document.getElementById("product" + num).remove()
}

const submitButton = document.getElementById('submitCart');

submitButton.addEventListener("click", function () {
        let input = document.getElementById("billingEmail");
        let re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!re.test(input.value)) {
            document.getElementById("emailErrorMessage").innerHTML = "Your email address is not properly formatted!";
            setTimeout(function () {
                document.getElementById("emailErrorMessage").innerHTML = "";
            }, 5000);
        } else {
            let xmlHttpReq = new XMLHttpRequest();
            xmlHttpReq.open("GET", "stock/", true);
            xmlHttpReq.setRequestHeader("Content-type", "application/json;charset=UTF-8");
            xmlHttpReq.setRequestHeader("X-CSRFToken", CSRF_TOKEN);

            xmlHttpReq.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200) {
                    let data = JSON.parse(xmlHttpReq["response"]);
                    if (!data["message"] || data["message"].length === 0) {
                        let xmlHttpReq2 = new XMLHttpRequest();
                        xmlHttpReq2.open("POST", "submit/", true);
                        xmlHttpReq2.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                        xmlHttpReq2.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
                        xmlHttpReq2.send("email=" + input.value);
                        let products = document.getElementsByClassName("product");
                        while (products.length > 0) {
                            products[0].parentNode.removeChild(products[0]);
                        }
                        alert("Your order has been successfully registered! Details were sent to your email address.")
                    } else {
                        alert(data["message"]);
                    }
                }
            }
            xmlHttpReq.send();
        }
    }
)
;