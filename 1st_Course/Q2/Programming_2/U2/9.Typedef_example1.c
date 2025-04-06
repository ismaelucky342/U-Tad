#include <stdio.h>

// Define a structure named 'student_t' to represent student information
typedef struct student
{
    int ID;     // Student ID
    int Grade;  // Student Grade
} Student_t;

int main() {
    // Declare two student variables of type 'Student'
    Student_t student1, student2;

    // Assign values to the attributes of the first student
    student1.ID = 1;
    student1.Grade = 85;

    // Assign values to the attributes of the second student
    student2.ID = 2;
    student2.Grade = 74;

    // Print the average grade of the first student
    printf("The average grade of student %d is %d. \n", student1.ID, student1.Grade);

    // Print the average grade of the second student
    printf("The average grade of student %d is %d. \n", student2.ID, student2.Grade);

    return 0;
}


