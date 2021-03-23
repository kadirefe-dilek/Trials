/*	Kadir Efe Dilek
Create a program that takes in input and decides whether it was a fibonacci number or not.
This code tests for only the first 20 fibonacci numbers.
*/
#include <stdio.h>
#include <stdlib.h>

int isFibo (int);

int main (void) {
	
	int number;
	puts("Enter the number to be tested: ");
	scanf("%d", &number);
	
	if(isFibo(number) == 1) {	//calls the function to test the case
        printf("%d is a fibonacci number.\n", number);
	}	 
	else {
        printf("%d is NOT a fibonacci number.\n", number);
	}
	
	system("pause");
	return 0;
}	

int isFibo(int f) {
	int temp;	//holds the next number temporarily in the sequence 
	int a = 0;	//nth fibonacci number
	int b = 1;	//(n+1)th fibonacci number 
	int status = 0;	//last status of the given number to be returned by the function. İnitially, choosen as zero to provide control in the main.
	
	for(int i = 0; i < 20; i++) {	//
    	temp = a + b;	//creating the next number in the sequence
    	a = b;		
    	b = temp;	//shifting the positions of numbers
    	
 	    if(f == a || f == 0) {	//testing the case
	        status = 1;		//initializing to one to provide control in the main. 
	    }
	    
	}

	return status;

}
