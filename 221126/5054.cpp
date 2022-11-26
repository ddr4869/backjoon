#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;
int Xi[23];


int main(){
	ios_base::sync_with_stdio(false);
	int T, N, result;
	cin >> T;
	while(T--){
		cin >> N;
		int sum=0;
		int MAX=0, MIN=100;
		for(int i=0;i<N;i++){
			cin >> Xi[i];
			sum+=Xi[i];
			if (Xi[i]>MAX) MAX=Xi[i];
			if (Xi[i]<MIN) MIN=Xi[i];
		}
		int middle = sum/=N;
		result= (MAX-middle)+(middle-MIN);
		cout << 2*result << endl;
	}
	return 0;
}
