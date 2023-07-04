#include <iostream>
using namespace std;

int main() 
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n,a;
	    cin>>n>>a;
	    
	    if(a<(n-a)) 
	        cout<<a<<endl;
	    else 
	        cout<<(n-a)<<endl;
	 
	}
	return 0;
}