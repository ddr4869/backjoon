#include <iostream>
#include <string>
#include <vector>
#include <math.h>
using namespace std;
vector<int> val;


int main(){
	ios_base::sync_with_stdio(false);
	string color;
	for(int i=0;i<3;i++){
		cin >> color;
		if (color=="black") val.push_back(0);
		else if (color=="brown") val.push_back(1);
		else if (color=="red") val.push_back(2);
		else if (color=="orange") val.push_back(3);
		else if (color=="yellow") val.push_back(4);
		else if (color=="green") val.push_back(5);
		else if (color=="blue") val.push_back(6);
		else if (color=="violet") val.push_back(7);
		else if (color=="grey") val.push_back(8);
		else if (color=="white") val.push_back(9);
	}

	int a,b,c;
	c = val.back();
	val.pop_back();
	b = val.back();
	val.pop_back();
	a = val.back();
	
	long long result = (10*a+b)*pow(10,c);
	cout << result << endl;
	
	return 0;
}
