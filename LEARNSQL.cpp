#include <iostream>

using namespace std;

int main() {
    int R, C, E;
    cin >> R >> C >> E;

    int totalCells = (R + E) * C;

    cout << totalCells << endl;

    return 0;
}
