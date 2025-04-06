#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    // Define a string containing a passage from "Don Quixote".
    char *phrase = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income. The rest of it went in a doublet of fine cloth and velvet breeches and shoes to match for holidays, while on week-days he made a brave figure in his best homespun. He had in his house a housekeeper past forty, a niece under twenty, and a lad for the field and market-place, who used to saddle the hack as well as handle the bill-hook. His family consisted of a housekeeper somewhat advanced in years, a niece not quite twenty, and a lad for the field and market, who bore a resemblance to the master of the house in so far as he was not a little mischievous. The age of our gentleman bordered upon fifty years; he was of a robust constitution, spare, gaunt-featured, a very early riser and a great sportsman. They will have it his surname was Quixada or Quesada (for here there is some difference of opinion among the authors who write on the subject), although from reasonable conjectures it seems plain that he was called Quexana. But this is of but little importance to our tale; it will be enough not to stray a hair's breadth from the truth in the telling of it.";

    char c;
    int i = 0;
    FILE *filePointer;
    filePointer = fopen("quijote_2.txt","w");

    // Implement a while loop until the end of the input string.
    while ((c = phrase[i]) != '\0') {
        putc(c, filePointer); // Write character to file
        i++;
    }

    printf("%s", phrase); // Print the input string to console
    fclose(filePointer); // Close the file
    return 0;
}
