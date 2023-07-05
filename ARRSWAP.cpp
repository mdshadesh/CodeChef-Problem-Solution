#include <bits/stdc++.h>
using namespace std;

int main() 
{
	int t;
	cin>>t;
	while(t--)
	{
	    long int n;
	    cin>>n;
	    long int minimum=LONG_MAX;
	    long int arr[2*n];
	    
	    for(int i=0;i<2*n;i++) cin>>arr[i];
	    
	    sort(arr,arr+2*n);
	    
	    for(int i=2*n-1;i>=n-1;i--)
	    {
	        minimum=min(minimum,arr[i]-arr[i-n+1]);
	    }
	    cout<<minimum<<endl;
	}
	
	return 0;
}