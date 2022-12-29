const Template = ({key, preview, name, text, quantity, price}) => `
    <div
        class="card rounded-3 mb-4"
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
                    <input id="form1" min="0" name="quantity" value="${quantity}" type="number"
                           class="form-control form-control-sm"/>
                </div>
                <div class="col-md-3 col-lg-2 col-xl-2 offset-lg-1">
                    <h5 class="mb-0">${price}$</h5>
                </div>
                <div class="col-md-1 col-lg-1 col-xl-1 text-end">
                    <button type="button" class="btn btn-danger">
                        <a href="#" class="remove-item">X</a>
                    </button>
                </div>
            </div>
        </div>
    </div>`;

function showPrice() {
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
                } else {
                    document.getElementById("product" + key).querySelector("#form1").value = data[key]["quantity"];
                }
            }

        }
    };
    xmlHttpReq.open("GET", "update", true);
    xmlHttpReq.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlHttpReq.send();
    setTimeout(showPrice, 5000)
}

document.addEventListener("DOMContentLoaded", function () {
        setTimeout(showPrice, 1000);
    }
);


const input = document.getElementById('form1');

input.addEventListener('input', updateValue);

function updateValue(e) {
    let id = e.target.parentElement.parentElement.parentElement.parentElement.id;
    let xmlHttpReq;
    xmlHttpReq = new XMLHttpRequest();
    xmlHttpReq.open("POST", "update/quantity/", true);
    xmlHttpReq.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttpReq.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
    xmlHttpReq.send("id="+id+"&value="+e.target.value);
}
