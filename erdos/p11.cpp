#include <iostream>
using namespace std;

int facmod(long long int n){
	long long int fac=1;
	for(long long int i=1;i<1000000009;i++){
		fac=((fac%1000000009)*i)%1000000009;
	}
	return fac;
}

int main()
{
cout<<facmod(1000000008)<<endl;
}
