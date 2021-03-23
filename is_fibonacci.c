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
	
	if(isFibo(number) == 1) {
        printf("%d is a fibonacci number.\n", number);
	}	 
	else {
        printf("%d is NOT a fibonacci number.\n", number);
	}
	
	system("pause");
	return 0;
}	

int isFibo(int f) {
	int temp;
	int a = 0;
	int b = 1;
	int status = 0;
	
	for(int i = 0; i < 20; i++) {
    	temp = a + b;
    	a = b;
    	b = temp;
    	
 	    if(f == a) {
	        status = 1;
	    }
	    
	}

	return status;

}
