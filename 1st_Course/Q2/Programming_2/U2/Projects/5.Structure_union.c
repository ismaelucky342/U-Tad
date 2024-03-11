union user_id {

struct NIF {
    unsigned int number; 
    char c; 
}nif;

struct CIF
{
    unsigned int number; 
    char c; 
}cif; 

char Passport[8];

struct NIE
{
    char prefix; 
    unsigned int number; 
    char suffix; 
}nie; 

char username[16]; 

}; 
/*The form of storage is different when we compare a union with respect to a structure. 
 A structure ("struct") allows related variables to be stored together and in contiguous
 memory locations. 
 In contrast, unions store multiple members in a package, but instead of placing their members one after another, 
  all the members overlap each other in the same position.*/

// Alternative structuring 

struct NIF {
    unsigned int number; 
    char c; 
}nif;

struct CIF
{
    unsigned int number; 
    char c; 
}cif; 

char Passport[8];

struct NIE
{
    char prefix; 
    unsigned int number; 
    char suffix; 
}nie; 

struct user_id {
    struct NIF nif;  
    struct CIF cif;  
    char username[16]; 
    struct NIE nie; 
    char Passport[8];
}; 