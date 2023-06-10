#include <bits/stdc++.h>
using namespace std;

int main() {
    int B;
    cin >> B;
    if(B >= 1 && B <= 50) 
        cout << "100" << endl;
	else if(B >= 51 && B <= 100) 
	    cout << "50" << endl;
	else 
	    cout << "0" << endl;
	return 0;
}
