#include <bits/stdc++.h>
#include <stack>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        bool ans = true;
        int track=0;
        cin >> n;
        for (int i = 0; i < n; i++) {
            char temp;
            cin >> temp;
            if (temp == 'H') {
                track+=1;
                if(track>1) ans=false;
                
            }
            else if (temp == 'T') {
                if(track!=1) ans=false;
                track-=1;
                if(track<-1) ans=false;
            }
        }
        getchar();
        if(track!=0) 
            ans=false;
        if (ans)
            cout << "Valid" << endl;
        else
            cout << "Invalid" << endl;
    }

    return 0;
}
