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
                console.log(data[i]);
                let div = document.createElement("div");
                let p = document.createElement("p");
                let a = document.createElement("a");
                a.setAttribute("class", "btn btn-primary gallery-result");
                a.setAttribute("data-toggle", "collapse");
                a.setAttribute("href", "#collapseE" + i);
                a.setAttribute("role", "button");
                a.setAttribute("aria-expanded", "true");
                a.setAttribute("aria-controls", "collapseE" + i);
                a.append(data[i]["fields"]["email"]);
                p.append(a);
                div.append(p);

                let div2 = document.createElement("div");
                div2.setAttribute("id", "collapseE" + i);
                div2.setAttribute("class", "colapse show");

                let div3 = document.createElement("div");
                div3.setAttribute("class", "card card-body faq-answer");
                div3.append(data[i]["fields"]["text"]);
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
