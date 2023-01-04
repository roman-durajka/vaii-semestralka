ajax_function(1);

function ajax_function(page) {
    let xmlHttpReq;
    xmlHttpReq = new XMLHttpRequest();
    xmlHttpReq.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            let element = document.getElementById("paginate")
            let data = JSON.parse(JSON.parse(xmlHttpReq.response));
            while (element.firstChild) {
                element.removeChild(element.firstChild);
            }
            for (let i = 0; i < data.length; i++) {
                let div = document.createElement("div");
                let p = document.createElement("p");
                let a = document.createElement("a");
                a.setAttribute("class", "btn btn-primary gallery-result");
                a.setAttribute("data-toggle", "collapse");
                a.setAttribute("href", "#collapseE" + i);
                a.setAttribute("role", "button");
                a.setAttribute("aria-expanded", "true");
                a.setAttribute("aria-controls", "collapseE" + i);
                a.append("Order number ");
                a.append(data[i]["pk"]);
                p.append(a);
                div.append(p);

                let div2 = document.createElement("div");
                div2.setAttribute("id", "collapseE" + i);
                div2.setAttribute("class", "collapse show");

                let div3 = document.createElement("div");
                div3.setAttribute("class", "card card-body faq-answer");
                let p1 = document.createElement("p");
                p1.append("Email: ");
                p1.append(data[i]["fields"]["email"]);
                let p2 = document.createElement("p");
                p2.append("Price: ");
                p2.append(data[i]["fields"]["price"]);
                p2.append("$");
                div3.append(p1);
                div3.append(p2);

                for (let key in data[i]["fields"]["data"]) {
                    let p3 = document.createElement("p");
                    p3.append("Item ID: " + key.toString() + "; ");
                    p3.append("Name: " + data[i]["fields"]["data"][key]["name"] + "; ");
                    p3.append("Quantity: " + data[i]["fields"]["data"][key]["quantity"].toString() + "; ");
                    div3.append(p3);
                }
                div2.append(div3);
                div.append(div2);

                element.append(div);
            }
        }
    };
    xmlHttpReq.open("POST", "paginate/", true);
    xmlHttpReq.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlHttpReq.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
    xmlHttpReq.send("page="+page);
}
