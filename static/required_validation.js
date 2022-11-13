const forms = document.getElementsByClassName("site-form");

for (const loadedForm of forms) {
    loadedForm.addEventListener('submit', (e) => {
        let valid = true;
        let elements = loadedForm.getElementsByTagName("input");

        for (const element of elements) {
            if (element.hasAttribute("required") && (element.value === "" || element.value === null)) {
                element.textContent = "You have to fill in this field!"
                valid = false;
            } else {
                element.textContent = "";
            }
        }

        elements = loadedForm.getElementsByTagName("textarea");
        for (const element of elements) {
            if (element.hasAttribute("required") && (element.value === "" || element.value === null)) {
                element.textContent = "You have to fill in this field!"
                valid = false;
            } else {
                element.textContent = "";
            }
        }

        if (!valid) {
            e.preventDefault();
        }
    });
}
