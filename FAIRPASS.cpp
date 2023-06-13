#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N, K;
        cin >> N >> K;

        if (K >= N)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}
