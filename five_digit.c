#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    printf("Enter a five digit number: ");
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    /*
    Step 1: Get number by user
    Step 2: Get the modulus/remainder of the number
    Step 3: sum the remainder of the number
    Step 4: Divide the number by 10
    Step 5: Repeat the step 2 while number is greater than 0.
    */

    int sum = 0;
    int r;
    while (n>0) {
        r = n%10;
        sum += r;
        n = n/10;
    }
    printf("Sum: %d\n", sum);
    
    return 0;
}