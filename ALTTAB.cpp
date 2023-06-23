#include <bits/stdc++.h>
using namespace std;

int main() {
	
	    int n;
	    cin >> n;
	    
	    int cnt = 0;
	    unordered_map<string, int>mp;
	    for(int i = 0; i < n; ++i) {
	        string s; cin >> s;
	        mp[s] = cnt++;
	    }
	    
	    vector<pair<int, string>>vec;
	    for(auto &it : mp) {
	        vec.push_back({it.second, it.first});
	    }
	    
	    sort(vec.begin(), vec.end());
	    
	    string ans = "";
	    for(int i = vec.size() - 1; i >= 0; --i) {
	        string x = vec[i].second;
	        int sz = x.size();
	        ans += x.substr(sz - 2);
	    }
	    cout << ans << endl;
	
	return 0;
}