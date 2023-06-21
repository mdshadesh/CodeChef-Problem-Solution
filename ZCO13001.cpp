#include <bits/stdc++.h>
#define ll long long int

using namespace std;

int main() 
{
    ll n; cin>>n;
    ll a[n];
    for(ll i=0;i<n;i++)
    {
        cin>>a[i];
    }
    sort(a,a+n);
    ll ans=0 , f=0 ,l=n-1;
    ll count=n-1;
    
    while(count>0)
    {
        ans+=count*(a[l--]);
        ans-=count*(a[f++]);
        count-=2;
    }
    cout<<ans<<endl;
	return 0;
}