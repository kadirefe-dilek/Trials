#include <stdio.h>

int main()
{
    int min = 1000000000;
    int k;
    printf ("Enter an integer. Enter -1 to stop the process.\t");
    scanf("%d", &k);
    
    while(k != -1) { // here -1 is choosen as sentinel value
        if(k < min){
            min = k;
        }
        printf("Minimum of theese so far is: %d\n", min);
        
        printf("Enter the next integer. Enter -1 to stop.\t");
        scanf("%d", &k);
    }
    
    printf("Minimum of all theese is: %d", min);

    return 0;
}
