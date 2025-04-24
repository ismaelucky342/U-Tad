# POO Final Exam: Exercise 5

## Overview

Develop a program to manage a digital library. The system should allow registering users, managing books, and handling book loans.

---

## Required Functionalities

### Book Management
- Add books with attributes: **title**, **author**, **ISBN**, and **availability** (borrowed or not).
- List all available books and those currently borrowed.
- Search for books by **title** or **author**.

### User Management
- Register users with attributes: **name**, **email**, and a list of currently borrowed books.

### Loans
- Allow a registered user to borrow an available book.
- Return a borrowed book.
- Restrict the maximum number of books a user can borrow (e.g., 3).

### Storage
- Save the list of books and users in separate files.
- Load the data when starting the application.

---

## Example Application Menu

```
=== Main Menu ===
1. Manage books
2. Manage users
3. Borrow a book
4. Return a book
5. Save and exit
Select an option:
```

---

## Important Details

- **Error Handling**: Each functionality should handle possible errors using exceptions, such as:
    - Attempting to borrow a book that is already borrowed.
    - Attempting to return a book that is not borrowed.
    - Registering a user with an already existing email.
- **Input Validation**: Implement validations for data input (e.g., do not accept an empty book title).

---

## Example Usage

1. The user selects **“1. Manage books”** and adds a new book to the library.
2. They select **“2. Manage users”** and register a user named “Juan Pérez.”
3. In **“3. Borrow a book,”** they select a book and a user to associate them.
4. In **“4. Return a book,”** they mark a book as returned by the corresponding user.
5. They save the changes and close the application.

---

## Evaluation Criteria

- **Code Structure**: Clarity, use of classes and methods.
- **Exception Handling**: Validation of input data and logic for possible errors in loans and returns.
- **File Usage**: Correct saving and loading of data.
- **Best Practices**: Clear comments and consistency in naming conventions.
