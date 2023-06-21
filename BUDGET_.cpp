#include <bits/stdc++.h>
#define ll long long 

using namespace std;

int main() 
{
    ll int a;
    cin>>a;
    while(a--)
    {
        ll int b, c, sum;
        cin >> b >>c ;
        
        sum = c * 30;
        
        if(b >= sum)
        {
            cout<<"Yes"<<endl;
        }
        else{
            cout<<"No"<<endl;
        }
    }
	
	return 0;
}
