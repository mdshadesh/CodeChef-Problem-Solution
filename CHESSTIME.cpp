#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;

        int games = N * 60 / 20;
        cout << games << endl;
    }

    return 0;
}
