#include <bits/stdc++.h>
using namespace std;

int main() {
    int T; cin >> T;
    while(T--)
    {
        int N, K; cin >> N >> K;
        for(int i = 0; i < N; i++)
        {
            int I; cin >> I;
            if(K >= I)
            {
                K-= I;
                cout << 1;
            }
            else cout << 0;
        }
        cout << endl;
    }
	return 0;
}
