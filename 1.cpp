// C++ program to convert decimal
// number to ternary number

#include <cstdio>
#include <iostream>
#include <math.h>
using namespace std;
void convertToTernary(int Number)
{
	if (Number == 0)
		return;
	int x = Number % 3;
	Number /= 3;
	if (x < 0)
		Number += 1;
	convertToTernary(Number);
	if (x < 0)
		cout << x + (3 * -1);
	else
		cout << x;
}
int main()
{
	int a;
	cin>>a;
    if (a != 0) {
		convertToTernary(a);
	}
	else
		cout << "0" << endl;
// 	return 0;
}
