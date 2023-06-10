#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)	{
	    int k = 0, n;
	    cin>>n;
	    int a[2*n];
	    for(int i=0; i<2*n; i++)
	    {
	        cin>>a[i];
	    }
	    sort(a, a+2*n);
	    for(int i=0; i<2*n-1; i++){
	         if(a[i] == a[i+1]) {
	            k++;
	            if(k==2) {
	                cout<<"No"<<endl;
	                break;
	            }
	        }
	        else
	            k=0;
	    }
	    if(k<2)
	        cout<<"Yes"<<endl;
	}
	return 0;
}
