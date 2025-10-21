/** Form Handling Functions */

// Function to get form data as an object   
export function getFormData(formId) {
    const form = document.getElementById(formId);
    const formData = {};
    if (form) {
        const inputs = form.elements;
        for (let i = 0; i < inputs.length; i++) {
            const input = inputs[i];
            if (input.name) {
                formData[input.name] = input.value;
            }
        }
    } else {
        console.error(`Form with ID ${formId} not found.`);
    }
    return formData;
}

// Function to set form data from an object
export function setFormData(formId, data) {
    const form = document.getElementById(formId);
    if (form) {
        const inputs = form.elements;
        for (let i = 0; i < inputs.length; i++) {
            const input = inputs[i];
            if (input.name && data.hasOwnProperty(input.name)) {
                input.value = data[input.name];
            }
        }
    } else {
        console.error(`Form with ID ${formId} not found.`);
    }
}

// Function to reset a form by ID
export function resetForm(formId) {
    const form = document.getElementById(formId);
    if (form) {
        form.reset();
    } else {
        console.error(`Form with ID ${formId} not found.`);
    }
}

// Exporting functions for external use
export {
    getFormData,
    setFormData,
    resetForm
};

