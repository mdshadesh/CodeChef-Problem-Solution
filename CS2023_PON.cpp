#include <bits/stdc++.h>
#include<math.h>

using namespace std;

int main() 
{
	int t; cin>>t; 
	while(t--)
	{
	    int n, b;
	    cin>>n>>b;
	    int i=0,  c=-1;
	    while(i<n){
	        int a ; cin>>a; if((a&b)==b) c&=a;
	        i++;
	    }
	    if(c==b) 
	        cout<<"yes"<<endl;
	    else 
	        cout<<"no"<<endl;
	    
	}
	        
	return 0;
}