using namespace std;

#include <iostream>
#include <vector>

int main() {
    int n, h;
    int j, k, c;
    
    bool b = false;

    cin >> n;
    cin >> h;

    vector<int> v(n); vector<int>::iterator i;

    for (j = 0; j < n; j++)
        cin >> v[j];
    
    i = v.begin();
    cin >> c;
    while (c != 0) {
        if (c == 1) {
            if (i != v.begin()) i--;
        } else if (c == 2) {
            if (i != v.end() - 1) i++;
        } else if (c == 3) {
            if (*i != 0 && b == false) {
                (*i)--;
                b = true;
            }
        } else if (c == 4) {
            if (*i != h && b == true) {
                (*i)++;
                b = false;
            }
        }

        cin >> c;
    }
    
    for (j = 0; j < n; j++)
        cout << v[j] << ' ';
    cout << endl;
}