#include <iostream>
using namespace std;

#define MAX 200000

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T;
    cin >> T;
    for (int i = 1; i < T + 1; i++) {
        int N;
        cin >> N;
        int *books = new int[N];
        int tmp_list[MAX][MAX];
        
        for (int j = 0; j < N; j++) {
            int isTrue = -1;
            for (int t; t < sizeof(tmp_list); t++) {
                if (tmp_list[t][-1] + 1 == books[j]) {
                    isTrue = t;
                }
            }
        }
    }
}