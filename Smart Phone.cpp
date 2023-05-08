#include<iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;

int main()
{
    long long int n,i,money;

    cin>>n;

    long long int array[n];

    for(i=0;i<n;i++)
        scanf("%lld",&array[i]);

    sort(array,array+n);

    money=array[n-1];

    for(i=n-2;i>=0;i--)
    {
        if(array[i]*(n-i)>money)
           money=array[i]*(n-i);
    }

    cout<<money;

    return 0;
}

