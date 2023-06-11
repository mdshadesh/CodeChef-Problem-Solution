#include<bits/stdc++.h>

using namespace std;
typedef long long int ll;

int main ()
{
    ll t,n;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>n>>s;
        ll a=0,b=0;

        for(int i=0; i<n; i++)
        {
            if(s[i]=='1')
                a++;
            else
                b++;
        }
        if(b==n)
            cout<<0<<endl;
        else if(a==n)
            cout<<1<<endl;
        else if(a==b)
            cout<<a<<endl;
        else if(a<b)
            cout<<a<<endl;
            else
                cout<<b+1<<endl;
    }

}