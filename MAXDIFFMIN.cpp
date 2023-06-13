#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int a, b, c;
        cin >> a >> b >> c;

        int diff = (max(max(a, b), c) - min(min(a, b), c));

        cout << diff << endl;
    }

    return 0;
}
