/** Event Handling Functions */

// Function to add an event listener to an element by ID
function addEventListenerById(id, event, handler) {
    const element = document.getElementById(id);
    if (element) {
        element.addEventListener(event, handler);
    } else {
        console.error(`Element with ID ${id} not found.`);
    }
}

// Function to remove an event listener from an element by ID
function removeEventListenerById(id, event, handler) {
    const element = document.getElementById(id);
    if (element) {
        element.removeEventListener(event, handler);
    } else {
        console.error(`Element with ID ${id} not found.`);
    }
}

// Example usage:
// addEventListenerById('myButton', 'click', () => alert('Button clicked!'));
// removeEventListenerById('myButton', 'click', myClickHandler);

// Exporting functions for external use
export {
    addEventListenerById,
    removeEventListenerById
};

// Function to change the text content of an element by ID
export function changeTextById(id, newText) {
    const element = document.getElementById(id);
    if (element) {
        element.textContent = newText;
    } else {
        console.error(`Element with ID ${id} not found.`);
    }
}

// Function to change the background color of an element by class name
export function changeBackgroundColorByClass(className, color) {
    const elements = document.getElementsByClassName(className);
    if (elements.length > 0) {
        Array.from(elements).forEach(element => {
            element.style.backgroundColor = color;
        });
    } else {
        console.error(`No elements found with class name ${className}.`);
    }
}

// Function to add a new list item to a ul or ol by ID
export function addListItemById(listId, itemText) {
    const list = document.getElementById(listId);
    if (list) {
        const newItem = document.createElement('li');
        newItem.textContent = itemText;
        list.appendChild(newItem);
    } else {
        console.error(`List with ID ${listId} not found.`);
    }
}

// Function to remove an element by ID
export function removeElementById(id) {
    const element = document.getElementById(id);
    if (element) {
        element.parentNode.removeChild(element);
    } else {
        console.error(`Element with ID ${id} not found.`);
    }
}       