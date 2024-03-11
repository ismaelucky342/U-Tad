#include <stdio.h>
#include <stdlib.h>

// Enum to represent menu options
enum MenuOption {
    AddRecord = 49,     // '1' for adding a record
    DeleteRecord = 50,  // '2' for deleting a record
    ModifyRecord = 51,  // '3' for modifying a record
    ExitProgram = 52    // '4' for exiting the program
};

int main() {
    int option = 0;
    enum MenuOption userChoice;

    // Display the menu
    printf(" 1- Add Record \n 2- Delete Record \n 3- Modify Record \n 4- Exit\n");

    // Get user input for menu choice
    option = getchar();
    userChoice = option;

    // Switch statement to handle the chosen menu option
    switch (userChoice) {
        case AddRecord:
            printf("Adding a new record \n");
            break;
        case DeleteRecord:
            printf("Deleting a record \n");
            break;
        case ModifyRecord:
            printf("Modifying a record \n");
            break;
        case ExitProgram:
            printf("Program Exit \n");
            break;
        default:
            printf("Error! Invalid value \n");
            break;
    }

    return 0;
}

