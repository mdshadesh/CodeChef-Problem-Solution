#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

#define nl '\n'
#define pb push_back
#define ppb pop_back
#define mod 1000000007
#define pi 3.1415926535897932384626433832795

void yes() { cout<<"YES\n"; }
void no() { cout<<"NO\n"; }

void solve()
{
    ll n , m , k;
    cin >> n >>m >>k;
    vector<int>v;
    ll max = 0;
    for(int i = 0;i < n;i++)
        {
            int x;
            cin >> x;
            v.pb(x);

        }
    for(int i = 0;i < n;i++)
        {
            if(max < v[i])
                max = v[i];

        }
        ll res = max + k - 1;
        if(k == 1)
        {
            if(max <= m)
            {
                cout << "yes\n";
            }
            else
                cout << "No\n";
        }
        else
        {
            if(res <= m)
            {
                cout << "Yes\n";
            }
            else
            {
                cout << "No\n";
            }
        }



}

int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        solve();
    }


    return 0;
}