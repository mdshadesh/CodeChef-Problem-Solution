#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n; cin>>n;
        int a[n],b=0;
        for(int i=0; i<n; i++) {
            cin>>a[i];
            b+=a[i];
        }
        if(b%2==0) {
            cout<<"yes"<<endl;
        }
        else {
            cout<<"no"<<endl;
        }
	}
	return 0;
}
