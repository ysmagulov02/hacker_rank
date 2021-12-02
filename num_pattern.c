#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
  	// Complete the code to print the pattern.

    int len = 2*n - 1;
    int min;

    for (int i = 0; i < len; i++) {
        for (int j = 0; j < len; j++) {
            if (i < j) {
                min = i;
            } else {
                min = j;
            }
            if (min < len - i - 1) {
                min = min;
            } else {
                min = len - i - 1;
            }
            if (min < len - j - 1) {
                min = min;
            } else {
                min = len - j - 1;
            }
            printf("%d ", n - min);
        }
        printf("\n");
    }
      
    return 0;
}