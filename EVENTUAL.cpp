#include <bits/stdc++.h>
using namespace std;

int main() 
{
    int t,n;
    string s;
    for(cin>>t;t--;)
    {
        cin>>n>>s;
        int a[26] = {}, flag = 0;
        for(char c:s)
            a[c-'a']++;
        for(int i:a)
            if(i%2)
                flag = 1;
        cout << (flag?"NO":"YES") << endl;
    }
    return 0;
}