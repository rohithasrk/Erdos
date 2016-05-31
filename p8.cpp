#include <iostream>
#include <cmath>
using namespace std;

bool isprime(long int a){
	long int sq = int(sqrt(a));
	long int nfact=0;
	for(long int i=2;i<sq;i++){
		if(a%i==0){
			nfact++;
			return false;
		}
	}
	if (nfact==0) return true;
}
int sumOfDigits(long int n){
	int sum=0;
	while(n>0){
		sum+=n%10;
		n/=10;
	}
	return sum;
}

int main(){
	long int sum=2;
	for(long int i=2;i<1000000000;i++){
		if(isprime(i)){
			sum+=sumOfDigits(i);
		}
	}
	cout<<sum<<endl;
}
