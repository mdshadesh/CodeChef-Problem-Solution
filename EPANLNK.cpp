#include <bits/stdc++.h>
#define ll long long 

using namespace std;

int remain(string s)
{
    ll int n=s.size();
    if(n>1){
        int num=(s[n-2]-'0')*10+(s[n-1]-'0');
        return num%20;
    }
    else
     return (s[0]-'0');
}
int main() 
{
	ll int t;
	cin>>t;
	while(t--){
	    string pan;
	    cin>>pan;
	    cout<<remain(pan)<<endl;
	}
	return 0;
}