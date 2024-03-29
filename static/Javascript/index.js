var checked;
var checkbox = document.getElementById("flexSwitchCheckDefault");

document.addEventListener("DOMContentLoaded", () => {
    checked = false;
})


checkbox.addEventListener('change', () => {
    var page = window.location.pathname;
    checked = (!checked) ? true : false;
    handleCheck(checked, page);
})

function handleCheck(checked, page) {
    console.log(page)
    if (checked === true) {
        switch (page) {
            case "/":
            case "/redirect_to_login_page":
            case "/login":
                document.getElementById("Password").type = "text";
                break;
            case "/redirect_to_Register_page":
            case "/register":
                document.getElementById("registerPassword").type = "text";
                break;
            default:
                break;
        }
    }
    else {
        switch (page) {
            case "/":
            case "/redirect_to_login_page":
            case "/login":
                document.getElementById("Password").type = "password";
                break;
            case "/redirect_to_Register_page":
            case "/register":
                document.getElementById("registerPassword").type = "password";
                break;
            default:
                break;
        }
    }
}