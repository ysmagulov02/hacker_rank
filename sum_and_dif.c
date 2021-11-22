#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int a, b;
    int int_sum = 0;
    int int_dif = 0;
    float c, d;
    float float_sum = 0.0;
    float float_dif = 0.0;
    
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    printf("Enter two floats: ");
    scanf("%f %f", &c, &d);
    int_sum = a + b;
    int_dif = a - b;
    float_sum = c + d;
    float_dif = c - d;
    printf("\n%d %d", int_sum, int_dif);
    printf("\n%.1f %.1f\n", float_sum, float_dif);
     
    return 0;
}