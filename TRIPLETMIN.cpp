
#include <bits/stdc++.h>
using namespace std;

void solve(){
    
    long long n, q;
    cin >> n >> q;
    vector<int> vec(n);
    for(auto &i:vec){
        cin >> i;
    }
    
    sort(vec.begin(), vec.end());


    map<long long , int> mp;
    long long current = 0;
    
    for (int i = 0; i < n-2; i++){
        current += ((n-i-2)*(n-i-1))/2;
        mp.insert({current, vec[i]});
    }


    for(int i = 0; i<q; i++){
        long long temp = 0;
        cin >> temp;
        cout << mp.lower_bound(temp)->second << endl;
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    long  long  t = 0;cin>>t;
    while (t--){
        solve();
    }
}