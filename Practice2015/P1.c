#include <stdio.h>

int main()
{
    int N, i, indexLen, tempInt, a, b, sum;
    
    scanf("%d", &N);
    
    int lst[N+1];
    
    sum = 0;
    for(i=0; i<N; i++)
    {
        scanf("%d", &tempInt);
        lst[i] = tempInt;
        sum = sum + tempInt;
    }
    lst[i+1] = 0;
    
    a = sum - lst[0];
    b = 0;
    i = 0;
    while(i<N)
    {
        if(a==b)
        {
            printf("%d", i);
        }
        b = b + lst[i];
        a = a - lst[i+1];
        i ++;
    }
    printf("\n");
}
