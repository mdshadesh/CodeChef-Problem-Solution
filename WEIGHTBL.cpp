#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main() {
	ll int t;
	cin>>t;
	while(t--)
	{
	    ll int w1,w2,x1,x2,m;
	    cin>>w1>>w2>>x1>>x2>>m;
	    int d = w2 - w1;
	    cout<< (d >= x1 * m && d <= x2 * m ) <<endl;
	}
	return 0;
}