#include <stdio.h>

int main() {
  //declaring variables to be used.
	int how_many, number, max1, max2; //max1 to be the largest and max2 the second largest 
	int sum = 0;  //sum is initialized to 0 as default
	
	printf("How many numbers will you enter?\t");
	scanf("%d", &how_many);
	puts("");
        puts("");

	while(how_many != 0) {
	    printf("Enter an integer:\t");
	    scanf("%d", &number);
	    
        if(number > max1) {
            max2= max1; //max1 is now second greatest
            max1 = number;  //assigning new max1
        }
        else if (number > max2) {
            max2 = number;  //assigning new max2 value
        }
        
	    how_many--;
	}
	printf("Two largest numbers are: %d and %d.\n", max1, max2);
	sum = max1 + max2;
	printf("Sum of two largest is: %d", sum);

	return 0;
}
