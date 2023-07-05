#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N, M, K;
        cin >> N >> M >> K;

        unordered_set<int> ignoredFiles;
        unordered_set<int> trackedFiles;

        for (int i = 0; i < M; ++i) {
            int file;
            cin >> file;
            ignoredFiles.insert(file);
        }

        for (int i = 0; i < K; ++i) {
            int file;
            cin >> file;
            trackedFiles.insert(file);
        }

        int trackedAndIgnored = 0;
        int untrackedAndUnignored = 0;

        for (int i = 1; i <= N; ++i) {
            if (ignoredFiles.count(i) && trackedFiles.count(i))
                ++trackedAndIgnored;
            else if (!ignoredFiles.count(i) && !trackedFiles.count(i))
                ++untrackedAndUnignored;
        }

        cout << trackedAndIgnored << " " << untrackedAndUnignored << endl;
    }

    return 0;
}
