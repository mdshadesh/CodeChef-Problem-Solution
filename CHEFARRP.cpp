#include <bits/stdc++.h>
#define ll long long 

using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t--)   {
        int n;
        cin >> n;
        int a[n];
        for(int i = 0; i < n; i++)        {
            cin >> a[i];
        }
        int c = 0;
        for(int i = 0; i < n; i++)       {
            int sum = 0, pro = 1;
            for(int j = i; j < n; j++)            {
                sum = sum + a[j];
                pro = pro * a[j];
                if(sum == pro)
                {
                    c++;
                }
            }
        }
        cout << c << endl;
    }
    cin.get();
}