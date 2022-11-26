#include <iostream>
using namespace std;


int main(){
	ios_base::sync_with_stdio(false);
	
	int hour, min;
	cin >> hour >> min;
	
	if (min >= 45)printf("%d %d", hour, min - 45);
	else if (hour != 0 && min >= 45) printf("%d %d", hour - 1, min - 45);
	else if (hour != 0 && min < 45) printf("%d %d", hour - 1, min + 15);
	else if (hour == 0 && min >= 45) printf("%d %d", hour + 23, min - 45);
	else if (hour == 0 && min < 45) printf("%d %d", hour + 23, min + 15);
	return 0;
}
