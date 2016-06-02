#include <iostream>
using namespace std;

int mod(long long int n){
	int facmod=1;
	for(long long int i=1;i<=n;i++){
		facmod=((facmod%2097152)*201413)%2097152;
	}
	return facmod;
}

int main(){
	long long int n=1;
	while(mod(n)!=1){
		if(mod(n+1)==1){
			cout<<n+1<<endl;
		}
	}
}
