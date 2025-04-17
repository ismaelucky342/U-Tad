# AEC5: Implementation of a Phonebook with a Hash Table

This project involves the implementation of a phonebook that uses a **hash table** to store contacts, where each contact consists of a name and a phone number. The phonebook is implemented in two versions:

- **Exercise 1**: Implementation of a hash table without collision handling.
- **Exercise 2**: Implementation of a hash table with **open addressing** to handle collisions.

## Objectives

- Learn how to implement hash tables in C++.
- Understand collision handling in hash tables.
- Perform basic storage and search operations on a phonebook.

---

## Exercise 1: **Phonebook without Collisions**

### Description:
In this exercise, a phonebook is implemented using a hash table to store contacts. However, **collisions are not handled**, meaning that if two phone numbers have the same hash value, the system will overwrite the existing contact without any additional handling.

### Attributes of the `Agenda` Class:
- `int capacity`: Specifies the capacity of the hash table (maximum number of contacts).
- `String* names`: Array that stores the names of the contacts.
- `long* phones`: Array that stores the phone numbers.
- `bool* occupied`: Array that indicates whether a position in the table is occupied.

### Methods:
- **Constructor**: Initializes the table with a specified capacity.
- **Destructor**: Frees the memory allocated to the table.
- **obtainPosition(long phone)**: Returns the corresponding position in the hash table using a simple hash function based on the modulo operation.
- **contactExists(long phone)**: Checks if a contact is stored in the table.
- **getContact(long phone)**: Returns the name of the contact corresponding to the given phone number.
- **addContact(long phone, string contact)**: Adds a new contact to the table.
- **deleteContact(long phone)**: Deletes a contact from the hash table.
- **print()**: Displays all the contacts stored in the table (this method should not be implemented by the student).

### Considerations:
- **No collision handling**: Techniques such as linked lists or open addressing are not used. If a collision occurs, the previous contact is overwritten.

---

## Exercise 2: **Phonebook with Open Addressing**

### Description:
In this exercise, the phonebook also uses a hash table to store contacts, but now **collisions are handled** using the **open addressing** technique. This means that if two contacts have the same hash position, the system will search for a free position further in the table to store the new contact.

### Attributes of the `Agenda` Class:
- `int capacity`: Specifies the capacity of the hash table (maximum number of contacts).
- `int n`: Current number of elements in the table.
- `LinkedList* table`: Array of linked lists that stores the contacts in the corresponding positions of the table.

### Methods:
- **Constructor**: Initializes the table with a specified capacity.
- **Destructor**: Frees the memory allocated to the table and its linked lists.
- **obtainPosition(long phone)**: Uses a hash function to calculate the corresponding position of the phone number.
- **contactExists(long phone)**: Verifies if a contact exists in the table.
- **getContact(long phone)**: Returns the name of the contact associated with the phone number.
- **addContact(long phone, string contact)**: Adds a contact, handling collisions using open addressing.
- **deleteContact(long phone)**: Deletes a contact from the hash table.
- **print()**: Displays all the contacts stored in the table (this method should not be implemented by the student).

### Considerations:
- **Collision handling**: In case of a collision, the table uses open addressing to find the next available position, ensuring that contacts are not overwritten.
- **Use of linked lists**: Each cell of the hash table is a linked list that stores the contacts sharing the same hash position.

---

## **Compilation and Usage with Makefile**

### To compile and run the project, use the provided **Makefile**. The Makefile automatically compiles the source code and links the generated files.

### Usage Instructions:

1. **Compilation**:
    In the terminal, navigate to the root folder of the project and run the following command to compile the project:

    ```bash
    make
    ```

2. **Execution**:
    Once the project is compiled, you can run the program with the following command:

    ```bash
    ./bin/exercise_1
    ```

### Makefile Structure:

The Makefile contains the following key configurations:

- **Compilation**: Converts `.cpp` source files into `.o` object files.
- **Executable Generation**: Creates the final executable in `bin/exercise_1`.
- **Cleanup**: Removes the generated object files and executable with the command `make clean`.

### Available Menu Operations:

- **C**: Check if a contact is in the phonebook.
- **V**: View a contact in the phonebook.
- **A**: Add a contact to the phonebook.
- **E**: Delete a contact from the phonebook.
- **I**: Print the entire hash table.
- **S**: Exit the program.

---

## Complexity Analysis

### Exercise 1 (Without Collisions):

- **Insert a contact**: O(1) on average.
- **Search for a contact**: O(1) on average.
- **Delete a contact**: O(1) on average.

### Exercise 2 (With Open Addressing):

- **Insert a contact**: O(1) on average, but can reach O(n) in the worst case if the table is nearly full.
- **Search for a contact**: O(1) on average, but can reach O(n) if there are many collisions.
- **Delete a contact**: O(1) on average, but can also reach O(n) in the worst case if the table is full.

# Extra
![alt text](image.png)
