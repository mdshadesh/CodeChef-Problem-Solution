#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int A, B;
        cin >> A >> B;
        int gap = A + B;
        cout << gap << endl;
    }

    return 0;
}
