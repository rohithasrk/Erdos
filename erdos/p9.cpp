#include <iostream>
#include <cmath>
using namespace std;

int nfact(long long int n){
	int nfac=0;
	double sqr = sqrt(n);
	long long int sqrtn = int(sqrt(n));
	for(long long int i=1;i<sqrtn;i++){
		if(n%i==0) nfac++;
	}
	if(sqr==sqrtn) return 2*nfac-1;
	else return 2*nfac;
}

int main(){
	long long int number=1;
	while(nfact(number)<300){
		if(nfact(number+1)>=300){
			cout<<number+1<<endl;
		}
	number++;
	}
}
