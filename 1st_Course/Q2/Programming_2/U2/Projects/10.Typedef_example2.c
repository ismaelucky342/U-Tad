#include <stdio.h>

// Define a structure named 'student_t' to represent student information
typedef struct student{
    int ID;     // Student ID
    int Grade;  // Student Grade
} Student_t;

int main() {
    // Declare an array of 10 student variables of type 'Student'
    Student_t s[10];

    int i, j;

    // Assign values to the attributes of the first 5 students in the array
    for (i = 0; i < 5; i++) {
        s[i].ID = i + 1;
        s[i].Grade = i + 80;
    }

    // Print the average grade of each of the first 5 students
    for (j = 0; j < 5; j++) {
        printf("The average grade of student %d is %d. \n", s[j].ID, s[j].Grade);
    }

    return 0;
}
