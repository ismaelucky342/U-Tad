/** DOM Manipulation Functions */

// Function to change the text of an element by ID
function changeTextById(id, newText) {
    const element = document.getElementById(id);
    if (element) {
        element.textContent = newText;
    } else {
        console.error(`Element with ID ${id} not found.`);
    }
}

// Function to change the background color of an element by class name
function changeBackgroundColorByClass(className, color) {
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
function addListItemById(listId, itemText) {
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
function removeElementById(id) {
    const element = document.getElementById(id);
    if (element) {
        element.parentNode.removeChild(element);
    } else {
        console.error(`Element with ID ${id} not found.`);
    }
}

// Function to toggle visibility of an element by ID
function toggleVisibilityById(id) {
    const element = document.getElementById(id);
    if (element) {
        if (element.style.display === 'none') {
            element.style.display = '';
        } else {
            element.style.display = 'none';
        }
    } else {
        console.error(`Element with ID ${id} not found.`);
    }
}

// Exporting functions for external use
export {
    changeTextById,
    changeBackgroundColorByClass,
    addListItemById,
    removeElementById,
    toggleVisibilityById
};

