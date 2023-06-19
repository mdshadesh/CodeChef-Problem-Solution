#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int len;
        cin >> len;

        long long int a[len];
        long long int b[len];

        for (int i = 0; i < len; i++)
            cin >> a[i];

        for (int j = 0; j < len; j++)
            cin >> b[j];

        long long int cnt = 0;
        long long int max_om = 0;

        for (int i = 0; i < len; i++) {
            if (a[i] != 0) {
                cnt++;
                if (cnt > max_om)
                    max_om = cnt;
            } else {
                cnt = 0;
            }
        }

        long long int cnt_addy = 0;
        long long int max_addy = 0;
        for (int j = 0; j < len; j++) {
            if (b[j] != 0) {
                cnt_addy++;
                if (cnt_addy > max_addy)
                    max_addy = cnt_addy;
            } else {
                cnt_addy = 0;
            }
        }

        if (max_om == max_addy)
            cout << "Draw" << endl;
        else if (max_om > max_addy)
            cout << "Om" << endl;
        else
            cout << "Addy" << endl;
    }

    return 0;
}
