#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(long long int n){
	int sq=(int)sqrt(n);
	if(n==2) return true;
	for(int i=2;i<=sq;i++){
		if(n%i==0) return false;
	}
	return true;
}

long long int fact(int n){
	if(n==0) return 1;
	else return n*fact(n-1);
}

int ncr(int n,int r){
	long long int num=fact(n);
	long long int den=fact(n-r)*fact(r);
	return num/den;
}

int power(long long int n, int p){
		int pow=0;
		while(n%p==0){
			pow+=1;
			n=n/p;
		}
		return pow;
}

long long int nOfq(long long int n){
	if (n==1) return 1;
	long long int prod=1;
	for(long long int i=2;i<=n;i++){
		//cout<<"Prime"<<isPrime(i)<<endl;
		if(isPrime(i)){
			int p=power(n,i);
			//cout<<"Power"<<" "<<p<<endl;
			if(p!=0){ 
				prod=prod*ncr(5*p-1,p );
				//cout<<prod<<endl;
			}
		}
	}
	//cout<<prod<<endl;
	return prod;
}

int main(){
	//cout<<ncr(4,2)<<endl;				Testing.
	//cout<<power(4,2)<<" "<<isPrime(23)<<endl;
	long long int upper=1000000000000;
	long long int sum=0;
	for(long long int i=1;i<=upper;i++){
		sum+=nOfq(i);
		//cout<<sum<<" "<<endl;
	}
	cout<<sum<<endl;
	//cout<<nOfq(2)<<endl;
	//cout<<power(2,2);
}
