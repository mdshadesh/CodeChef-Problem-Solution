#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int>v;
        int a[n];
        for(int i=0;i<n;++i){
            int x;
            cin>>x;
            v.push_back(x);
            a[i]=count(v.begin(),v.end(),v[i]);
        }
        int m=*max_element(a,a+n);
        cout<<n-m<<endl;
                
        }
	return 0;
}