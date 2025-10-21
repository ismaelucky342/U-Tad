/** Browser Object Model (BOM) Functions */

// Function to get the current URL
function getCurrentURL() {
    return window.location.href;
}

// Function to redirect to a new URL
function redirectToURL(url) {
    window.location.href = url;
}

// Function to get the browser's user agent
function getUserAgent() {
    return navigator.userAgent;
}

// Function to open a new browser window
function openNewWindow(url, width = 600, height = 400) {
    window.open(url, '_blank', `width=${width},height=${height}`);
}

// Function to close the current browser window
function closeCurrentWindow() {
    window.close();
}

// Function to get the screen dimensions
function getScreenDimensions() {
    return {
        width: window.screen.width,
        height: window.screen.height
    };
}

// Function to display an alert dialog
function showAlert(message) {
    alert(message);
}

// Function to display a confirmation dialog
function showConfirm(message) {
    return confirm(message);
}

// Function to display a prompt dialog
function showPrompt(message, defaultValue = '') {
    return prompt(message, defaultValue);
}

// Example usage:
console.log("Current URL:", getCurrentURL());
console.log("User Agent:", getUserAgent());
console.log("Screen Dimensions:", getScreenDimensions());
// openNewWindow('https://www.example.com');
// showAlert("This is an alert!");
// const userResponse = showConfirm("Do you want to proceed?");
// const userInput = showPrompt("Please enter your name:", "Guest");

