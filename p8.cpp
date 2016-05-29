#include <iostream>
#include <cmath>
using namespace std;

bool isprime(double a){
	double sq = sqrt(a);
	double nfact=0;
	for(double i=2;i<sq;i+=1.0){
		if(a%i==0.0){
			nfact++;
			return false;
		}
	}
	if (nfact==0)return true;
}
