#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    long long n,m;
	    cin>>n>>m;
	    long long g=__gcd(n,m);
	    long long mn=min(n,m);
	    if(g==1)	    {
	        cout<<1<<endl;
	    }
	    else	    {
	        cout<<g<<endl;
	    }
	}
	return 0;
}