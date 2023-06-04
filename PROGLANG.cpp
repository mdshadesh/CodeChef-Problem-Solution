#include <iostream>
using namespace std;

int main() 
{
	int t;cin>>t;while(t--)
	{
	    int a,b,a1,b1,a2,b2;
	    cin>>a>>b>>a1>>b1>>a2>>b2;
	    bool isIn1 = (a==a1||a==b1)&&(b==a1||b==b1);
	    bool isIn2 = (a==a2||a==b2)&&(b==a2||b==b2);
	    if(isIn1) 
	        cout<<1<<endl;
	    else if(isIn2) 
	        cout<<2<<endl;
	    else 
	        cout<<0<<endl;
	}
	return 0;
}
