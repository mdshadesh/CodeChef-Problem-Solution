#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;
        int B;
        cin >> B;
        int current = -1;
        int i = 0;

        while (i < N) {
            int AX;
            cin >> AX;
            if ((AX & B) == B)
                current &= AX;
            i++;
        }

        if (current == B)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}