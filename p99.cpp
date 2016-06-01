#include <iostream>
#include <cmath>
using namespace std;

int sumofD(int n){
	int sum=0;
	while(n>0){
		sum=sum+n%10;
		n/=10;
	}
	return sum;
}

int main(){
	int p=0;
	int q=0;
	for(int i=10000;i<100000;i++){
		if(sumofD(i)==41){
			q++;
			if(i%11==0){
				p++;
			}
		}
	}
	cout<<p<<endl;
	cout<<q<<endl;
}
