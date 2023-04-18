function login() {
    // Get input values
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Add your login validation logic here
    // Example: check if username and password are valid
    if (username === "admin" && password === "123456") {
        // Redirect to web console or perform other actions
        window.location.href = "console.html"; // replace "console.html" with the appropriate URL for your web console
        return false; // prevent form submission
    } else {
        // Display error message
        document.getElementById("error-msg").innerHTML = "Invalid username or password.";
        return false; // prevent form submission
    }
}
