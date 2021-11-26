#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void update(int *a,int *b) {
    // Complete this function
    int x, y;
    x = (*a + *b);
    y = abs(*a - *b);
    *a = x;
    *b = y;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    printf("Enter two integers:");
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d\n", a, b);

    return 0;
}