// program: takes 3 integer, tests if summation of smaller 2 numbers, is grater than biggest number

#include <iostream>

using namespace std;

int main() {
    
    int num1, num2, num3, min, mid, max;
    cout << "Input 3 integers\n";
    cin >> num1 >> num2 >> num3;
    
    if(num1 > num2) {
        if(num1 > num3) {
            if(num2 > num3) {
                min = num3;
                mid = num2;
                max = num1;
            }
            else { 
                min = num2;
                mid = num3;
                max = num1;
            }
        }
        else {
            min = num2;
            mid = num1;
            max = num3;
        }
    }
    else {
        if(num2 > num3) {
            if(num1 > num3) {
                min = num3;
                mid = num1;
                max = num2;
            }
            else {
                min = num1;
                mid = num3;
                max = num2;
            }
        }
        else {
            min = num1;
            mid = num2;
            max = num3;
        }
    }
    
    if(min + mid > max)
        cout << "Congrats";
    else
        cout << "Try again";

}
