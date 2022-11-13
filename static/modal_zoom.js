let items = document.querySelectorAll('.carousel-item');
let modal = document.getElementById("zoomModal");
let modalContent = document.getElementById("modalContent")

for (let i = 0; i < items.length; i++) {
    let item = items[i]
    item.addEventListener('click', (e) => {
        let image = item.getElementsByTagName("img")[0]
        enlarge(image);
    });

    modal.addEventListener('dblclick', (e) => {
        shrink();
    });

    let lastTap = 0;
    modal.addEventListener('touchend', function (e) {
        let time = new Date().getTime();
        let tapLength = time - lastTap;
        if (tapLength < 500 && tapLength > 0) {
            e.preventDefault();
            shrink();
        }
        lastTap = time;
    });
}

function enlarge(image) {
    modal.style.display = "block";
    modalContent.src = image.src
    modalContent.alt = image.alt
}

function shrink() {
    modal.style.display = "none";
}
