#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n,q,r=0;
	    cin>>n;
	    int *p = new int[n];
	    for(int i=0;i<n;i++)
	    {
	        cin>>p[i];
	        if(p[i]==1)
	            q=i;
	        else if(p[i]==n)
	            r=i;
	    }
	    if(r<q)
	        r = ((q-0)+(n-1-r))-1;
	    else
	        r = ((q-0)+(n-1-r));
	    
	    cout<<r<<"\n";
	}
	return 0;
}