function validateEmail(email) {
  let re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

const loadedForm = document.getElementById("submitIdeaForm");

loadedForm.addEventListener('submit', (e) => {
    let messages = [];

    let emailValue = loadedForm.email.value
    if (emailValue === "" || emailValue === null) {
        messages.push("You have to put in your email address!");
    } else if (!validateEmail(emailValue)) {
        messages.push("Your email address is not properly formatted!")
    }

    if (loadedForm.text.value === "" || loadedForm.text.value === null) {
        messages.push("You have to put in your idea!");
    }

    if (messages.length > 0) {
        e.preventDefault();
        let messageText = "<p>" + messages.join("</p><p>") + "</p>";
        document.getElementById("errorMessage").innerHTML = messageText;
        setTimeout(function () {
            document.getElementById("errorMessage").innerHTML = "";
        }, 5000);
    }
})
