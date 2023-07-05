#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int size;
        cin >> size;

        vector<int> vec;

        int prevEle, currEle;
        cin >> prevEle;

        int sub, count = 1;

        while (--size) {
            cin >> currEle;
            sub = abs(currEle - prevEle);
            if (sub > 2) {
                vec.push_back(count);
                count = 1;
            } else {
                count++;
            }
            prevEle = currEle;
        }

        vec.push_back(count); // If last comparison is lesser than 2, then count will not be able to store in vector. So, we push count after completion of the loop. And if the value is > 2, then in the vector, the last and second last element will be similar.

        sort(vec.begin(), vec.end());

        cout << vec.front() << " " << vec.back() << endl;
    }
    return 0;
}
