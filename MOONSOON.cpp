#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	   long long int n,m,h,c=0;
	    cin>>n>>m>>h;
	    long long int a[n],b[m];
	    for(int i=0;i<n;i++){
	        cin>>a[i];
	    } 
	     for(int i=0;i<m;i++){
	        cin>>b[i];
	    }
	    sort(a,a+n);
	    sort(b,b+m);
	    for(int i=0;i<m;i++){
	        b[i]=b[i]*h;
	    }
	    
	   int d=min(n,m);
	    for(int i=0;i<d;i++){
	        if(a[n-i-1]<b[m-i-1]) c=c+a[n-i-1]; 
	         if(a[n-i-1]>=b[m-i-1]) c=c+b[m-i-1];
	    }
	    cout<<c<<endl;
	    
	}
	
	return 0;
}