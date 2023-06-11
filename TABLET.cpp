#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        ll int n, b, area = 0, x = 0;
        cin >> n >> b;
        for(int i = 0; i < n; i++)
        {
            int w , h , c;
            cin >> w >> h >> c;
            if(c <= b)         {
                if(area < w*h)          {
                    area = w * h;
                    x = 1;
                }
            }
        }
        if(x == 1)       {
            cout << area << endl;
        } else        {
            cout << "no tablet" << endl;
        }
    }
    cin.get();
}
