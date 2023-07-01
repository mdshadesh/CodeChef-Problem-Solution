#include <bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);   cin.tie(NULL); cout.tie(NULL);
	int t; cin>>t;
	while(t--)
	{
        int n;  cin>>n; int flag=n , f=0 ,x;
        
        map<int,int> m; //frequency map
        vector<int> ans; //to store answer vector
        
        for(int i=0;i<n;i++)
        {
            cin>>x;
            m[x]++;
        }
       
        while(m[0]>0)
        {
            while(m[f]>0)
            {
                m[f]--;
                f++;
                flag--;
            }
            ans.push_back(f);
            f=0;
        }
        
        for(int i=0;i<flag;i++)
        {
            ans.push_back(0);
        }
        
        cout<<ans.size()<<"\n";
        for(auto &val:ans)
        {
            cout<<val<<" ";
        }
        cout<<"\n";
	}
}