#include <stdio.h>
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/

int max_of_four(int a, int b, int c, int d) {
    int the_max;
    if (a>b && a>c && a>d) {
        the_max = a;
    } else if (b>a && b>c && b>d) {
        the_max = b;
    } else if (c>a && c>b && c>d) {
        the_max = c;
    } else if (d>a && d>b && d>c) {
        the_max = d;
    }
    return the_max;
}

int main() {
    int a, b, c, d;
    //scanf("%d %d %d %d", &a, &b, &c, &d);
    a = 2;
    b = 5;
    c = 3;
    d = 8;
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}