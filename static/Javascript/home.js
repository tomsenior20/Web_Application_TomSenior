window.onload = initializeHiddenInputs;

function initializeHiddenInputs() {
    var locationInput = document.getElementById("location");
    var commentInput = document.getElementById("comment");
    var jobRoleInput = document.getElementById("JobRole");
    var companyInput = document.getElementById("company");

    document.getElementById("hidden_location").value = locationInput.textContent;
    document.getElementById("hidden_comment").value = commentInput.value;
    document.getElementById("hidden_JobRole").value = jobRoleInput.value;
    document.getElementById("hidden_company").value = companyInput.value;
}

function updateHiddenInput(fieldName, value) {
    document.getElementById(fieldName).value = value;
    document.getElementById("hidden_" + fieldName).value = value; // Update corresponding hidden input
}
