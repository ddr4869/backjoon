#include<iostream>
#include<algorithm>
#include<string.h>
#include<vector>
#include<string>
using namespace std;
int N, M;
int arr[1001];
int cache[1001][1001];
int solve(int k, int num) {
	if (k == N) {
		if (arr[N] > num)return 1;
		else return 0;
	}
	int& ret = cache[k][num];
	if (ret != -1)return ret;
	ret = 0;
	for (int i = k + 1; i <= N; i++)
		if (num < arr[i])
			ret = max(ret, 1 + solve(i, arr[i]));
	return ret;
}

int main() {
	memset(cache, -1, sizeof(cache));
	cin >> N;
	for (int i = 1; i <= N; i++)
		cin >> arr[i];
	cout << solve(0, 0) << endl;
}