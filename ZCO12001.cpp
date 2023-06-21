#include <bits/stdc++.h>

using namespace std;

using ll = long long;

int main() 
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
    int n; cin >> n;
    int v , pos = 1 , posOpening, posDepth, posWidthMax , depth = 0 , depthMax = 0 , widthMax = 0;
    
    for(int i=0; i<n; i++) 
    {
        cin >> v;
        if(v==1) 
        { // opening bracket
            if(depth==0)
                posOpening = pos;
            depth++;
            if(depth>depthMax) 
            {
                depthMax = depth;
                posDepth = pos;
            }
        }
        else 
        { // closing bracket
            depth--;
            if(depth==0) 
            {
                int width = pos-posOpening+1;
                if(width>widthMax) 
                {
                    widthMax = width;
                    posWidthMax = posOpening;
                }
            }
        }
        pos++;
    }
    cout << depthMax << ' ' << posDepth << ' ';
    cout << widthMax << ' ' <<  posWidthMax << endl;
}