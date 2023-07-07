#include<iostream>
#include<algorithm>

using namespace std;

int cnt[1000];

void solve()
{
    int m,a;
    cin>>m;
    int arr[10000]={0};
    for(int i=0;i<m;i++)
    {
        cin>>a;
        arr[a]++;
    }a=0;
    int brr[10000]={0};
    for(int i=0;i<10000;i++)
    {
        if(arr[i]>0){
            brr[arr[i]]++;
        }
    }int b=0;
    for(int i=0;i<10001;i++)
    {
        if(brr[i]>b){
            a=i;
            b=brr[i];
        }
    }
    cout<<a<<endl;
}

int main()
{
    int n;
    cin>>n;
    while(n--){
        solve();
    }
    return 0;
}