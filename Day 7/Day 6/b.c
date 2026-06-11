#include <stdio.h>
#include <math.h> 

int main() {
    long long binary;
    long long decimal = 0; 
    int remainder, i = 0;

    printf("Enter a binary number: ");
    if (scanf("%lld", &binary) != 1) {
        printf("Invalid input.\n");
        return 1;
    }

    while (binary != 0) {
        remainder = binary % 10;
         decimal += remainder * (long long)pow(2, i);
        binary /= 10;
        i++;
    }
